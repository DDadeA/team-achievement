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
    st.markdown("# :violet[당신이 한 운동은?]")

st.selectbox("운동종목", ["유산소운동", "근력운동", "기타" ])
next_button = st.button("다음 페이지")

def go_to_시간설문():
    st.switch_page("pages/시간 설문.py")
if next_button:
    go_to_시간설문()