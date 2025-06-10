
import streamlit as st
from langchain.schema import HumanMessage
from graph import build_graph, ChatState
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="LangGraph Multi-Agent Chatbot", page_icon="🤖")
st.title("🤖 LangGraph Multi-Agent Chatbot")

graph = build_graph()

if "chat_state" not in st.session_state:
    st.session_state.chat_state = ChatState()

user_input = st.text_input("Ask me anything:")

if user_input:
    st.session_state.chat_state.messages.append(HumanMessage(content=user_input))
    result = graph.invoke({"messages": st.session_state.chat_state.messages})
    for msg in result["messages"]:
        st.markdown(f"**🗨️ {msg.content}**")
