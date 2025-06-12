import streamlit as st
import wikipedia

# 🎨 Dark Mode Styling
st.set_page_config(page_title="📘 Exam Helper Chatbot", layout="centered")
st.markdown(
    """
    <style>
        body { background-color: #0e1117; color: white; }
        .stTextInput > div > div > input { background-color: #262730; color: white; }
        .stButton > button { background-color: #1f77b4; color: white; }
    </style>
    """,
    unsafe_allow_html=True
)

# 🤖 Chatbot Header
st.title("📘 Exam Helper Chatbot 🤖")
st.markdown("Ask anything from your syllabus and get detailed answers using Wikipedia! 🌐")

# ⏳ Chat memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# 📝 Text input only (no voice)
question = st.text_input("💬 Ask your question here:")

# 🔍 Answer using Wikipedia
if st.button("🔍 Get Answer"):
    if question:
        try:
            answer = wikipedia.summary(question, sentences=8)  # Increased to 8 sentences for longer answers
            st.session_state.chat_history.append((question, answer))
        except Exception as e:
            st.session_state.chat_history.append((question, "⚠️ Couldn't find a full answer. Try rephrasing your question."))

# 💬 Show full chat
st.markdown("---")
for q, a in st.session_state.chat_history:
    st.markdown(f"**🧑 You:** {q}")
    st.markdown(f"**🤖 Bot:** {a}")
