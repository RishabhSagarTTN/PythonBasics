import logging
logging.basicConfig(filename="hi.txt", format="%(asctime)s - %(levelname)s - %(message)s",level=logging.INFO)
dic = {}
def count(stri):
    """Count function count the frequency of the word in the string and print it"""
    logging.info(f'Inside the function for the {stri}')
    sp = stri.split()  # split the line into the list
    for word in sp:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
    logging.info("Function execution complete")      
    sorted_dict = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True)) # make the final result by sorting 
    print(sorted_dict)

count('''Python Multiline String Using Triple-Quotes Using the triple quotes style is one of the easiest and most common ways to split a large 
      string into a multiline Python string. Triple quotes (\''' or \""")
      can be used to create a multiline string. It allows you to format text 
      over many lines and include line breaks. Put two triple quotes around the 
      multiline Python string, one at the start and one at the end, to define it.''')
