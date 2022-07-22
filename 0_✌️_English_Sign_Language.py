import streamlit as st
import pandas as pd
import numpy as np
from html_module import line_break, section, callout, title
from PIL import Image

# 전체 페이지 설정
st.set_page_config(
    page_title="English Sign Language",
    page_icon="🤘",  # 아이콘
    initial_sidebar_state="expanded", 
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.balloons()  # 풍선 효과
title('English Sign Language CNN Project')

# 개요 section
section('Summary')
image = Image.open('images/sign_language.jpg')
st.image(image,)
callout([
  '안녕하세요! ✌ Sign팀입니다. 🙂',
  'Kaggle의 English Sign Language 데이터를 이용하여 CNN Project를 진행하였습니다.',
  'OpenCV의 Real Time으로 실시간으로 알파벳 수화를 예측할 수 있도록 만들었습니다.'
])
line_break()

# 데이터 출처 section
section('Dataset')
link = 'https://www.kaggle.com/datasets/datamunge/sign-language-mnist'
st.markdown(link, unsafe_allow_html=True)
st.caption('데이터 출처 사이트로 이동하기')
line_break()

# Sign Team Notion section
section('Notion')
link = 'https://www.notion.so/likelion-aischool/English-Sign-Language-759acc98547a4e259367a63625ba2158'
st.markdown(link, unsafe_allow_html=True)
st.caption('팀 노션 페이지로 이동하기')
line_break()
