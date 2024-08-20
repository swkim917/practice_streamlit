import streamlit as st

# text input
a = st.text_input('첫번째 수', placeholder='첫번째 수를 입력하세요')
b = st.text_input('두번째 수', placeholder='두번째 수를 입력하세요')

a = int(a)
b = int(b)
st.text(str(a + b))
