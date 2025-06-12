import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="📘 Exam Helper Chatbot", layout="centered")

st.title("📘 Exam Helper Chatbot 🤖")
st.markdown("Ask anything related to your subjects and get instant answers! 💡")

@st.cache_resource
def load_model():
    return pipeline("question-answering")

qa = load_model()

# Sample context (replace this later with Wikipedia or live search)
context = """
Design Thinking is a human-centered approach to solving problems creatively.
It includes stages like Empathize, Define, Ideate, Prototype, and Test.
"""

# Store chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Ask user for question
question = st.text_input("💬 Ask your question here:")

# Submit
if st.button("🔍 Get Answer"):
    if question:
        result = qa(question=question, context=context)
        st.session_state.chat_history.append((question, result["answer"]))

# Show chat history
st.markdown("---")
for q, a in st.session_state.chat_history:
    st.markdown(f"**🧑 You:** {q}")
    st.markdown(f"**🤖 Bot:** {a}")
