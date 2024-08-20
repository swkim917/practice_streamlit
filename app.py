import streamlit as st

# text input
string = st.text_input(
    '영화 제목', placeholder='좋아하는 영화 제목을 작성하세요'
)

if string:
    st.text('좋아하는 영화는 '+string)
