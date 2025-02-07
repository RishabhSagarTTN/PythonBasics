from datetime import *
import logging
logging.basicConfig(filename="piki.txt",format="%(asctime)s %(levelname)s %(message)s", level=logging.INFO)
def datecount(step,start=date.today()):
    """function to calculate the dates in the future based on the current time and the steps"""
    logging.info("Inside the function")
    dic= {
        "daily": timedelta(days=1),
        "alternative": timedelta(days=2),
        "weekly": timedelta(weeks=1),
        "monthly": timedelta(weeks=4),  
        "quaterly": timedelta(weeks=16),
        "yearly": timedelta(days=365),
    }# mapping for the steps so that we can apply operation based on that
    diff = dic[step]  
    while True:
        yield start
        start += diff

    

dc = datecount(step='quaterly') # generator for the datecount
for i in range(10): 
    print (next(dc)) 
logging.info("Execution complete")    
