import logging

from sqlalchemy import text

from app.database.session import SessionLocal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init() -> None:
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))
    except Exception as e:
        logger.error(e)
        raise e

def main() -> None:
    logger.info("Initializing DB")
    init()
    logger.info("DB finished Initializing")

if __name__ == "__main__":
    main()
