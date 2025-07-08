from langchain_community.chat_models import ChatOllama
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatOllama(model = 'llama3',
             base_url= 'http://127.0.0.1:11434'
             )

st.header('Research tool')

user_input = st.text_input('Enter your prompt')

if st.button('Summerize'):
    result = model.invoke(user_input)
    st.write(result.content)