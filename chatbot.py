import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="📘 Exam Helper Chatbot", layout="centered")

st.title("📘 Exam Helper Chatbot")
st.markdown("Ask any question related to your exam topics! I’ll try my best to answer it.")

@st.cache_resource
def load_qa():
    return pipeline("question-answering")

qa = load_qa()

context = """
Design Thinking is a human-centered approach to solving problems creatively. 
It includes stages like Empathize, Define, Ideate, Prototype, and Test.
"""

# Continuous chat
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

question = st.text_input("💬 Ask your question here:")

if st.button("🔍 Get Answer") and question:
    result = qa(question=question, context=context)
    st.session_state.chat_history.append((question, result["answer"]))
    st.experimental_rerun()

for q, a in st.session_state.chat_history:
    st.markdown(f"**You:** {q}")
    st.markdown(f"**AI:** {a}")
