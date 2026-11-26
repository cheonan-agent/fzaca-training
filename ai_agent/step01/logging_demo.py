# step01/logging_demo.py
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("ai_agent")

logger.debug("디버그용 상세 정보")
logger.info("서버 시작")
logger.warning("대화가 길다: 42개 메시지")
logger.error("LLM 호출 실패")