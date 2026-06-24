# Frontend User Interface File

import streamlit as st
import requests

st.title("💬 LLM Chatbot")

# Initialize chat history in session state if it doesn't exist yet
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Text input field to enter a message
user_input = st.text_input("You:", key="input")

# Submitting a message
if user_input:
    # Add user's message to chat history
    st.session_state.chat_history.append(("You", user_input))
    
    with st.spinner("Thinking..."):  # loading spinner
        try:
            print("here")
            print("User Input", user_input)
            # Send POST request to backend API with the user message
            res = requests.post("http://localhost:8000/chat", json={"message": user_input})
            

            if res.status_code == 200:
                data = res.json()

                # Check if the expected keys exist in the response
                if "response" in data:
                    st.session_state.chat_history.append(("Bot", data["response"]))
                    #st.markdown(f"🕒 Time: {data.get('execution_time', 'N/A')}s | 🔢 Tokens: {data.get('tokens', 'N/A')}")
                else:
                    # If 'response' is missing, show the error key (if present)
                    error_msg = data.get("error", "Unexpected response from server.")
                    st.session_state.chat_history.append(("Bot", f"Error: {error_msg}"))

            else:
                # Non-200 HTTP response
                st.session_state.chat_history.append(("Bot", f"Server error {res.status_code}"))

        except Exception as e:
            # Catch connection errors or other exceptions
            st.session_state.chat_history.append(("Bot", f"Exception: {str(e)}"))

# Display the conversation history in order
for speaker, msg in st.session_state.chat_history:
    st.markdown(f"**{speaker}**: {msg}")