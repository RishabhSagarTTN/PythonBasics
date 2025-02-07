import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-d','--deliminator',type=str, default=',')
parser.add_argument('-q','--quote',type=str, default='"')
parser.add_argument('-f', '--col', nargs='+', type=int,default=[0,1])
parser.add_argument('--head', type=int, default=0)
parser.add_argument('--tail', type=int, default=0)
parser.add_argument('csvlook', type=str)

parser.add_argument('--skip', type=int, default=0)
# argparse is used to get the value from the command line with the repect variable
# csvloop command is mandatory to run the program

args = parser.parse_args()
deliminator=args.deliminator
passed=args.col
quote=args.quote
head=args.head
tail=args.tail
skip=args.skip
# these are the parameter that is taken from the command line some of them isoptional and set with defaults

# condition is put so that no conflict is arrised if arrised throw an error
if (head>0 and skip>0 or tail>0) or (skip>0 and head>0 or tail>0) or (tail>0 and head>0 or skip>0):
    raise ValueError("Error")

with open("../customers-100.csv", 'r') as file:# csv file is open to read 
    with open('final.csv', 'w+') as finals:
        for i in file:
            temp=[]
            line=i.split(deliminator)
            for col in range(0,len(passed)):
                if len(line)>passed[col]:
                    latest=line[passed[col]]+quote
                    temp.append(f"{quote}{latest:<15}")
            finals.write(" ".join(temp)+"\n")# make the final file with the respective col that is passed in terminal
        finals.seek(0)    

# read and print the data from the final with the respective condition that is passed in the terminal
        if head >0:
            for i in range(0,head):
                print(finals.readline())
        elif tail >0:
            ans=finals.readlines()
            number=len(finals.readlines())
            f=number-tail
            for i in range(f,number):
                print(ans[f])            
        elif skip>0:
            count=0
            for j in finals:
                if count<skip:
                    count+=1
                    continue
                print(j)    


            
                     
                     
                     
            

