import streamlit as st
from PIL import Image 

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
    st.markdown("# :violet[오늘의 보상]") 
    st.markdown("# :violet[오늘 근력운동을 2시간 하였습니다. 오늘의 보상은 2000원어치의 음류수 쿠폰입니다.]")

쿠폰 = Image.open('pages/스타벅스 쿠폰.jpg')
st.image(쿠폰)

