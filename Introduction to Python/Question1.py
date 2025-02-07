import logging

logging.basicConfig(filename="primes.log", level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")


def is_prime(number):
    """function used to check weather the number is prime or not"""

    logging.info(f"function is called for {number}")
    if number<2:
        return False
    for i in range (2,int(number**0.5)+1):# checks weather the number is prime or not
        logging.info("Inside the loop")
        if number%i==0:
            logging.info(f"{number} is not the prime number")
            return False
        logging.info(f"{number} is the prime number")
        return True
    
value=is_prime(int(input("Enter the number")))# take number from the user for checking
if value:
    print("Number is prime")
else:
    print("Number is not prime")    

