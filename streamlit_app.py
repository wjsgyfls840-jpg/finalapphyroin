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
st.markdown("### 🗺️ 너가 탐험할 수 있는 곳이야! ")

# 1번 탐험지: 이모지 모양 규칙
st.markdown(
    """
    <div style="background-color: #ffb74d; padding: 15px; border-radius: 10px; text-align: center; height: 100px; display: flex; flex-direction: column; justify-content: center; cursor: pointer;">
        <h3 style="margin: 0; color: white;">🎨 이모지 모양 규칙</h3>
        <p style="margin: 5px 0 0 0; color: white; font-size: 13px;">알록달록한 이모지들의 패턴을 찾아봐!</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")

# 2번 탐험지: 수의 배열 규칙
st.markdown(
    """
    <div style="background-color: #4fc3f7; padding: 15px; border-radius: 10px; text-align: center; height: 100px; display: flex; flex-direction: column; justify-content: center; cursor: pointer;">
        <h3 style="margin: 0; color: white;">🔢 수의 배열 규칙</h3>
        <p style="margin: 5px 0 0 0; color: white; font-size: 13px;">숫자들이 따라가는 규칙을 찾아봐!</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")

# 3번 탐험지: 직접 규칙 만들기
st.markdown(
    """
    <div style="background-color: #f48fb1; padding: 15px; border-radius: 10px; text-align: center; height: 100px; display: flex; flex-direction: column; justify-content: center; cursor: pointer;">
        <h3 style="margin: 0; color: white;">🎨 나만의 규칙</h3>
        <p style="margin: 5px 0 0 0; color: white; font-size: 13px;">직접 규칙을 만들어서 보여줄래?</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# 시각적인 구분을 위한 선
st.markdown("---")

# 4. 사용법 가이드 영역 (st.info 위젯을 활용해 예쁜 파란색 박스로 강조)
st.markdown("#### 💡 이렇게 탐험해 봐요!")

guide_text = """
1. 👀 위의 3가지 탐험지를 살펴봐요!
2. 🔍 **왼쪽 사이드바 메뉴**에서 원하는 탐험지를 클릭해요!
3. 🎉 각 탐험지에서 재밌는 문제들을 풀어봐요!
"""
st.info(guide_text)

# 하단에 아이들의 흥미를 돋우는 귀여운 문구 추가
st.markdown("#### 👈 준비가 되었다면 왼쪽 사이드바 메뉴를 꾹 눌러줘! 🚀")
