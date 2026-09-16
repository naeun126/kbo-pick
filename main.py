import streamlit as st

# ---------------------------------------------------
# 페이지 기본 설정
# ---------------------------------------------------
st.set_page_config(
    page_title="KBO 응원팀 찾기 ⚾",
    page_icon="⚾",
    layout="centered",
)

# ---------------------------------------------------
# 귀여운 스타일링 (CSS)
# ---------------------------------------------------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #eaf6ff 0%, #fff7e6 50%, #ffe9f2 100%);
    }
    .main-title {
        text-align: center;
        font-size: 40px;
        font-weight: 800;
        color: #2e86de;
        padding-top: 5px;
        text-shadow: 2px 2px 0px #ffffff;
    }
    .sub-title {
        text-align: center;
        font-size: 17px;
        color: #6b7a99;
        padding-bottom: 20px;
    }
    .question-box {
        background: #ffffffcc;
        border-radius: 20px;
        padding: 18px 22px;
        margin-bottom: 14px;
        box-shadow: 0px 4px 12px rgba(46, 134, 222, 0.15);
        border: 2px solid #d7ecff;
    }
    .result-card {
        background: #ffffffdd;
        border-radius: 25px;
        padding: 30px;
        margin-top: 20px;
        box-shadow: 0px 8px 20px rgba(46, 134, 222, 0.25);
        border: 3px dashed #a5d8ff;
        text-align: center;
    }
    .team-emoji {
        font-size: 60px;
    }
    .team-name {
        font-size: 30px;
        font-weight: 800;
        margin: 8px 0px;
    }
    .team-desc {
        font-size: 16px;
        color: #555555;
        line-height: 1.6;
        margin-top: 8px;
    }
    .tag {
        display: inline-block;
        background: #eaf6ff;
        color: #2e86de;
        border-radius: 20px;
        padding: 5px 14px;
        margin: 4px;
        font-size: 14px;
        font-weight: 600;
    }
    div.stButton > button {
        background: linear-gradient(135deg, #6fc3ff, #a6dcff);
        color: white;
        border: none;
        border-radius: 30px;
        padding: 12px 30px;
        font-size: 18px;
        font-weight: 700;
        box-shadow: 0px 4px 12px rgba(46, 134, 222, 0.4);
        transition: 0.2s;
    }
    div.stButton > button:hover {
        transform: scale(1.05);
        background: linear-gradient(135deg, #55b4ff, #8fd0ff);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------
# 팀 정보 데이터
# ---------------------------------------------------
team_info = {
    "LG 트윈스": {
        "emoji": "🐯",
        "color": "#C30452",
        "desc": "세련되고 트렌디한 걸 좋아하는 당신! 서울의 도시적인 감성과 화려한 응원 문화를 즐기는 LG 트윈스가 잘 맞아요.",
        "tags": ["#트렌디", "#서울", "#화려한응원"],
    },
    "두산 베어스": {
        "emoji": "🐻",
        "color": "#131230",
        "desc": "은근한 승부욕과 끈기를 가진 당신! 꾸준함과 저력으로 승부하는 두산 베어스와 찰떡궁합이에요.",
        "tags": ["#끈기", "#저력", "#전통명가"],
    },
    "KT 위즈": {
        "emoji": "🪄",
        "color": "#000000",
        "desc": "새로운 것에 열려있고 성장 가능성을 믿는 당신! 젊은 패기로 빠르게 성장한 KT 위즈가 어울려요.",
        "tags": ["#성장", "#젊음", "#도전"],
    },
    "SSG 랜더스": {
        "emoji": "🚀",
        "color": "#CE0E2D",
        "desc": "화끈하고 스케일 큰 걸 좋아하는 당신! 파워풀한 타격과 큰 무대를 즐기는 SSG 랜더스와 잘 맞아요.",
        "tags": ["#파워풀", "#스케일", "#인천"],
    },
    "NC 다이노스": {
        "emoji": "🦖",
        "color": "#315288",
        "desc": "독특하고 개성 있는 걸 좋아하는 당신! 공룡 마스코트처럼 유니크한 매력의 NC 다이노스가 잘 맞아요.",
        "tags": ["#개성", "#유니크", "#창원"],
    },
    "롯데 자이언츠": {
        "emoji": "🔵",
        "color": "#041E42",
        "desc": "정과 의리를 중요하게 여기는 당신! 부산 특유의 뜨거운 응원 열기를 가진 롯데 자이언츠와 찰떡이에요.",
        "tags": ["#의리", "#뜨거운응원", "#부산"],
    },
    "삼성 라이온즈": {
        "emoji": "🦁",
        "color": "#074CA1",
        "desc": "품격과 원칙을 중시하는 당신! 명문 구단의 전통과 안정감을 지닌 삼성 라이온즈가 잘 맞아요.",
        "tags": ["#명문", "#원칙", "#대구"],
    },
    "한화 이글스": {
        "emoji": "🦅",
        "color": "#FF6600",
        "desc": "포기하지 않는 뜨거운 마음을 가진 당신! 끝까지 응원하는 팬심으로 유명한 한화 이글스와 잘 맞아요.",
        "tags": ["#열정", "#의리팬심", "#대전"],
    },
    "KIA 타이거즈": {
        "emoji": "🐅",
        "color": "#EA0029",
        "desc": "자존심 강하고 우승 DNA를 믿는 당신! 최다 우승의 명가 KIA 타이거즈와 잘 어울려요.",
        "tags": ["#우승DNA", "#자존심", "#광주"],
    },
    "키움 히어로즈": {
        "emoji": "🦸",
        "color": "#570514",
        "desc": "실속과 스토리를 중요하게 여기는 당신! 육성으로 스타를 키워내는 키움 히어로즈와 잘 맞아요.",
        "tags": ["#실속", "#육성", "#스토리"],
    },
}

# ---------------------------------------------------
# 질문 및 팀별 점수 매핑
# ---------------------------------------------------
questions = [
    {
        "q": "1️⃣ 친구들 사이에서 나는 어떤 사람인가요?",
        "options": {
            "분위기 메이커, 화려한 걸 좋아함": ["LG 트윈스", "SSG 랜더스"],
            "묵묵히 자기 할 일 하는 믿음직한 타입": ["두산 베어스", "삼성 라이온즈"],
            "새로운 도전을 즐기는 실험 정신": ["KT 위즈", "NC 다이노스"],
            "의리 있고 정 많은 타입": ["롯데 자이언츠", "한화 이글스"],
        },
    },
    {
        "q": "2️⃣ 여행 스타일은 어느 쪽에 가까운가요?",
        "options": {
            "계획 없이 즉흥적으로 떠나는 편": ["KT 위즈", "SSG 랜더스"],
            "꼼꼼하게 일정을 다 짜고 움직이는 편": ["삼성 라이온즈", "두산 베어스"],
            "핫플레이스 위주로 트렌디하게": ["LG 트윈스", "KIA 타이거즈"],
            "숨은 명소 찾아다니는 걸 좋아함": ["NC 다이노스", "키움 히어로즈"],
        },
    },
    {
        "q": "3️⃣ 스트레스를 받으면 나는?",
        "options": {
            "일단 끝까지 참고 버틴다": ["한화 이글스", "두산 베어스"],
            "화끈하게 풀어버린다": ["롯데 자이언츠", "SSG 랜더스"],
            "냉정하게 원인부터 분석한다": ["삼성 라이온즈", "KT 위즈"],
            "주변 사람들과 수다로 푼다": ["LG 트윈스", "키움 히어로즈"],
        },
    },
    {
        "q": "4️⃣ 좋아하는 색깔 분위기는?",
        "options": {
            "레드 계열 - 강렬하고 열정적인": ["KIA 타이거즈", "SSG 랜더스"],
            "블루 계열 - 시원하고 신뢰감 있는": ["삼성 라이온즈", "롯데 자이언츠"],
            "블랙 계열 - 세련되고 차분한": ["두산 베어스", "KT 위즈"],
            "오렌지·핑크 계열 - 발랄하고 독특한": ["한화 이글스", "NC 다이노스"],
        },
    },
    {
        "q": "5️⃣ 나에게 야구란?",
        "options": {
            "결과보다 과정을 즐기는 것": ["키움 히어로즈", "NC 다이노스"],
            "무조건 이겨야 제맛": ["KIA 타이거즈", "SSG 랜더스"],
            "오랜 전통과 스토리를 응원하는 것": ["삼성 라이온즈", "두산 베어스"],
            "그날 분위기와 축제를 즐기는 것": ["LG 트윈스", "롯데 자이언츠"],
        },
    },
]

# ---------------------------------------------------
# 화면 구성
# ---------------------------------------------------
st.markdown('<div class="main-title">⚾ 나의 KBO 응원팀 찾기 ⚾</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">몇 가지 질문에 답하면 나와 찰떡인 구단을 찾아드려요! 🎉</div>', unsafe_allow_html=True)

answers = []
for i, item in enumerate(questions):
    st.markdown(f'<div class="question-box">', unsafe_allow_html=True)
    choice = st.radio(item["q"], list(item["options"].keys()), key=f"q{i}")
    st.markdown("</div>", unsafe_allow_html=True)
    answers.append(item["options"][choice])

if st.button("⚾ 나의 응원팀 확인하기!"):
    scores = {team: 0 for team in team_info}
    for teams in answers:
        for t in teams:
            scores[t] += 1

    best_team = max(scores, key=scores.get)
    info = team_info[best_team]
    tags_html = "".join([f'<span class="tag">{t}</span>' for t in info["tags"]])

    st.markdown(
        f"""
        <div class="result-card" style="border-color:{info['color']}55;">
            <div class="team-emoji">{info['emoji']}</div>
            <div class="team-name" style="color:{info['color']};">당신의 운명의 구단은...</div>
            <div class="team-name" style="color:{info['color']}; font-size:26px;">✨ {best_team} ✨</div>
            <div class="team-desc">{info['desc']}</div>
            <div style="margin-top:15px;">{tags_html}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.balloons()

st.markdown("---")
st.markdown(
    "<div style='text-align:center; color:#aaaaaa; font-size:13px;'>Made with ⚾ by Streamlit</div>",
    unsafe_allow_html=True,
)
