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

# 🧠 CHATBOT UI TITLE
st.title("📘 Exam Helper Chatbot 🤖")
st.markdown("Ask anything from your exam subjects. Get full answers from Wikipedia! 🌐")

# 🧠 SAVE CHAT HISTORY
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ✍️ TEXT INPUT
question = st.text_input("💬 Ask your question here:")

# 🔍 SEARCH ANSWER
if st.button("🔍 Get Answer"):
    if question:
        try:
            # 📄 GET FULL WIKIPEDIA PAGE CONTENT (up to 1500 characters)
            page = wikipedia.page(question)
            answer = page.content[:1500] + "..."
            st.session_state.chat_history.append((question, answer))
        except Exception as e:
            st.error("⚠️ Couldn't find a full answer. Try rephrasing your question.")

# 💬 DISPLAY CHAT HISTORY
st.markdown("---")
for q, a in st.session_state.chat_history:
    st.markdown(f"**🧑 You:** {q}")
    st.markdown(f"**🤖 Bot:** {a}")
