import logging
import sys

logger = logging.getLogger("paradise")
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("[%(levelname)s] %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

def set_level(level):
    logger.setLevel(level)
