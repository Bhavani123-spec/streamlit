import os
os.environ["GOOGLE_API_KEY")=st.secrets["GOOGLE_API_KEY")
import streamlit as st
st.title("Streamlit Chatbot")
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# Initialize chat model
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Set up Streamlit UI
st.set_page_config(page_title="Gemini ChatBot", page_icon="🤖")
st.title("💬 Gemini ChatBot")
st.markdown("Ask anything. Type `quit` to end the chat.")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [SystemMessage(content="you are a helpful assistant.")]

# Display chat messages
for msg in st.session_state.chat_history:
    if isinstance(msg, HumanMessage):
        st.chat_message("user").markdown(msg.content)
    elif isinstance(msg, AIMessage):
        st.chat_message("assistant").markdown(msg.content)

# User input box
user_prompt = st.chat_input("Type your message...")

# Handle user input
if user_prompt:
    if user_prompt.strip().lower() == "quit":
        st.stop()

    st.session_state.chat_history.append(HumanMessage(content=user_prompt))
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # Get response from Gemini
    response = llm.invoke(st.session_state.chat_history)
    st.session_state.chat_history.append(AIMessage(content=response.content))

    with st.chat_message("assistant"):
        st.markdown(response.content)
