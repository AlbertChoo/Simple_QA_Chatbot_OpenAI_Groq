import requests
import streamlit as st 
import openai
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Simple Q&A Chatbot With OpenAI & Groq"

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to user queries in a friendly and conversational manner."),
        ("user", "Question:{question}"),
    ]
)

def validate_api_key(api_key, provider):
    """Validate the API key by making a test request."""
    try:
        if provider == "OpenAI":
            openai.api_key = api_key
            openai.Model.list()
        elif provider == "Groq":
            llm = ChatGroq(model="mixtral-8x7b-32768", groq_api_key=api_key)
            llm.invoke("Hello")  # Test invocation
        return "APPROVED"
    except Exception as e:
        return f"Invalid API Key: {str(e)}"

def generate_response(question, api_key, engine, provider, temperature, max_tokens):
    if provider == "OpenAI":
        llm = ChatOpenAI(model=engine, openai_api_key=api_key)
    else:
        llm = ChatGroq(model=engine, groq_api_key=api_key)
    
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({"question": question})
    return answer

# Streamlit App Title
st.title("Chat with AI")

# Sidebar for Model Selection
provider = st.sidebar.selectbox("Select Provider", ["OpenAI", "Groq"])

if provider == "OpenAI":
    engine = st.sidebar.selectbox("Select OpenAI Engine", ["gpt-3.5-turbo", "gpt-4", "gpt-4o", "gpt-4-turbo"])
    api_key = st.sidebar.text_input("Enter OpenAI API Key", type="password")
    api_url = "https://api.openai.com/v1/chat/completions"

elif provider == "Groq":
    engine = st.sidebar.selectbox("Select Groq Engine", ["llama-3.1-8b-instant", "qwen-2.5-coder-32b", "gemma2-9b-it"])
    api_key = st.sidebar.text_input("Enter Groq API Key", type="password")
    api_url = f"https://api.groq.com/openai/v1/chat/completions"

# User Input
user_input = st.text_area("Enter your message:")

# Debugging: Show selected provider and engine
st.sidebar.write(f"**Provider:** {provider}")
st.sidebar.write(f"**Engine:** {engine}")

# Function to call the API
def chat_with_ai(prompt):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": engine,
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(api_url, json=data, headers=headers)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.text}"

# Submit Button
if st.button("Send"):
    if api_key and user_input:
        response = chat_with_ai(user_input)
        st.text_area("Response:", response, height=200)
    else:
        st.warning("Please enter an API key and a message.")
