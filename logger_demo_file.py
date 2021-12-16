import logging

class LoggerFileDemo():
    def filelog(self):
        ## Created Logger
        logger = logging.getLogger(name=LoggerFileDemo.__name__)
        logger.setLevel(logging.INFO)

        ## Create Handler
        filehandler = logging.FileHandler(filename="FileHanlder.log", mode="w")
        filehandler.setLevel(logging.DEBUG)

        ## Create Formatter
        formatter = logging.Formatter("%(asctime)s : %(name)s : %(levelname)s : %(message)s", datefmt='%d/%m/%Y %I:%M:%S %p')

        ## Add formater to Handler
        filehandler.setFormatter(formatter)

        ## Add Handler to logger
        logger.addHandler(filehandler)

        ## Log Messages
        logger.debug("This is Updated DEBUG Message.")
        logger.info("This is Updated INFO Message.")
        logger.warning("This is Updated WARNING Message.")
        logger.error("This is Updated ERROR Message.")
        logger.critical("This is Updated CRITICAL Message.")

demo = LoggerFileDemo()

demo.filelog()