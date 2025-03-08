# 🤖 Simple Q&A Chatbot with OpenAI & Groq 🚀

This repository contains two implementations of a simple Q&A chatbot using OpenAI and Groq models via LangChain and Streamlit.

## ✨ Features
- ✅ Supports both OpenAI and Groq models
- 🧠 Uses LangChain for structured prompt handling
- 🎨 Streamlit-based UI for easy interaction
- 🔒 API key validation for security
- ⚙️ Customizable model settings, temperature, and max tokens

## 📂 Files Overview
- `openai&groq-app.py` 📌: Supports both OpenAI and Groq models, allowing users to select the provider and engine.
- `openai-app.py` 📝: A simpler version that only supports OpenAI models.
- `.gitignore` 🚫: Ensures `.env` and `venv` are ignored for security.
- `requirements.txt` 📄: Lists dependencies for easy setup.
- `.env` 🔑: Stores API keys (not included in the repo for security reasons).

## 🔧 Installation

### Prerequisites
Ensure you have Python installed (preferably Python 3.8+). 🐍

### Steps
1. Clone this repository: 🛠️
   ```bash
   git clone https://github.com/AlbertChoo/GenAI_Projects.git
   cd your-repo-name
   ```
2. Create a virtual environment (optional but recommended): 🌱
   ```bash
   python -m venv venv # conda create -p venv python=3.10 y [I use this], conda activate venv/
   source venv/bin/activate  # On Windows use: venv\Scripts\activate 
   ```
3. Install dependencies: 📦
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the root directory and add your API keys: 🔑
   ```env
   OPENAI_API_KEY=your_openai_api_key
   GROQ_API_KEY=your_groq_api_key
   LANGCHAIN_API_KEY=your_langchain_api_key
   LANGCHAIN_PROJECT=your_project_name #Example: 'GenAIAppWIthOpenAI'
   ```

## 🚀 Usage

### Running OpenAI & Groq Chatbot
```bash
streamlit run openai&groq-app.py
```

### Running OpenAI-only Chatbot
```bash
streamlit run openai-app.py
```

## 🛠️ Customization
- Modify `ChatPromptTemplate` in `openai&groq-app.py` or `openai-app.py` to change the system prompt.
- Adjust temperature and max tokens via Streamlit UI for different response styles.

## ❓ Troubleshooting
- ❌ If API calls fail, ensure your API keys are correct and valid.
- 🛠️ If running on a new machine, ensure all dependencies are installed with `pip install -r requirements.txt`.

## 📜 License
MIT License ⚖️

