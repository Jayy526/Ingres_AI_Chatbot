import streamlit as st
import requests


st.title("INGRES AI Chatbot 💧")


question = st.text_input("Ask about groundwater:")
if st.button("Ask"):
    resp = requests.post("http://127.0.0.1:8000/ask", json={"question": question})
    st.write(resp.json()["answer"])