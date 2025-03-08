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
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]="Simple Q&A Chatbot With OpenAI"

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please response to user queries in a friendly and conversational manner."),
        ("user", "Question:{question}"),
    ]
)

def generate_response(question, api_key, engine, temperature, max_tokens):
    openai.api_key = api_key
    llm = ChatOpenAI(model=engine)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({"question": question})
    return answer
    
## Title of the App
st.title("Simple Q&A Chatbot With OPENAI")

## Sidebar Settings
st.sidebar.header("Settings")
api_key = st.sidebar.text_input("Enter your OpenAI API Key", value="", type="password")
### After entering API key, select OpenAI model/ engine
engine = st.sidebar.selectbox("Select OpenAI Engine", ["gpt-3.5-turbo", 
                                                       "gpt-4", 
                                                       "gpt-4o",
                                                       "gpt-4-turbo"])

## Adjust response parameter
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7, step=0.1)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

## Main interface for user input
st.write("Go ahead and ask any question!")
user_input=st.text_input("You:")

if user_input and api_key:
    response=generate_response(user_input,api_key,engine,temperature,max_tokens)
    st.write(response)

elif user_input:
    st.warning("Please enter the OpenAI API Key in the side bar")
else:
    st.write("Please provide the user input")