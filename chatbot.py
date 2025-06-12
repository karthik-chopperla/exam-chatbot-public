import streamlit as st
import wikipedia

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

# 🔍 GET ANSWER
if st.button("🔍 Get Answer"):
    if question.strip():
        try:
            word_count = len(question.split())
            if word_count <= 5:
                answer = wikipedia.summary(question, sentences=2)
            elif word_count <= 10:
                answer = wikipedia.summary(question, sentences=4)
            else:
                answer = wikipedia.summary(question, sentences=7)
            st.session_state.chat_history.append((question, answer))
        except wikipedia.DisambiguationError:
            st.error("⚠️ Too many topics. Be more specific.")
        except wikipedia.PageError:
            st.error("❌ No Wikipedia page found. Try another keyword.")
        except Exception as e:
            st.error(f"🚨 Error: {e}")

# 💬 SHOW CHAT HISTORY WITH COPY BOX
st.markdown("---")
for i, (q, a) in enumerate(st.session_state.chat_history):
    st.markdown(f"**🧑 You:** {q}")
    st.markdown(f"**🤖 Bot:**")
    st.text_area(f"Answer {i+1}", value=a, height=150, key=f"ta_{i}")
    st.caption("📋 Select and copy manually (pyperclip disabled in cloud)")
