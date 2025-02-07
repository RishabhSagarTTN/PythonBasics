import logging
logging.basicConfig(filename="hello.txt", format="%(asctime)s - %(levelname)s - %(message)s",level=logging.INFO)
def vowels(s):
    """Vowels function count the number of vowels present in the word and return it"""
    # logging.info(f"Vowels function is called for {s}")
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    total=sum(1 for char in s if char in vowels)
    # logging.info(f"vowels function return the value {total}")
    return total

def filterw(stri):
    """filterw function filter the substring with the even number of vowels"""
    logging.info(f"filterw function is called for {stri}")
    words = stri.split()  # split input string into words
    fil = [word for word in words if vowels(word) % 2 != 0]  # filter words with even vowels
    logging.info(f"filterw function return the value {fil}")
    return " ".join(fil)  # Join words back into a string

input_string = str(input("Enter the line ")) # input from the user
out_string = filterw(input_string)
print(out_string)
logging.info("Execution complete")