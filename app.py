import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="Ehsaas 🤍", page_icon="💬", layout="centered")

st.title("Ehsaas 🤍 - Your Buddy")

# --- Initialize multiple chat sessions ---
if "chats" not in st.session_state:
    st.session_state.chats = []  # list of chat histories
if "current_chat" not in st.session_state:
    st.session_state.current_chat = []  # active chat messages
if "active_chat_index" not in st.session_state:
    st.session_state.active_chat_index = None  # track selected chat

# --- Function to send message ---
def send_message():
    user_msg = st.session_state.chat_input.strip()
    if not user_msg:
        return

    # Add user message
    st.session_state.current_chat.append({"role": "user", "content": user_msg})

    # Call backend
    response = requests.post(
        "http://localhost:8000/chat",
        json={"message": user_msg}
    )
    bot_reply = response.json()["response"]

    # Add bot reply
    st.session_state.current_chat.append({"role": "bot", "content": bot_reply})

    # Clear input
    st.session_state.chat_input = ""

# --- Function to start new chat ---
def new_chat():
    if st.session_state.current_chat:  # only save if not empty
        st.session_state.chats.append({
            "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "messages": st.session_state.current_chat
        })
    st.session_state.current_chat = []
    st.session_state.active_chat_index = None

# --- Function to load old chat ---
def load_chat(index):
    st.session_state.current_chat = st.session_state.chats[index]["messages"].copy()
    st.session_state.active_chat_index = index

# --- Sidebar for chat sessions ---
with st.sidebar:
    st.header("💭 Conversations")
    if st.button("➕ New Chat"):
        new_chat()

    if st.session_state.chats:
        for i, chat in enumerate(st.session_state.chats):
            if st.button(f"Chat {i+1} ({chat['time']})"):
                load_chat(i)

# --- Chat history display with pastel bubbles (dark text) ---
for msg in st.session_state.current_chat:
    if msg["role"] == "user":
        st.markdown(
            f"""
            <div style='background-color:#D1E7DD;
                        padding:10px;border-radius:15px;
                        margin:5px 0;text-align:left;
                        color:#222;font-weight:500;'>
                🙋 {msg['content']}
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"""
            <div style='background-color:#F8D7DA;
                        padding:10px;border-radius:15px;
                        margin:5px 0;text-align:left;
                        color:#222;font-weight:500;'>
                🫶 {msg['content']}
            </div>
            """,
            unsafe_allow_html=True,
        )

# --- Input box ---
st.chat_input("Type your message...", key="chat_input", on_submit=send_message)