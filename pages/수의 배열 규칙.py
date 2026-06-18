import random

import streamlit as st

st.set_page_config(page_title="수의 배열 규칙", page_icon="🔢", layout="centered")

pattern_bank = [
    {
        "pattern": "3, 6, 9, 12, 15, 18, [ ? ]",
        "answer": 21,
        "feedback": "딩동댕! 이 수의 배열은 앞의 수에 [ 3 ]씩 더해지는 규칙이 있어요! 🔢✨",
        "choices": [21, 24],
    },
    {
        "pattern": "10, 15, 20, 25, 30, [ ? ]",
        "answer": 35,
        "feedback": "딩동댕! 이 수의 배열은 앞의 수에 [ 5 ]씩 더해지는 규칙이 있어요! 🔢✨",
        "choices": [35, 40],
    },
    {
        "pattern": "24, 20, 16, 12, 8, [ ? ]",
        "answer": 4,
        "feedback": "딩동댕! 이 수의 배열은 앞의 수에 [ 4 ]씩 빼지는 규칙이 있어요! 🔢✨",
        "choices": [4, 6],
    },
    {
        "pattern": "120, 130, 140, 150, [ ? ]",
        "answer": 160,
        "feedback": "딩동댕! 이 수의 배열은 앞의 수에 [ 10 ]씩 더해지는 규칙이 있어요! 🔢✨",
        "choices": [160, 170],
    },
    {
        "pattern": "5, 10, 15, 20, [ ? ]",
        "answer": 25,
        "feedback": "딩동댕! 이 수의 배열은 앞의 수에 [ 5 ]씩 더해지는 규칙이 있어요! 🔢✨",
        "choices": [25, 30],
    },
    {
        "pattern": "18, 15, 12, 9, [ ? ]",
        "answer": 6,
        "feedback": "딩동댕! 이 수의 배열은 앞의 수에 [ 3 ]씩 빼지는 규칙이 있어요! 🔢✨",
        "choices": [6, 7],
    },
    {
        "pattern": "1, 2, 3, 4, 5, [ ? ]",
        "answer": 6,
        "feedback": "딩동댕! 이 수의 배열은 앞의 수에 [ 1 ]씩 더해지는 규칙이 있어요! 🔢✨",
        "choices": [6, 7],
    },
    {
        "pattern": "2, 4, 6, 8, [ ? ]",
        "answer": 10,
        "feedback": "딩동댕! 이 수의 배열은 앞의 수에 [ 2 ]씩 더해지는 규칙이 있어요! 🔢✨",
        "choices": [10, 12],
    },
    {
        "pattern": "7, 14, 21, 28, [ ? ]",
        "answer": 35,
        "feedback": "딩동댕! 이 수의 배열은 앞의 수에 [ 7 ]씩 더해지는 규칙이 있어요! 🔢✨",
        "choices": [35, 42],
    },
    {
        "pattern": "100, 90, 80, 70, [ ? ]",
        "answer": 60,
        "feedback": "딩동댕! 이 수의 배열은 앞의 수에 [ 10 ]씩 빼지는 규칙이 있어요! 🔢✨",
        "choices": [60, 65],
    },
    {
        "pattern": "8, 12, 16, 20, [ ? ]",
        "answer": 24,
        "feedback": "딩동댕! 이 수의 배열은 앞의 수에 [ 4 ]씩 더해지는 규칙이 있어요! 🔢✨",
        "choices": [24, 26],
    },
]

if "quiz_index" not in st.session_state:
    st.session_state.quiz_index = random.randrange(len(pattern_bank))
    st.session_state.feedback = ""
    st.session_state.last_answer = None
    st.session_state.try_count = 0


def set_new_quiz():
    new_index = st.session_state.quiz_index
    while new_index == st.session_state.quiz_index:
        new_index = random.randrange(len(pattern_bank))
    st.session_state.quiz_index = new_index
    st.session_state.feedback = ""
    st.session_state.last_answer = None
    st.session_state.try_count = 0


def handle_answer(choice):
    if choice == current_quiz["answer"]:
        st.session_state.feedback = current_quiz["feedback"]
        st.session_state.try_count = 0
        st.snow()
    else:
        st.session_state.try_count += 1
        if st.session_state.try_count == 1:
            st.session_state.feedback = (
                "아쉽지만 아직 아니에요. 한번만 더 기회를 줄게요! 숫자의 차이를 다시 살펴봐요. 🔍"
            )
        else:
            st.session_state.feedback = (
                "두 번째 기회도 틀렸어요. 다음 문제에서 다시 도전해볼까요? 😄"
            )


current_quiz = pattern_bank[st.session_state.quiz_index]

st.markdown("# 🔢 마법의 숫자! 수의 배열 규칙 나라")
st.markdown(
    "**숫자들이 어떤 비밀을 가지고 늘어나거나 줄어들고 있나요? 규칙을 찾아 빈칸 [ ? ]에 올 알맞은 숫자를 맞춰보세요!**"
)

st.write("\n")

st.markdown("## " + current_quiz["pattern"])

st.write("\n")

button_col1, button_col2 = st.columns(2)
with button_col1:
    if st.button(str(current_quiz["choices"][0])):
        st.session_state.last_answer = current_quiz["choices"][0]
        handle_answer(current_quiz["choices"][0])
with button_col2:
    if st.button(str(current_quiz["choices"][1])):
        st.session_state.last_answer = current_quiz["choices"][1]
        handle_answer(current_quiz["choices"][1])

st.write("\n")
if st.session_state.feedback:
    st.markdown(f"### {st.session_state.feedback}")

st.write("\n")
if st.button("다른 문제 풀기 🔄"):
    set_new_quiz()
