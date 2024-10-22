import streamlit as st
import numpy as np
from PIL import Image
import pickle
from datetime import datetime


# # 모델 파일 로드 (pickle 사용)
# model_path = 'models/iris_model_svc.pkl'
# with open(model_path, 'rb') as file:
#     model = pickle.load(file)

# 김치 데이터셋의 결과 이름
gimchi_result_names = ['김장 하기', '포장 김치 구매하기']

# 페이지 제목과 파비콘 설정
st.set_page_config(
    page_title="살래? 말래?",  # 탭에 표시될 제목
    page_icon="🥬"  # 탭에 표시될 파비콘 (이모지 또는 이미지 URL 가능)
)

# CSS로 구분선 및 텍스트 중앙 정렬 스타일 추가
st.markdown("""
    <style>
    .divider {
        border-top: 1px solid #d3d3d3; /* 회색 구분선 */
        margin: 20px 0;
    }
    .center-text {
        text-align: center; /* 텍스트 중앙 정렬 */
        font-size: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# CSS로 제목에 배경 색상 추가
st.markdown("""
    <style> 
    .title {
        font-size: 40px;
        font-weight: bold;
        background-color: #ffcdd2;
        padding: 10px;
        border-radius: 5px;
        color: black;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# 제목과 스타일 적용
st.markdown('<div class="title">🥬살래? 말래?🥬</div>', unsafe_allow_html=True)

# 페이지 추가
st.sidebar.success("select a page above")

# 일반 텍스트 (중앙 정렬 적용)
st.markdown('<div class="center-text">-김장을 할지! 포장 김치를 구매할지! 헷갈리시는 분들을 위한 서비스-</div>', unsafe_allow_html=True)

# 첫 번째 구분선
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# 재료 선택 (복수 선택 가능, '배추'는 기본 선택)
ingredients = st.multiselect(
    '1. 원하는 재료를 선택하세요:',
    ['양파', '마늘', '건고추', '배추', '고춧가루', '생강'],
    default=['배추']  # '배추'를 기본값으로 설정
)

# 두 번째 구분선
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# 김장 재료 구매 날짜 선택 (오늘 이전 날짜는 선택 불가)
purchase_date = st.date_input(
    "재료를 구매할 날짜를 선택하세요:",
    min_value=datetime.now().date(),  # 최소 날짜를 오늘로 설정
    value=datetime.now().date()  # 기본값을 오늘 날짜로 설정
)

# 세 번째 구분선
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# 총 구매할 김치 무게 선택 (슬라이드바)
kimchi_weight = st.slider(
     '구매할 김치 무게를 선택하세요 (kg):',
     1.0, 20.0, 1.0, 1.0,  # 최소, 최대, 기본값, 단계
     format="%f kg"  # 슬라이더 값 표시 형식
)

# 실시간으로 입력한 값 표시
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.write("**입력된 정보**:")
st.write(f"- 선택한 재료: {', '.join(ingredients) if ingredients else '재료를 선택하지 않았습니다.'}")
st.write(f"- 구매 날짜: {purchase_date.strftime('%Y-%m-%d')}")
st.write(f"- 김장할 김치 무게: {kimchi_weight:.1f} kg")

# 네 번째 구분선
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# '비교하기' 버튼을 클릭했을 때 필수 항목 확인
if st.button('비교하기'):
    if not ingredients:
        st.error("재료를 선택해야 합니다!")
    else:
        st.success("김장 하기와 포장 김치 구매하기를 비교하는 중입니다!")


# st.experimental_set_query_params 이거 안됨
# 페이지 변환 하고 싶은데 뭘 해도 안된다....
