from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

# load environment variables
load_dotenv()


# prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please response to the user's input message."),
        ("user", "Question: {question}")
    ]
)

# stremlit framewrok
st.title("Langchain Demo with OpenAI API")
input_text = st.text_input("Search the topic you want") 

# openai LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))


 



