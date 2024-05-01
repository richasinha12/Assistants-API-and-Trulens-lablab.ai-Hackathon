import streamlit as st
from clarifai.client.model import Model

st.set_page_config(
    page_title="GPT-CODER :)",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)


sidebar = st.sidebar
sidebar.title("Home")
sidebar.markdown("- Chatbot")
sidebar.markdown("- About us")


st.title("⭐GPT-CODER⭐")
# st.write("Enter your queries below:")
while(True):
    prompt = st.text_input("Enter your queries below:")
    if st.button('Submit'):
        model_url="https://clarifai.com/openai/chat-completion/models/gpt-4-turbo"
        model_prediction = Model(url=model_url,pat="de242f3fc61f4e5b9388c9dc7fe7b0a9").predict_by_bytes(prompt.title().encode(), input_type="text")  
        st.success(model_prediction.outputs[0].data.text.raw)




