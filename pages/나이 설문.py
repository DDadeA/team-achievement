import streamlit as st

import streamlit as st

def set_background(color):
  style = f"""
    <style>
      div.stApp {{
        background-color: {color};
      }}
    </style>
  """
  st.markdown(style, unsafe_allow_html=True)

set_background("#228B22")  

with st.container():
   st.markdown("# :violet[당신의 나이는?]")

st.number_input("당신의 나이를 입력하세요",value=None, placeholder="나이를 입력하세요...")
next_button = st.button("다음 페이지")

def go_to_운동종목설문():
    st.switch_page("pages/운동종목 설문.py")
if next_button:
    go_to_운동종목설문()