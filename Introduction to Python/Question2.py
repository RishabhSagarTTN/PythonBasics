import logging

logging.basicConfig(filename="primes.log", level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

def binary(number):
    """generates binary for the particular number and return it"""
    logging.info(f"Converting {number} to binary")

    bin=""
    while number>0:
        bin=str(number%2)+bin
        number//=2
    logging.info(f"Binary result: {bin}")

    return bin


def octal(number):
    """generates octal for the particular number and return it"""
    logging.info(f"Converting {number} to octal")
    oct=""
    while number>0:
        oct=str(number%8)+oct
        number//=8
    logging.info(f"octal result: {oct}")

    return oct

def hexadecimal(number):
    """generates hexadecimal for the particular number and return it"""
    logging.info(f"Converting {number} to hexadecimal")
    hex="0123456789ABCDEF"
    hexa=""
    while number>0:
        hexa=hexa[number%16]+ hexa
        number//=16
    logging.info(f"hexadecimal result: {hexa}")

    return hexa


try:
    num=int(input("Enter a number")) # take number from the user for the evaluation
    choice= input("b for binary, o for octal and h for hexadecimal").lower()# choose which conversion you wanted
    if choice=='b':
        print(f"{binary(num)}")
    elif choice=='o':
        print(f"{octal(num)}")
    elif choice == 'h':
        print(f"{hexadecimal(num)}")
    else: # ifnumber is 0, there is no point for execution
        print("0")
except ValueError:
    logging.error("Invalid input")                    