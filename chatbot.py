import streamlit as st
import wikipedia
import speech_recognition as sr

# 🌙 DARK MODE STYLING
st.set_page_config(page_title="📘 Exam Helper Chatbot", layout="centered")
st.markdown("""
    <style>
        body { background-color: #0e1117; color: white; }
        .stTextInput input { background-color: #262730; color: white; }
        .stButton > button { background-color: #1f77b4; color: white; }
    </style>
""", unsafe_allow_html=True)

# 🧠 CHATBOT UI TITLE
st.title("📘 Exam Helper Chatbot 🤖")
st.markdown("Ask anything from your exam subjects. Get full answers from Wikipedia! 🌐")

# 💬 SESSION STORAGE FOR CHAT
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ✍️ TEXT INPUT
question = st.text_input("💬 Ask your question here:")

# 🎤 VOICE INPUT (optional, local use only)
if st.button("🎤 Use Voice"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎙️ Listening... Speak your question clearly.")
        try:
            audio = recognizer.listen(source, timeout=5)
            question = recognizer.recognize_google(audio)
            st.success(f"✅ You said: {question}")
        except:
            st.error("⚠️ Could not recognize your voice. Try again.")

# 🔍 SEARCH WIKIPEDIA
if st.button("🔍 Get Answer"):
    if question.strip() != "":
        try:
            summary = wikipedia.summary(question, sentences=5)  # Shorter summary
            st.session_state.chat_history.append((question, summary))
        except wikipedia.DisambiguationError as e:
            st.error("⚠️ Your question is too broad. Try being more specific.")
        except wikipedia.PageError:
            st.error("❌ Could not find any page. Try using different keywords.")
        except Exception as e:
            st.error(f"🚨 Unexpected error: {e}")

# 💬 DISPLAY CHAT HISTORY
st.markdown("---")
for q, a in st.session_state.chat_history:
    st.markdown(f"**🧑 You:** {q}")
    st.markdown(f"**🤖 Bot:** {a}")
