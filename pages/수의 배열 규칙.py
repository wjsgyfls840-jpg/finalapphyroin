import random
import re

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


# 필터: 패턴 문자열과 정답/선택지가 모두 한자리수(절댓값이 0~9)인지 검사
def _is_single_digit_number(n: int) -> bool:
    # 10 미만의 자연수만 허용 (1..9)
    try:
        v = int(n)
    except Exception:
        return False
    return 1 <= v < 10


def _pattern_has_only_single_digits(pattern_str: str) -> bool:
    nums = re.findall(r"\d+", pattern_str)
    if not nums:
        return False
    return all(_is_single_digit_number(int(x)) for x in nums)


# 사용 가능한 문제 은행: 한자리수만 포함된 문제들. 없으면 전체 은행을 사용.
available_bank = [
    q
    for q in pattern_bank
    if _is_single_digit_number(q.get("answer", 999))
    and all(_is_single_digit_number(c) for c in q.get("choices", []))
    and _pattern_has_only_single_digits(q.get("pattern", ""))
]

if not available_bank:
    available_bank = pattern_bank

if "quiz_index" not in st.session_state:
    st.session_state.quiz_index = random.randrange(len(available_bank))
    st.session_state.feedback = ""
    st.session_state.last_answer = None
    st.session_state.generated_quiz = None
    st.session_state.answered = False
    st.session_state.try_count = 0


def set_new_quiz():
    # 무작위로 규칙 생성 문제를 만들어 표시하도록 한다 (항상 한자리수)
    gen = generate_random_quiz()
    if gen is None:
        # 생성 실패 시 기존 은행에서 다른 문제로 전환
        n = len(available_bank)
        if n <= 1:
            st.session_state.feedback = "문제가 한 개뿐입니다. 새 문제를 추가해보세요!"
            return
        choices = [i for i in range(n) if i != st.session_state.quiz_index]
        st.session_state.quiz_index = random.choice(choices)
        st.session_state.generated_quiz = None
    else:
        st.session_state.generated_quiz = gen
    st.session_state.feedback = ""
    st.session_state.last_answer = None
    st.session_state.try_count = 0
    st.session_state.answered = False


def generate_random_quiz():
    # step: -4..-1, 1..4 (정수 증감)
    steps = [i for i in range(-4, 5) if i != 0]
    random.shuffle(steps)
    for step in steps:
        length = random.choice([4, 5])  # 보여줄 항 수 (마지막이 빈칸)
        # 가능한 start 범위 계산하여 1..9 범위의 자연수만 생성
        if step > 0:
            start_min = 1
            start_max = 9 - step * (length - 1)
        else:
            start_min = 1 - step * (length - 1)
            start_max = 9
        if start_min > start_max:
            continue
        possible_starts = list(range(start_min, start_max + 1))
        if not possible_starts:
            continue
        start = random.choice(possible_starts)
        seq = [start + step * i for i in range(length)]
        # 안전 검사: 모든 항이 1..9인지 확인
        if not all(1 <= x < 10 for x in seq):
            continue
        pattern_str = ", ".join(str(x) for x in seq[:-1]) + ", [ ? ]"
        answer = seq[-1]
        # 생성할 오답 후보 (1..9 범위, 정수)
        distractors = [answer + d for d in (-2, -1, 1, 2)]
        distractors = [d for d in distractors if 1 <= d < 10 and d != answer]
        if not distractors:
            continue
        wrong = random.choice(distractors)
        choices = [answer, wrong]
        random.shuffle(choices)
        if step > 0:
            feedback = f"딩동댕! 이 수의 배열은 앞의 수에 [ {abs(step)} ]씩 더해지는 규칙이 있어요! 🔢✨"
        else:
            feedback = f"딩동댕! 이 수의 배열은 앞의 수에 [ {abs(step)} ]씩 빼지는 규칙이 있어요! 🔢✨"
        return {
            "pattern": pattern_str,
            "answer": answer,
            "feedback": feedback,
            "choices": choices,
        }
    return None


def handle_answer(choice):
    if choice == current_quiz["answer"]:
        st.session_state.feedback = "정답입니다!"
        st.session_state.try_count = 0
        st.session_state.answered = True
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


current_quiz = st.session_state.generated_quiz or available_bank[st.session_state.quiz_index]

st.markdown("# 🔢 마법의 숫자! 수의 배열 규칙 나라")
st.markdown(
    "**숫자들이 어떤 비밀을 가지고 늘어나거나 줄어들고 있나요? 규칙을 찾아 빈칸 [ ? ]에 올 알맞은 숫자를 맞춰보세요!**"
)

st.write("\n")

st.markdown("## " + current_quiz["pattern"])

st.write("\n")

button_col1, button_col2 = st.columns(2)
with button_col1:
    key0 = f"choice0_{hash(current_quiz['pattern'])}"
    if st.button(str(current_quiz["choices"][0]), key=key0):
        st.session_state.last_answer = current_quiz["choices"][0]
        handle_answer(current_quiz["choices"][0])
with button_col2:
    key1 = f"choice1_{hash(current_quiz['pattern'])}"
    if st.button(str(current_quiz["choices"][1]), key=key1):
        st.session_state.last_answer = current_quiz["choices"][1]
        handle_answer(current_quiz["choices"][1])

st.write("\n")
if st.session_state.feedback:
    st.markdown(f"### {st.session_state.feedback}")

st.write("\n")
if st.button("다른 문제 풀기 🔄"):
    set_new_quiz()
