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
    st.markdown("# :violet[당신의 성별은?]")

st.selectbox("성별", ["남자", "여자"])
next_button = st.button("다음 페이지")

def go_to_나이설문():
    st.switch_page("pages/나이 설문.py")

if next_button:
    go_to_나이설문()