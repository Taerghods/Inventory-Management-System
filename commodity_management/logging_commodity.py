import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

def setup_logging(log_level):
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y/%m/%d %H:%M:%S %p',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler('test.log')
        ]
    )


# main.py
# from config_logging import setup_logging

class Test1:
    def say_hello(self, name):
        setup_logging(logging.DEBUG)
        logger = logging.getLogger("class Test")
        logger.debug(f"start {name}")
        logger.info(f"{name} successfully ")
        logger.error(f"end {name}")

t1 = Test1()
t1.say_hello("Ali")

