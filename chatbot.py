import streamlit as st
from transformers import pipeline

# 🌙 Dark Mode Styling
st.set_page_config(page_title="📘 Exam Helper Chatbot", layout="centered")
st.markdown("""
    <style>
        body { background-color: #0e1117; color: white; }
        .stTextInput input { background-color: #262730; color: white; }
        .stButton > button { background-color: #1f77b4; color: white; }
    </style>
""", unsafe_allow_html=True)

# 🤖 Chatbot Title
st.title("📘 Exam Helper Chatbot 🤖")
st.markdown("Ask any subject question and get full detailed answers! 🚀")

# 🧠 Save full chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# 🔁 Load chatbot model only once
if "qa_model" not in st.session_state:
    with st.spinner("Loading AI model..."):
        st.session_state.qa_model = pipeline("text-generation", model="google/flan-t5-large")

# ✍️ User input
question = st.text_input("💬 Ask your question here:")

# 🔍 Get Answer button
if st.button("🔍 Get Answer"):
    if question:
        with st.spinner("Generating answer..."):
            response = st.session_state.qa_model(question, max_length=300, do_sample=True)
            answer = response[0]["generated_text"]
            st.session_state.chat_history.append((question, answer))

# 💬 Show full chat history
st.markdown("---")
for q, a in st.session_state.chat_history:
    st.markdown(f"**🧑 You:** {q}")
    st.markdown(f"**🤖 Bot:** {a}")
