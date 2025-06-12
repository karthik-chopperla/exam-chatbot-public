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

# 🧠 Chat memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ✍️ User input
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
            st.error("⚠️ Could not understand your voice. Try again.")

# 🔍 Get Answer
if st.button("🔍 Get Answer"):
    if question:
        try:
            # ✅ Step 1: Search related titles
            search_results = wikipedia.search(question)
            if search_results:
                # ✅ Step 2: Load first match
                page = wikipedia.page(search_results[0])
                answer = page.content[:1500]  # Limit answer length
                st.session_state.chat_history.append((question, answer))
            else:
                st.error("⚠️ Sorry, I couldn't find anything related to your question.")
        except wikipedia.DisambiguationError as e:
            st.error(f"⚠️ Your question is too broad. Try being more specific. Options: {e.options[:5]}")
        except Exception as e:
            st.error("⚠️ An error occurred. Try again.")

# 💬 Display chat history
st.markdown("---")
for q, a in st.session_state.chat_history:
    st.markdown(f"**🧑 You:** {q}")
    st.markdown(f"**🤖 Bot:** {a}")
