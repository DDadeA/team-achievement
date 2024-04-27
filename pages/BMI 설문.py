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
    st.markdown("# :violet[당신의 비만도는?]")

st.selectbox("비만도", ["저체중", "정상", "1단계 비만","2단계 비만", "3단계 비만" ])
next_button = st.button("다음 페이지")

def go_to_매인화면():
    st.switch_page("pages/매인 화면.py")
if next_button:
    go_to_매인화면()