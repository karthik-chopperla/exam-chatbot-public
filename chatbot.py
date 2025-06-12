import streamlit as st
import wikipedia
import speech_recognition as sr

# 🌙 Dark Mode UI
st.set_page_config(page_title="📘 Exam Helper Chatbot", layout="centered", initial_sidebar_state="collapsed")
st.markdown("""
    <style>
        body { background-color: #0e1117; color: white; }
        .stTextInput input { background-color: #262730; color: white; }
        .stButton > button { background-color: #1f77b4; color: white; }
    </style>
""", unsafe_allow_html=True)

st.title("📘 Exam Helper Chatbot 🤖")
st.markdown("Ask any question from any subject. Get full answers from Wikipedia. 🌐")

# 🧠 Save chat
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ✍️ Text input
question = st.text_input("💬 Ask your question here:")

# 🎤 Voice input
if st.button("🎤 Use Voice"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎙️ Listening... Please speak.")
        try:
            audio = recognizer.listen(source, timeout=5)
            question = recognizer.recognize_google(audio)
            st.success(f"✅ You said: {question}")
        except:
            st.error("⚠️ Could not understand your voice. Please try again.")

# 🔍 Get Answer
if st.button("🔍 Get Answer"):
    if question:
        try:
            # 📄 Full Wikipedia page (not just summary)
            answer = wikipedia.page(question).content
            st.session_state.chat_history.append((question, answer[:1500]))  # Show first 1500 characters
        except:
            st.error("⚠️ No answer found. Try a different question.")

# 💬 Show chat history
st.markdown("---")
for q, a in st.session_state.chat_history:
    st.markdown(f"**🧑 You:** {q}")
    st.markdown(f"**🤖 Bot:** {a}")
