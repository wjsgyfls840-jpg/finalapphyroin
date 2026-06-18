import streamlit as st

st.set_page_config(page_title="직접 규칙 만들기", page_icon="🎨", layout="centered")

# 다양한 테마별 에셋 리스트
shape_themes = {
    "🍎 과일": {
        "🍎": "사과",
        "🍌": "바나나",
        "🍇": "포도",
        "🍓": "딸기",
        "🍊": "오렌지",
    },
    "🐶 동물": {
        "🐶": "강아지",
        "🐱": "고양이",
        "🐭": "쥐",
        "🐹": "햄스터",
        "🐰": "토끼",
    },
    "⭐ 도형": {
        "⭐": "별",
        "🔺": "삼각형",
        "⬛": "네모",
        "🔵": "동그라미",
        "❤️": "하트",
    },
    "1️⃣ 숫자": {
        "1️⃣": "하나",
        "2️⃣": "둘",
        "3️⃣": "셋",
        "4️⃣": "넷",
        "5️⃣": "다섯",
    },
    "☀️ 날씨": {
        "☀️": "해",
        "🌙": "달",
        "⭐": "별",
        "☁️": "구름",
        "🌧️": "비",
    },
}

def detect_pattern(sequence):
    """규칙성이 있는지 감지하는 함수"""
    if len(sequence) < 2:
        return None, None
    
    # 숫자 이모지를 실제 숫자로 변환하는 매핑
    number_map = {
        "1️⃣": 1, "2️⃣": 2, "3️⃣": 3, "4️⃣": 4, "5️⃣": 5,
        "6️⃣": 6, "7️⃣": 7, "8️⃣": 8, "9️⃣": 9, "0️⃣": 0
    }
    
    # 숫자 수열인지 확인
    if all(emoji in number_map for emoji in sequence):
        numbers = [number_map[emoji] for emoji in sequence]
        
        # 산술 수열인지 확인 (최소 3개 이상의 같은 공차)
        if len(numbers) >= 3:
            differences = [numbers[i+1] - numbers[i] for i in range(len(numbers)-1)]
            # 모든 공차가 같으면 산술 수열
            if len(set(differences)) == 1:
                return sequence, "arithmetic"  # 산술 수열 표시
    
    # 반복 패턴 확인
    for pattern_len in range(1, len(sequence) // 2 + 1):
        pattern = sequence[:pattern_len]
        # 이 패턴이 몇 번 반복되는지 확인
        repeat_count = 0
        for i in range(0, len(sequence), pattern_len):
            if sequence[i:i+pattern_len] == pattern:
                repeat_count += 1
            else:
                break
        
        # 패턴이 최소 2번 이상 반복되면 규칙 발견
        if repeat_count >= 2 and pattern_len * repeat_count >= len(sequence):
            return pattern, repeat_count
    
    return None, None


if "rule_sequence" not in st.session_state:
    st.session_state.rule_sequence = []
    st.session_state.feedback = ""
    st.session_state.try_count = 0
    st.session_state.current_theme = "🍎 과일"


st.markdown("# 🎨 나만의 규칙 디자이너!")
st.markdown(
    "**아래에 있는 예쁜 모양 보기를 꾹꾹 눌러서 나만의 멋진 규칙을 만들어보세요!**"
)

st.write("\n")

# 테마 선택 섹션
st.markdown("## 📦 보기 테마 선택")
theme_cols = st.columns(len(shape_themes))
for idx, theme_name in enumerate(shape_themes.keys()):
    with theme_cols[idx]:
        if st.button(theme_name, key=f"theme_{theme_name}"):
            st.session_state.current_theme = theme_name
            st.session_state.rule_sequence = []
            st.session_state.feedback = ""
            st.session_state.try_count = 0
            st.rerun()

# 현재 테마 표시
st.info(f"현재 보기: **{st.session_state.current_theme}**")

st.write("\n")

# 모양 버튼들
st.markdown("## 모양 선택하기")
current_shapes = shape_themes[st.session_state.current_theme]
button_cols = st.columns(3)
for idx, (emoji, name) in enumerate(current_shapes.items()):
    with button_cols[idx % 3]:
        if st.button(f"{emoji} {name}", key=f"shape_{emoji}_{st.session_state.current_theme}"):
            st.session_state.rule_sequence.append(emoji)

st.write("\n")

# 나의 규칙 기차 표시
st.markdown("## 나의 규칙 기차 🚂")
if st.session_state.rule_sequence:
    display_text = " ➔ ".join(st.session_state.rule_sequence)
    st.markdown(f"## {display_text}")
else:
    st.markdown("### 모양을 클릭해서 규칙을 만들어보세요!")

st.write("\n")

# 초기화 버튼
col1, col2 = st.columns(2)
with col1:
    if st.button("처음부터 다시 만들기 🧹"):
        st.session_state.rule_sequence = []
        st.session_state.feedback = ""
        st.session_state.try_count = 0
        st.rerun()

# 규칙 완성 버튼
with col2:
    if st.button("규칙 완성! 🚀"):
        if len(st.session_state.rule_sequence) < 2:
            st.warning("최소 2개 이상의 모양을 선택해주세요!")
        else:
            pattern, pattern_type = detect_pattern(st.session_state.rule_sequence)
            
            if pattern:
                # 조건 A: 올바른 규칙이 있을 때
                if pattern_type == "arithmetic":
                    # 산술 수열인 경우
                    number_map = {
                        "1️⃣": 1, "2️⃣": 2, "3️⃣": 3, "4️⃣": 4, "5️⃣": 5,
                        "6️⃣": 6, "7️⃣": 7, "8️⃣": 8, "9️⃣": 9, "0️⃣": 0
                    }
                    numbers = [number_map[emoji] for emoji in st.session_state.rule_sequence]
                    diff = numbers[1] - numbers[0]
                    diff_text = f"[ {diff} ]씩 더해지는" if diff > 0 else f"[ {abs(diff)} ]씩 빼지는"
                    st.session_state.feedback = f"와! 우리 친구는 수가 {diff_text} 아주 멋진 규칙을 만들었구나! 대단해요! 🎨✨"
                else:
                    # 반복 패턴인 경우
                    pattern_names = " ".join([current_shapes[e] for e in pattern])
                    st.session_state.feedback = f"와! 우리 친구는 [ {pattern_names} ]가 반복되는 아주 멋진 규칙을 만들었구나! 대단해요! 🎨✨"
                st.session_state.try_count = 0
                st.balloons()
            else:
                st.session_state.try_count += 1
                
                if st.session_state.try_count == 1:
                    # 조건 B: 규칙이 없을 때 - 1차 경고
                    st.session_state.feedback = "으음? 모양들이 불규칙하게 서 있어요. 규칙이 있도록 다시 한번 예쁘게 순서를 맞춰볼래? 🤔"
                else:
                    # 조건 C: 또 규칙이 없을 때 - 2차 대안 제시
                    st.session_state.feedback = "규칙 만들기가 조금 어려웠나요? 처음부터 다시 만들기 버튼을 눌러서 다른 모양 친구들로 새롭게 만들어보자! 🧚‍♀️"

st.write("\n")

# 피드백 표시
if st.session_state.feedback:
    st.markdown(f"### {st.session_state.feedback}")

st.write("\n")

# 통계 표시
if st.session_state.rule_sequence:
    st.info(f"현재 만든 규칙의 길이: {len(st.session_state.rule_sequence)}개")
