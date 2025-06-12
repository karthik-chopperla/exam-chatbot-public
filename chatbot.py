import streamlit as st
import wikipedia
from transformers import pipeline
import speech_recognition as sr

# 🎨 Dark mode styling
st.set_page_config(page_title="📘 Exam Helper Chatbot", layout="centered", initial_sidebar_state="collapsed")
st.markdown(
    """
    <style>
        body {
            background-color: #0e1117;
            color: white;
        }
        .stTextInput > div > div > input {
            background-color: #262730;
            color: white;
        }
        .stButton > button {
            background-color: #1f77b4;
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("📘 Exam Helper Chatbot 🤖")
st.markdown("Ask any question from your subject and get answers using Wikipedia search! 🌐")

@st.cache_resource
def load_model():
    return pipeline("question-answering")

qa = load_model()

# 🧠 Chat history memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ✍️ Text input
question = st.text_input("💬 Ask your question here:")

# 🎤 Voice input (works only on desktop, not Streamlit Cloud)
if st.button("🎤 Use Voice"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎙️ Listening... Please speak your question.")
        try:
            audio = recognizer.listen(source, timeout=5)
            question = recognizer.recognize_google(audio)
            st.success(f"✅ You said: {question}")
        except:
            st.error("⚠️ Could not understand your voice. Please try again.")

# 🔍 Answer button
if st.button("🔍 Get Answer"):
    if question:
        try:
            # 🔎 Search Wikipedia
            context = wikipedia.summary(question, sentences=5)
            result = qa(question=question, context=context)
            st.session_state.chat_history.append((question, result["answer"]))
        except:
            st.error("⚠️ Sorry, no good answer found. Try asking in a simpler way.")

# 💬 Display chat history
st.markdown("---")
for q, a in st.session_state.chat_history:
    st.markdown(f"**🧑 You:** {q}")
    st.markdown(f"**🤖 Bot:** {a}")
