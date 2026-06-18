import streamlit as st

# 페이지 기본 설정 (브라우저 탭에 표시될 이름)
st.set_page_config(page_title="규칙 나라 탐험!", page_icon="🧩", layout="wide")

# 1. 제목 영역
st.markdown("# 🧩 규칙 나라 탐험!")

# 2. 환영 인사 영역 (글씨 크기를 크게 키우고 이모지 추가)
st.markdown("### 🎉 규칙의 나라에 온 것을 환영해~~ ✨")
st.write("우리 주변에 숨겨진 재밌는 규칙들을 찾으러 함께 떠나볼까?")

# 시각적인 구분을 위한 선
st.markdown("---")

# 3. 탐험지 카드들 (3개 옵션)
st.markdown("### 🗺️ 탐험할 곳을 선택해봐! ")

col1, col2 = st.columns(2)

# 1번 탐험지: 이모지 모양 규칙
with col1:
    st.markdown(
        """
        <div style="background-color: #ffb74d; padding: 20px; border-radius: 10px; text-align: center; height: 200px; display: flex; flex-direction: column; justify-content: center; cursor: pointer;">
            <h2 style="margin: 0; color: white;">🎨 이모지 모양 규칙</h2>
            <p style="margin: 10px 0 0 0; color: white; font-size: 14px;">알록달록한 이모지들의 패턴을 찾아봐!</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("📍 이모지 탐험하기", use_container_width=True, key="emoji_btn"):
        st.switch_page("pages/이모지 모양 규칙.py")

# 2번 탐험지: 수의 배열 규칙
with col2:
    st.markdown(
        """
        <div style="background-color: #4fc3f7; padding: 20px; border-radius: 10px; text-align: center; height: 200px; display: flex; flex-direction: column; justify-content: center; cursor: pointer;">
            <h2 style="margin: 0; color: white;">🔢 수의 배열 규칙</h2>
            <p style="margin: 10px 0 0 0; color: white; font-size: 14px;">숫자들이 따라가는 규칙을 찾아봐!</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("📍 숫자 탐험하기", use_container_width=True, key="number_btn"):
        st.switch_page("pages/수의 배열 규칙.py")

col3, col4, col5 = st.columns(3)

# 3번 탐험지: 직접 규칙 만들기
with col4:
    st.markdown(
        """
        <div style="background-color: #f48fb1; padding: 20px; border-radius: 10px; text-align: center; height: 200px; display: flex; flex-direction: column; justify-content: center; cursor: pointer;">
            <h2 style="margin: 0; color: white;">🎨 나만의 규칙</h2>
            <p style="margin: 10px 0 0 0; color: white; font-size: 14px;">직접 규칙을 만들어서 보여줄래?</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("📍 규칙 만들기", use_container_width=True, key="create_btn"):
        st.switch_page("pages/직접 규칙 만들기.py")

# 시각적인 구분을 위한 선
st.markdown("---")

# 4. 사용법 가이드 영역 (st.info 위젯을 활용해 예쁜 파란색 박스로 강조)
st.markdown("#### 💡 이렇게 탐험해 봐요!")

guide_text = """
1. 👀 위의 3가지 탐험지 중에서 마음에 드는 곳을 선택해요!
2. 🎯 각 탐험지에서 재밌는 문제들을 풀어봐요!
3. 🎉 정답을 맞추면 풍선과 눈이 날려~~ 축하해줄 거야!
"""
st.info(guide_text)

# 하단에 아이들의 흥미를 돋우는 귀여운 문구 추가
st.markdown("#### 👆 위의 탐험지 중에서 하나를 선택하고 꾹 눌러줘! 🚀")
