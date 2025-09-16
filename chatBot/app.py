from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

## Prompt template 
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "you are helpful assistant, please respond to user queries"),
        ("user", "Question: {question}")
    ]
)

## Streamlit framework 
st.title('Langchain demo with OpenAI API')
input_text = st.text_input("Search the topic you want")

# OpenAI LLM 
llm = ChatOpenAI(model="gpt-3.5-turbo")

if input_text:
    prompt_message = prompt.format_prompt(question=input_text)
    chain_output = llm(prompt_message.to_messages())
    st.write(chain_output.content)