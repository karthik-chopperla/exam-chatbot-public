import streamlit as st
import wikipedia
import speech_recognition as sr
from googletrans import Translator
from fpdf import FPDF
import pyttsx3
import base64

# 🎨 Dark Mode Setup
st.set_page_config(page_title="📘 Exam Helper Chatbot", layout="centered")
st.markdown("""
    <style>
        body { background-color: #0e1117; color: white; }
        .stTextInput > div > div > input { background-color: #262730; color: white; }
        .stButton > button { background-color: #1f77b4; color: white; }
    </style>
    """, unsafe_allow_html=True)

# 🤖 Title
st.title("📘 Exam Helper Chatbot 🤖")
st.markdown("Ask anything from your subjects and get detailed answers! 💡")

# 🌐 Translator
translator = Translator()

# 🔊 Text-to-Speech Setup (works on laptop)
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speech speed

# 🧠 Chat memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ✍️ Text input
question = st.text_input("💬 Ask your question here:")

# 🎤 Voice Input
if st.button("🎤 Use Voice"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎙️ Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            question = recognizer.recognize_google(audio)
            st.success(f"✅ You said: {question}")
        except:
            st.error("⚠️ Could not understand voice. Try again.")

# 🌍 Translate language
lang = st.selectbox("🌐 Translate Answer To:", ["None", "Hindi", "Telugu"])

# 🔍 Get Answer
if st.button("🔍 Get Answer"):
    if question:
        try:
            answer = wikipedia.summary(question, sentences=5)
            if lang != "None":
                translated = translator.translate(answer, dest='hi' if lang == "Hindi" else 'te')
                answer = translated.text
            st.session_state.chat_history.append((question, answer))
            st.markdown(f"**🤖 Bot:** {answer}")

            # 🔊 Speak answer aloud (on your laptop)
            engine.say(answer)
            engine.runAndWait()

        except:
            st.error("⚠️ Couldn't find a good answer. Try rephrasing.")
            st.session_state.chat_history.append((question, "⚠️ Couldn't find a good answer."))

# 💬 Chat history
st.markdown("---")
for q, a in st.session_state.chat_history:
    st.markdown(f"**🧑 You:** {q}")
    st.markdown(f"**🤖 Bot:** {a}")

# 📄 Save as PDF
def save_as_pdf(history):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for q, a in history:
        pdf.multi_cell(0, 10, f"You: {q}\nBot: {a}\n\n")
    return pdf

if st.button("📄 Download Chat as PDF"):
    pdf = save_as_pdf(st.session_state.chat_history)
    pdf.output("chat_history.pdf")
    with open("chat_history.pdf", "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="chat_history.pdf">📥 Click here to download your PDF</a>'
        st.markdown(href, unsafe_allow_html=True)
