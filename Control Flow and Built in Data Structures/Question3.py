import logging
logging.basicConfig(filename="hii.txt", format="%(asctime)s - %(levelname)s - %(message)s",level=logging.INFO)
dic = {}
def count(stri):
    """Count function count the frequency of the word in the string and print only those word with frequency more than 1"""
    logging.info(f'Inside the function for the {stri}')
    sp = stri.split()  
    for word in sp:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
    logging.info("Function execution complete")      
    ans = ([word for word, count in dic.items() if count > 1]) # make the final ans by taking only those word 
    # which has frequency more than 1

    for i in ans:
        print(i)

count('''Python Multiline String Using Triple-Quotes Using the triple quotes style is one of the easiest and most common ways to split a large 
      string into a multiline Python string. Triple quotes (\''' or \""")
      can be used to create a multiline string. It allows you to format text 
      over many lines and include line breaks. Put two triple quotes around the 
      multiline Python string, one at the start and one at the end, to define it.''')
