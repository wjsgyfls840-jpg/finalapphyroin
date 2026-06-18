import random

import streamlit as st

st.set_page_config(page_title="이모지 모양 규칙", page_icon="🔮", layout="centered")

base_patterns = [
    {
        "pattern": "🍎 🍎 🍌 🍎 🍎 🍌 🍎 [ ? ]",
        "answer": "🍎",
        "feedback": "정답입니다! 이 규칙은 [사과, 사과, 바나나]가 순서대로 반복되는 규칙이에요! 🍎✨",
        "choice_a": "🍎 사과",
        "choice_b": "🍌 바나나",
    },
    {
        "pattern": "⚽ 🏀 🏀 ⚽ 🏀 🏀 ⚽ [ ? ]",
        "answer": "🏀",
        "feedback": "정답입니다! 이 규칙은 [공, 농구공, 농구공]이 순서대로 반복되는 규칙이에요! 🏀✨",
        "choice_a": "⚽ 축구공",
        "choice_b": "🏀 농구공",
    },
    {
        "pattern": "🐶 🐱 🐰 🐶 🐱 🐰 🐶 [ ? ]",
        "answer": "🐱",
        "feedback": "정답입니다! 이 규칙은 [개, 고양이, 토끼]가 순서대로 반복되는 규칙이에요! 🐱✨",
        "choice_a": "🐱 고양이",
        "choice_b": "🐰 토끼",
    },
    {
        "pattern": "🌟 ⭐⭐ ⭐⭐⭐ 🌟 ⭐⭐ [ ? ]",
        "answer": "⭐⭐⭐",
        "feedback": "정답입니다! 이 규칙은 [1개, 2개, 3개]의 별이 차례대로 커지는 규칙이에요! ⭐⭐⭐✨",
        "choice_a": "⭐⭐⭐ 별 3개",
        "choice_b": "⭐ 별 1개",
    },
]

extra_patterns = [
    {
        "pattern": "🍓 🍓 🍓 🍌 🍌 🍌 🍓 [ ? ]",
        "answer": "🍓",
        "feedback": "정답입니다! 이 규칙은 [딸기, 딸기, 딸기, 바나나, 바나나, 바나나]가 반복되는 규칙이에요! 🍓✨",
        "choice_a": "🍌 바나나",
        "choice_b": "🍓 딸기",
    },
    {
        "pattern": "🟠 🟠 🟢 🟠 🟠 🟢 🟠 [ ? ]",
        "answer": "🟠",
        "feedback": "정답입니다! 이 규칙은 [주황, 주황, 초록]이 순서대로 반복되는 규칙이에요! 🟠✨",
        "choice_a": "🟠 주황",
        "choice_b": "🟢 초록",
    },
    {
        "pattern": "🐟 🐟 🦀 🐟 🐟 🦀 🐟 [ ? ]",
        "answer": "🐟",
        "feedback": "정답입니다! 이 규칙은 [물고기 두 마리, 게 한 마리]가 반복되는 규칙이에요! 🐟✨",
        "choice_a": "🦀 게",
        "choice_b": "🐟 물고기",
    },
    {
        "pattern": "🍋 🍋 🍉 🍉 🍋 🍋 🍉 [ ? ]",
        "answer": "🍉",
        "feedback": "정답입니다! 이 규칙은 [레몬, 레몬, 수박]이 반복되는 규칙이에요! 🍉✨",
        "choice_a": "🍋 레몬",
        "choice_b": "🍉 수박",
    },
]

all_patterns = base_patterns + extra_patterns

if "quiz_index" not in st.session_state:
    st.session_state.quiz_index = random.randrange(len(all_patterns))
    st.session_state.feedback = ""
    st.session_state.last_answer = ""
    st.session_state.try_count = 0


def set_new_quiz():
    new_index = st.session_state.quiz_index
    while new_index == st.session_state.quiz_index:
        new_index = random.randrange(len(all_patterns))
    st.session_state.quiz_index = new_index
    st.session_state.feedback = ""
    st.session_state.last_answer = ""
    st.session_state.try_count = 0


def handle_answer(choice):
    if choice.split()[0] == current_quiz["answer"]:
        st.session_state.feedback = current_quiz["feedback"]
        st.session_state.try_count = 0
        st.balloons()
    else:
        st.session_state.try_count += 1
        if st.session_state.try_count == 1:
            st.session_state.feedback = (
                "아쉽지만 아직 아니에요. 한번만 더 기회를 줄게요! 모양들의 순서를 다시 살펴볼까요? 💪"
            )
        else:
            st.session_state.feedback = (
                "두 번째 기회도 틀렸어요. 다음 문제를 풀어볼까요? 😊"
            )


current_quiz = all_patterns[st.session_state.quiz_index]

st.markdown("# 🔮 알록달록 이모지 모양 규칙 나라!")
st.markdown(
    "**반복되는 모양과 색깔 속에 숨은 규칙을 찾고, 마지막 빈칸 [ ? ]에 올 알맞은 모양을 맞춰보세요!**"
)

st.write("\n")

st.markdown("## " + current_quiz["pattern"])

st.write("\n")

button_col1, button_col2 = st.columns(2)
with button_col1:
    if st.button(current_quiz["choice_a"]):
        st.session_state.last_answer = current_quiz["choice_a"]
        handle_answer(current_quiz["choice_a"])
with button_col2:
    if st.button(current_quiz["choice_b"]):
        st.session_state.last_answer = current_quiz["choice_b"]
        handle_answer(current_quiz["choice_b"])

st.write("\n")
if st.session_state.feedback:
    st.markdown(f"### {st.session_state.feedback}")

st.write("\n")
if st.button("다른 문제 풀기 🔄"):
    set_new_quiz()
