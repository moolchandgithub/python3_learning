import logging

class LoggerDemo():

#    def testlog(self, sevr, mess):
    def testlog(self):
        ## Create Logger
        logger = logging.Logger(name=LoggerDemo.__name__, level=logging.WARNING)
#        logger.setLevel(logging.INFO)

        ## Create Handler 
        consolehandler = logging.StreamHandler()
        consolehandler.setLevel(logging.DEBUG)

        ## Create Formatter
        formatter = logging.Formatter("%(asctime)s : %(name)s : %(levelname)s : %(message)s", datefmt='%d/%m/%Y %I:%M:%S %p')

        ## Add formatter to console handler
        consolehandler.setFormatter(formatter)

        ## Add console handler to logger
        logger.addHandler(consolehandler)

        ## Log Messages
        logger.debug("This is Updated DEBUG Message.")
        logger.info("This is Updated INFO Message.")
        logger.warning("This is Updated WARNING Message.")
        logger.error("This is Updated ERROR Message.")
        logger.critical("This is Updated CRITICAL Message.")
"""         if sevr == "debug":
            logger.debug(f"{mess}")
        elif sevr == "info":
            logger.info(f"{mess}")
        elif sevr == "warning":
            logger.warning(f"{mess}")
        elif sevr == "error":
            logger.error(f"{mess}")
        elif sevr == "critical":
            logger.critical(f"{mess}")
        else:
            logger.error(f"Wrong Severity defined") """


demo = LoggerDemo()

demo.testlog()
