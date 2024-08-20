import streamlit as st

# text input
string = st.text_input(
    'Movie title', placeholder='write down the title of your favorite movie'
)

if string:
    st.text('Your answer is '+string)