# STEP 01. 파이썬 기본 : 채팅 서비스 만들기 — AI 서비스 백엔드 프로그래밍 실무

**STEP 01 목표** — 파이썬 기초부터 FastAPI까지 익히고, 그동안 만든 부품을 조립해 **LLM 챗봇 v0.1**을 완성한다.

- 결과물: `/chat` API + Streamlit 채팅 화면 + 대화 기록 저장 + 로그


## 공통 실습 자료

### 프로젝트 폴더

과정 내내 하나의 폴더를 채워 나간다. STEP 01이 끝나면 아래 구조가 된다.

```
ai_agent/
├── data/
│   └── regulations.txt      ← 사내 규정 샘플 (아래)
├── app/
│   ├── __init__.py
│   ├── chat_utils.py        ← 메시지 함수 모듈 (8장)
│   ├── main.py              ← FastAPI 서버 (15장~)
│   ├── config.py            ← 설정 (8·17장)
│   ├── storage.py           ← 파일 저장 (9장~)
│   ├── conversation.py      ← 대화 클래스 (12장~)
│   ├── models.py            ← Pydantic 모델 (13장~)
│   ├── llm.py               ← LLM 호출 (17장~)
│   └── routers/
│       ├── __init__.py
│       ├── memos.py         ← 메모 API (15장)
│       └── chat.py          ← 대화 API (18장)
├── ui.py                    ← Streamlit 화면 (17장~)
├── step01/                  ← STEP 01 장별 실습 파일
├── streamlit_lab/           ← 부록 Streamlit 실습
├── .streamlit/
│   └── config.toml          ← Streamlit 설정 (17장)
├── .env                     ← API 키 (폴더를 압축해 넘길 때 뺀다)
├── .env.example             ← 키 목록 예시, 실제 키는 넣지 않음
├── .gitignore               ← uv가 만든다 (2장)
├── .python-version          ← 이 프로젝트가 쓸 파이썬 버전 (2장)
├── pyproject.toml           ← uv가 만드는 프로젝트 설정
├── uv.lock                  ← 설치된 패키지의 정확한 버전 (2장)
└── README.md
```