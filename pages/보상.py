import streamlit as st
from PIL import Image 

st.title("오늘의 보상")
st.write ("오늘 근력운동을 2시간 하였습니다. 오늘의 보상은 2000원어치의 음류수 쿠폰입니다.")

쿠폰 = Image.open('pages/스타벅스 쿠폰.jpg')
st.image(쿠폰)

