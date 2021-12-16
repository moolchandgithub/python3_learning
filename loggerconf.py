import logging
import logging.config

class LoggerDemoConf():
    def ConfFileDemo(self):
        logging.config.fileConfig("LoggerConfFile.txt")
        logger = logging.getLogger(LoggerDemoConf.__name__)

        ## Log Messages
        logger.debug("This is Updated DEBUG Message.")
        logger.info("This is Updated INFO Message.")
        logger.warning("This is Updated WARNING Message.")
        logger.error("This is Updated ERROR Message.")
        logger.critical("This is Updated CRITICAL Message.")


demo = LoggerDemoConf()

demo.ConfFileDemo()

logging.config.fileConfig("LoggerConfFile.txt")

logging.debug("This is printed using Logger")