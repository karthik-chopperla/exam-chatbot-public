import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="📘 Exam Helper Chatbot", layout="centered")

st.title("📘 Exam Helper Chatbot")
st.markdown("Ask me anything from your subject! 💡")

@st.cache_resource
def load_qa():
    return pipeline("question-answering")

qa = load_qa()

# Sample context (can be replaced with real or dynamic data)
context = """
Design Thinking is a human-centered approach to solving problems creatively.
It includes stages like Empathize, Define, Ideate, Prototype, and Test.
"""

# Store previous chat messages
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Show previous chat
for q, a in st.session_state.chat_history:
    st.markdown(f"**🧑 You:** {q}")
    st.markdown(f"**🤖 Bot:** {a}")

# New question input
question = st.text_input("💬 Ask your next question here:")

if question:
    result = qa(question=question, context=context)
    st.session_state.chat_history.append((question, result["answer"]))
    st.experimental_set_query_params()  # small hack to trigger rerender
    st.experimental_rerun()  # safe rerun for this use case
