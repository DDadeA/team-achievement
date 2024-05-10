import streamlit as st
import torch
import torch.nn as nn

style = """
  <style>
    div.stApp {
      background: linear-gradient(129deg, rgba(79,207,100,1) 29%, rgba(89,136,144,1) 87%, rgba(97,90,163,1) 100%);
    }

    div.stButton > button {
      &:hover {
        border: 1px solid #afa !important;
      }
    }
    div.stButton > button[kind="secondary"] {
      background-color: white !important;
      color: #555 !important;
      border-radius: 16px !important;
    }
    div.stButton > button[kind="primary"] {
      background-color: #444 !important;
      color: white !important;
      border-radius: 16px !important;
      border: 1px solid #444 !important;
    }
  </style>
"""
st.markdown(style, unsafe_allow_html=True)

with st.container():    
    st.markdown("# :violet[오늘의 추천:]")
    if 'name' in st.session_state:
        user_name = st.session_state['name']
    if 'age' in st.session_state:
        selected_age = st.session_state['age']
    if 'gender' in st.session_state:
        selected_gender = st.session_state['gender']
    if 'BMI' in st.session_state:
        selected_BMI = st.session_state['BMI']
    if 'exercise' in st.session_state:
        selected_exercise = st.session_state['exercise']
    st.write(f"# :grey[환영합니다, {user_name} 님]")
    st.write(f"# :grey[당신은 만 {selected_age}세인 {selected_gender}입니다.]")
    st.write(f"# :grey[오늘의 비만도는 {selected_BMI}입니다.]")
    st.write(f"# :grey[오늘 당신은 {selected_exercise}를 했습니다.]")
st.write("오늘의 추천 운동:")
class DNN(nn.Module):
    model = DNN()
model.load_state_dict(torch.load('model.pth'))
model.eval()


if 'exercise' in st.session_state:
    selected_exercise = st.session_state['exercise']
user_data = torch.tensor([1, 30, 0]).float()  


recommend_tensor = model(user_data).argmax().item()
recommend = f"운동{recommend_tensor}"

st.write(f"{recommend}")

prize_button = st.button("보상")

def go_to_reward():
    st.switch_page("pages/reward.py")
    
if prize_button:
    go_to_reward()