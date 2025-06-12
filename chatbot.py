import streamlit as st
import wikipedia
import pyperclip  # For copy button

# 🌙 DARK MODE STYLING
st.set_page_config(page_title="📘 Exam Helper Chatbot", layout="centered")
st.markdown("""
    <style>
        body { background-color: #0e1117; color: white; }
        .stTextInput input { background-color: #262730; color: white; }
        .stButton > button { background-color: #1f77b4; color: white; }
    </style>
""", unsafe_allow_html=True)

# 🧠 TITLE & INTRO
st.title("📘 Exam Helper Chatbot 🤖")
st.markdown("Ask any exam-related question. Get detailed, smart answers from Wikipedia based on your question depth! 🚀")

# 💬 SESSION STATE
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ✍️ TEXT INPUT
question = st.text_input("💬 Ask your question here:")

# 🔍 WIKIPEDIA SEARCH
if st.button("🔍 Get Answer"):
    if question.strip():
        try:
            # Adjust answer length based on question size
            words = len(question.split())
            if words <= 5:
                answer = wikipedia.summary(question, sentences=2)
            elif words <= 10:
                answer = wikipedia.summary(question, sentences=4)
            else:
                answer = wikipedia.summary(question, sentences=7)
            st.session_state.chat_history.append((question, answer))
        except wikipedia.DisambiguationError:
            st.error("⚠️ Too many possible topics. Try being more specific.")
        except wikipedia.PageError:
            st.error("❌ Couldn't find a Wikipedia page for this question.")
        except Exception as e:
            st.error(f"🚨 Error: {e}")

# 💬 SHOW HISTORY WITH COPY BUTTON
st.markdown("---")
for i, (q, a) in enumerate(st.session_state.chat_history):
    st.markdown(f"**🧑 You:** {q}")
    st.markdown(f"**🤖 Bot:** {a}")
    if st.button(f"📋 Copy Answer {i+1}", key=f"copy_{i}"):
        pyperclip.copy(a)
        st.success("✅ Answer copied to clipboard!")
