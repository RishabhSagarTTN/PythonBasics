import logging
logging.basicConfig(filename="hiio.txt", format="%(asctime)s - %(levelname)s - %(message)s",level=logging.INFO)
dic = {}
def count(stri):
    """Count function count the frequency of the word in the string and print only those word with frequency more than 1
    with its length and frequency"""
    logging.info(f'Inside the function for the {stri}')
    sp = stri.split()  
    for word in sp:
        if word in dic:
           dic[word][1] += 1
        else:
            dic[word] = [len(word),1]
    logging.info("Function execution complete")      
    ans = {word:count for word, count in dic.items() if count[1] > 1}# make the final ans by taking only those word 
    # which has frequency more than 1

    print("Word\t Length\t Occurrence")
    for i in ans.keys():
        print(f"{i}\t {ans[i][0]}\t {ans[i][1]}") # print the result with frequency and its lenght of the word
    
    

count('''Python Multiline String Using Triple-Quotes Using the triple quotes style is one of the easiest and most common ways to split a large 
      string into a multiline Python string. Triple quotes (\''' or \""")
      can be used to create a multiline string. It allows you to format text 
      over many lines and include line breaks. Put two triple quotes around the 
      multiline Python string, one at the start and one at the end, to define it.''')



