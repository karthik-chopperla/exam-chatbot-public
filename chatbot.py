import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Exam Helper Chatbot", layout="centered")

st.title("📘 Exam Helper Chatbot")
st.markdown("Ask me anything from your subject. I’ll try to answer it!")

# Load a small model
@st.cache_resource
def load_qa_pipeline():
    return pipeline("question-answering")

qa_pipeline = load_qa_pipeline()

# Sample fixed context (You can change this later to dynamic or from documents)
context = """
Design Thinking is a human-centered approach to solving problems creatively. 
It includes stages like Empathize, Define, Ideate, Prototype, and Test.
"""

question = st.text_input("💬 Your Question:")

if question:
    with st.spinner("Thinking..."):
        result = qa_pipeline(question=question, context=context)
        st.success("✅ " + result["answer"])
