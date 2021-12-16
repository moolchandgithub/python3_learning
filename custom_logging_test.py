import logging
import custom_logger as cl

class CustomDemo():
    log = cl.customLogger(logging.INFO)

    def method1(self):
        self.log.debug('debug message')
        self.log.info('info message')
        self.log.warning('warn message')
        self.log.error('error message')
        self.log.critical('critical message')

    def method2(self):
        M2Log = cl.customLogger(logging.DEBUG)
        M2Log.debug('debug message')
        M2Log.info('info message')
        M2Log.warning('warn message')
        M2Log.error('error message')
        M2Log.critical('critical message')

    def method3(self):
        M3log = cl.customLogger(logging.DEBUG)
        M3log.debug('debug message')
        M3log.info('info message')
        M3log.warning('warn message')
        M3log.error('error message')
        M3log.critical('critical message')

demo = CustomDemo()

demo.method1()
demo.method2()
demo.method3()
