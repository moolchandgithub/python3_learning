import inspect
import logging

def customLogger(loglevel):
    loggername = inspect.stack()[1][3]
    logger = logging.getLogger(loggername)
    logger.setLevel(logging.DEBUG)

    handler = logging.FileHandler("{0}.log".format(loggername), mode='w')
    handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s : %(name)s : %(levelname)s : %(message)s", datefmt='%d/%m/%Y %I:%M:%S %p')

    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger