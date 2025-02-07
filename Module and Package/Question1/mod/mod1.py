import logging
logging.basicConfig(filename="latest.txt", format="%(asctime)s %(levelname)s %(message)s", level=logging.INFO)

def hello():
    logging.info("Hello function is called")
    print("mod1")
    logging.info("Hello function is completed")
