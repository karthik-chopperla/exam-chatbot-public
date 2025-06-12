import streamlit as st
import wikipedia

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

# 🎤 Disabled voice input (Streamlit Cloud does not support mic access)
if st.button("🎤 Use Voice"):
    st.warning("🎤 Voice input is only available in local apps. Not supported on Streamlit Cloud.")

# 🔍 Get Answer
if st.button("🔍 Get Answer") and question:
    try:
        results = wikipedia.search(question)
        if not results:
            st.error("⚠️ No results found. Try rephrasing your question.")
        else:
            top_result = results[0]
            answer = wikipedia.summary(top_result, sentences=7, auto_suggest=False, redirect=True)
            st.session_state.chat_history.append((question, answer))
    except wikipedia.DisambiguationError as e:
        options = ", ".join(e.options[:5])
        st.error(f"⚠️ Your question is too broad. Did you mean: {options}?")
    except wikipedia.PageError:
        st.error("⚠️ Could not find a page for that topic. Try another question.")
    except Exception as e:
        st.error(f"⚠️ An error occurred: {e}")

# 💬 Show chat history
st.markdown("---")
for q, a in st.session_state.chat_history:
    st.markdown(f"**🧑 You:** {q}")
    st.markdown(f"**🤖 Bot:** {a}")
