# 도전 — step01/parrot.py (앵무새 챗봇에서 바뀌는 부분)
from app.storage import load_conversation, save_conversation
import logging

SESSION_ID = "me"
conversation = load_conversation(SESSION_ID)
logger = logging.getLogger("parrot")

print("앵무새 챗봇입니다. '종료'를 입력하면 끝납니다.")

while True:
    user_input = input("👤 ").strip()

    banned = ["비밀번호", "주민번호", "계좌"]
    if any(word in user_input for word in banned):
        logger.warning("금칙어가 포함된 입력을 차단했다.")
        continue
    
    elif user_input == "종료":
        print("대화를 종료합니다.")
        break
    if not user_input:
        continue

    logger.info("사용자 입력: %s", user_input)
    

print(f"총 메시지 수: {len(conversation)}")