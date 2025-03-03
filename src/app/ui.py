import streamlit as st
from langserve import RemoteRunnable
from langchain_core.messages import HumanMessage

# import os
# from dotenv import load_dotenv
# load_dotenv()

bot = RemoteRunnable("http://localhost:8080/")

if 'message_history' not in st.session_state:
    st.session_state.message_history = []

def call_api(input: str) -> dict:
    return bot.invoke({
        "messages": st.session_state.message_history + [HumanMessage(input)],
    })

user_prompt=st.chat_input()

if user_prompt is not None and user_prompt.strip() != "":
    response = call_api(user_prompt)
    new_messages = []
    for msg in response["messages"]:
        if  msg.type in ("human", "system") or (msg.type == "ai" and not msg.tool_calls):
            new_messages.append(msg)
    st.session_state.message_history = new_messages

for msg in st.session_state.message_history:
    with st.chat_message(msg.type, avatar=msg.type):
        st.write(msg.content)
