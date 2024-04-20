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

  st.markdown("# :red[안녕하세요, TA Health Care에 오신 것을 환영합니다!]")

skip_button = st.button("skip")
next_button = st.button("설문")


def go_to_성별설문():
    st.switch_page("pages/성별 설문.py")
if next_button:
    go_to_성별설문()

def go_to_매인화면():
    st.switch_page("pages/매인 화면.py")
if skip_button:
    go_to_매인화면()