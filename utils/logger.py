import logging
from pathlib import Path
LOG_FILE = Path(__file__).resolve().parent.parent / "app.log"

def configure_logging():
    logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
