# step01/logging_file.py
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(),                                    # 화면에
        logging.FileHandler("data/ai_agent.log", encoding="utf-8"),  # 파일에
    ],
)
logger = logging.getLogger("ai_agent")

def handle(question):
    logger.info("질문 수신: %s", question)
    try:
        days = int(question)
    except ValueError:
        logger.exception("숫자 변환 실패")
        return None
    return days

handle("15")
handle("열다섯")