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
    st.write(f":grey[ - 환영합니다, {user_name} 님]")
    st.write(f":grey[ - 당신은 만 {selected_age}세인 {selected_gender}입니다.]")
    st.write(f":grey[ - 오늘의 비만도는 {selected_BMI}입니다.]")
    st.write(f":grey[ - 오늘 당신은 {selected_exercise}를 했습니다.]")
st.write("오늘의 추천 운동:")

class DNN(nn.Module):
    
    def __init__(self):
        super(DNN, self).__init__()
        
        self.fc1 = nn.Linear(3, 40)
        self.activation = nn.LeakyReLU()
        self.fc2 = nn.Linear(40, 10)
        self.softmax = nn.Softmax(dim=0)

    def forward(self, x):
        x = self.fc1(x)
        x = self.activation(x)
        x = self.fc2(x)
        x = self.softmax(x)
        return x

model = torch.load("model.pt")
model.eval()
model.to("cpu")


if 'exercise' in st.session_state:
    selected_exercise = st.session_state['exercise']
  
def weight_mapping(weight_text):
    if weight_text == "저체중":
        return -2.5
    elif weight_text == "정상":
        return 0
    elif weight_text == "비만전단계비만":
        return 1
    elif weight_text == "1단계비만":
        return 2
    elif weight_text == "2단계비만":
        return 3
    elif weight_text == "3단계비만":
        return 4
      
def sex_mapping(sex):
    if sex == "여자":
        return -1
    if sex == "남자":
        return 1

user_data = torch.tensor([
            sex_mapping(selected_gender),
            int(selected_age),
            weight_mapping(selected_BMI)]).float()  


recommend_tensor = model(user_data).argmax().item()

def one_hot_decoder(result):
    if result == 1:
        return "실내 자전거타기"
    
    if result == 2:
        return "달리기"
    
    if result == 3:
        return "다리 벌려 앞으로 상체 숙이기"
    
    if result == 4:
        return "앉았다 일어서기"
    
    if result == 5:
        return "버피운동"
    
    if result == 6:
        return "몸통 비틀기"
    
    if result == 7:
        return "다리 벌려 옆으로 상체 숙이기"
    
    if result == 8:
        return "발목 얹고 다리 잡아당기기"
    
    if result == 9:
        return "엎드려 양팔 및 다리 들어올리기"
    
    if result == 10:
        return "몸통 들어올리기"
    
recommend = f"{one_hot_decoder(recommend_tensor) }"

st.markdown(f"### {recommend}")

prize_button = st.button("운동완료! 보상받기")

def go_to_reward():
    st.switch_page("pages/보상.py")
    
if prize_button:
    go_to_reward()