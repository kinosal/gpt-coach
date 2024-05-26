"""Streamlit app to generate Tweets."""

# Import from standard library

# Import from 3rd party libraries
import streamlit as st

# Import modules
import oai


# Define functions
def assistant(message_history: list, latest_message: str):
    """Generate next assistant message."""
    openai = oai.CoachGPT()
    messages = [
        *message_history,
        {
            "role": "user",
            "content": latest_message
        }
    ]
    return openai.create_completion(messages)


# Configure Streamlit page and state
st.set_page_config(page_title="CoachGPT", page_icon="🤖")

if "latest_message" not in st.session_state:
    st.session_state.latest_message = ""
if "message_history" not in st.session_state:
    st.session_state.message_history = []

# Render Streamlit page
st.title("Create your personal development plan with your AI coach")
st.markdown(
    "This mini-app uses OpenAI's [GPTs](https://platform.openai.com/docs/models/overview) to help you create your individual personal development plan."
)
with st.chat_message("assistant"):
    st.write(
        "Hi, I am Sky, your personal development coach. Today, I'd like to create your personal development plan together with you. Are you ready?"
    )

for message in st.session_state.message_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if message := st.chat_input():
    st.chat_message("user").markdown(message)
    st.session_state.latest_message = message
    st.session_state.message_history.append(
        {
            "role": "user",
            "content": message
        }
    )
    completion = assistant(st.session_state.message_history, st.session_state.latest_message)
    with st.chat_message("assistant"):
        st.markdown(completion)
    st.session_state.message_history.append(
        {
            "role": "assistant",
            "content": completion
        }
    )


