# from .mod1 import hello # importing as relative path
import logging
logging.basicConfig(filename="latest.txt", format="%(asctime)s %(levelname)s %(message)s", level=logging.INFO)

def hi():
    logging.info("Hi function is called")
    print("mod2 ")
    # hello()
    logging.info("Hi function completed")
