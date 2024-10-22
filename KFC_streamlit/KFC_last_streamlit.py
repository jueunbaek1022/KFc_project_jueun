import streamlit as st
import pandas as pd
from datetime import date
import matplotlib.pyplot as plt
import platform

if platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')
elif platform.system() == 'Darwin':  # macOS
    plt.rc('font', family='AppleGothic')
else:  # Linux
    plt.rc('font', family='NanumGothic')

# 마이너스 기호 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False

# 페이지 제목과 파비콘 설정 
st.set_page_config(
    page_title="살래? 말래?", layout="wide") # 탭에 표시될 제목

# 커스텀 CSS 추가
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: 700;
        color: #1E90FF;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        font-weight: 600;
        color: #4682B4;
        margin-bottom: 1rem;
    }
    .info-text {
        font-size: 1rem;
        color: #708090;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-header'>살래? 말래?</h1>", unsafe_allow_html=True)
st.markdown("""
    <style>
    .info-text {
        text-align: center;
        font-size: 18px;  /* 텍스트 크기 조정 */
        color: #333333;  /* 텍스트 색상 설정 */
    }
    </style>
    <p class='info-text'>김장철 농산물 가격 비교 서비스</p>
    """, unsafe_allow_html=True)
st.markdown("---")

# 사이드바 구성
with st.sidebar:
    st.markdown("<h2 class='sub-header'>입력 정보</h2>", unsafe_allow_html=True)
    
    ingredients = st.multiselect(
        "재료 선택",
        ["배추", "건고추", "깐마늘", "생강", "고춧가루", "쪽파"],
        default=["배추"]
    )
    
    purchase_date = st.date_input(
        "김장 예정일",
        min_value=date.today() # 최소 날짜를 오늘로 설정
    )
    
    # 각 재료에 대한 슬라이더 생성
    ingredient_weights = {}
    for ingredient in ingredients:
        if ingredient == "배추":
            ingredient_weights[ingredient] = st.slider(
                f"{ingredient} (포기)",
                min_value=0,
                max_value=50,
                value=1,
                step=1
            )
        else:
            ingredient_weights[ingredient] = st.slider(
                f"{ingredient} 무게 (kg)",
                min_value=0,
                max_value=50,
                value=1,
                step=1
            )
    
    compare_button = st.button("비교하기")

ingredient_prices = {
    "배추": 10000, "건고추": 1500, "깐마늘": 20000,
    "생강": 8000, "고춧가루": 2500, "쪽파": 25000
}

# 메인 페이지 구성
if compare_button:
    st.markdown("<h2 class='sub-header'>비교 결과</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<h3 class='sub-header'>1. 직접 담그기</h3>", unsafe_allow_html=True)
        
        estimated_cost = sum(ingredient_prices[ing] * weight for ing, weight in ingredient_weights.items())
        st.markdown(f"<div class='highlight'><h4>예상 비용: {estimated_cost:,.0f}원</h4></div>", unsafe_allow_html=True)
        
        # 선택된 재료별 가격 표시
        prices = [ingredient_prices[ing] for ing in ingredients]
        
        fig, ax = plt.subplots()
        ax.bar(ingredients, prices, color='skyblue')
        ax.set_ylabel('가격 (원)')
        ax.set_title('선택된 재료별 가격')
        
        for i, v in enumerate(prices):
            ax.text(i, v + 100, f"{v:,}원", ha='center', va='bottom')
        
        st.pyplot(fig)
        
        st.write(f"📅 김장 예정일: {purchase_date}")
    
    with col2:
        st.markdown("<h3 class='sub-header'>2. 포장 김치 구매</h3>", unsafe_allow_html=True)
        
        total_weight = sum(ingredient_weights.values())  # 총 김치 무게 계산
        
        df = pd.DataFrame([
            {"브랜드": "종가집", "제품명": "포기김치", "중량": f"{total_weight}kg", 
             "가격": f"{14970 * total_weight / 1:,.0f}원"},
            {"브랜드": "비비고", "제품명": "포기김치", "중량": f"{total_weight}kg", 
             "가격": f"{15900 * total_weight / 1:,.0f}원"},
            {"브랜드": "이마트 노브랜드", "제품명": "별미 포기김치", "중량": f"{total_weight}kg", 
             "가격": f"{19720 * total_weight / 3.5:,.0f}원"},
            {"브랜드": "늘만나김치", "제품명": "맛김치", "중량": f"{total_weight}kg", 
             "가격": f"{7000 * total_weight / 0.45:,.0f}원"}
        ])
        
        st.table(df)

        packaged_kimchi = [
            {"name": "종가집 포기김치", "url": "https://www.ssg.com/item/itemView.ssg?itemId=1000012927413"},
            {"name": "비비고 포기김치", "url": "https://www.cjthemarket.com/pc/prod/prodDetail?prdCd=40145356"},
            {"name": "이마트 노브랜드 별미 포기김치", "url": "https://emart.ssg.com/search.ssg?target=all&query=%ED%8F%AC%EA%B8%B0%EA%B9%80%EC%B9%98"},
            {"name": "늘만나김치 맛김치", "url": "https://www.mannakimchi.com"},
        ]
        
        st.markdown("<h4>추천 제품 링크</h4>", unsafe_allow_html=True)
        
        for kimchi in packaged_kimchi:
            st.markdown(f"- [{kimchi['name']}]({kimchi['url']})")

else:
    st.info("👈 왼쪽 사이드바에서 정보를 입력하고 '비교하기' 버튼을 눌러주세요.")