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

# 🎤 Voice input (store separately)
voice_input = ""

if st.button("🎤 Use Voice"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎙️ Listening... Please speak.")
        try:
            audio = recognizer.listen(source, timeout=5)
            voice_input = recognizer.recognize_google(audio)
            st.success(f"✅ You said: {voice_input}")
        except:
            st.error("⚠️ Could not understand your voice. Try again.")

# ✍️ Text input
text_input = st.text_input("💬 Ask your question here:")

# Decide final question
final_question = voice_input if voice_input else text_input

# 🔍 Get Answer
if st.button("🔍 Get Answer"):
    if final_question:
        try:
            # ✅ Get the best matching title
            search_results = wikipedia.search(final_question)
            if search_results:
                summary = wikipedia.summary(search_results[0], sentences=5)
                st.session_state.chat_history.append((final_question, summary))
            else:
                st.error("⚠️ No results found. Try rephrasing your question.")
        except wikipedia.DisambiguationError as e:
            st.error(f"⚠️ Too many results. Try being specific. Options: {e.options[:5]}")
        except Exception as e:
            st.error(f"⚠️ An error occurred: {e}")

# 💬 Show chat history
st.markdown("---")
for q, a in st.session_state.chat_history:
    st.markdown(f"**🧑 You:** {q}")
    st.markdown(f"**🤖 Bot:** {a}")
