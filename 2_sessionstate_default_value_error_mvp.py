import streamlit as st

import SessionState

st.markdown(
    "## Instructions\n"
    + "1. Type '2' into text input.\n"
    + "2. Press Enter.\n"
    + "3. Text changes as expected.\n"
    + "4. Type '3' into text input.\n"
    + "5. Press Enter.\n"
    + "6. Text instantly goes back to '2'.\n"
)

session = SessionState.get(text="1")
session.text = st.text_input("Text", session.text)
st.write(session.text)
