import streamlit as st
from streamlit_chat import message

def chatbot_page():
    st.header("Chatbot Interface")
    st.write("Ask the chatbot about stock trends, ROI, and more!")

    # Initialize session state for messages and textbox
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "user_input" not in st.session_state:
        st.session_state.user_input = ""  # Initial empty state for the textbox

    # Text input for user query
    user_input = st.text_input("Ask the chatbot:", key="user_input", on_change=lambda: None)

    # Process user input when it changes
    if user_input:
        # Simple chatbot logic
        if "trend" in user_input.lower():
            response = "Please provide the stock symbol for trend analysis."
        elif "roi" in user_input.lower():
            response = "ROI calculation is coming soon!"
        else:
            response = "I'm still learning. Ask about stock trends or ROI."

        # Append messages to session state
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.session_state.messages.append({"role": "bot", "content": response})

        # Clear the input field
        st.session_state.user_input = ""

    # Display messages
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            message(msg["content"], is_user=True)
        else:
            message(msg["content"], is_user=False)
