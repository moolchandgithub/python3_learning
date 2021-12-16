import logging

logging.basicConfig(filename="Logfile.log", level=logging.DEBUG, filemode="w", format="%(asctime)s : %(levelname)s : %(message)s", datefmt='%d/%m/%Y %I:%M:%S %p')
logging.debug("This is Updated DEBUG Message.")
logging.info("This is Updated INFO Message.")
logging.warning("This is Updated WARNING Message.")
logging.error("This is Updated ERROR Message.")
logging.critical("This is Updated CRITICAL Message.")
