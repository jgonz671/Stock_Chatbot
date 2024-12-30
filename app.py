import streamlit as st
from pages.chatbot import chatbot_page
from pages.dashboard import dashboard_page

# Set page configuration to "wide" layout
st.set_page_config(
    page_title="Stock Analysis Chatbot",
    layout="wide",
    initial_sidebar_state="collapsed",  # Collapsed initially, but will be hidden
)

# Add custom CSS to hide the sidebar and its toggle control
st.markdown(
    """
    <style>
        [data-testid="stSidebar"] { 
            display: none;  /* Hides the entire sidebar */ 
        }
        [data-testid="collapsedControl"] { 
            display: none;  /* Hides the sidebar toggle control */ 
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Main page navigation
st.title("Stock Analysis Chatbot")
st.markdown("Use the navigation below to switch between the Dashboard and Chatbot.")

# Navigation bullet points on the main page
page = st.radio("Go to", ["Dashboard", "Chatbot"], horizontal=True)

# Route to the selected page
if page == "Dashboard":
    dashboard_page()
elif page == "Chatbot":
    chatbot_page()
