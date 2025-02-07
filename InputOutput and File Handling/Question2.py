import json
# all the container to store the function, class , variables and the package in the Python_script file
function=[]
classes=[]
variables=set()
package=[]
with open('Python_script.py','r') as file:#reading te python file
    for line in file:
        line=line.strip()
        if line.startswith('prin'):
            continue
        temp=line.split()
        # finding the class, function, package and the variables in each line
        for index, value in enumerate(temp): 
            if value == 'class':
                lvar=temp[index+1]
                latestv=lvar.rstrip(":")               
                classes.append(latestv)
                break
            elif value == 'import':
                package.append(temp[index+1])  
                break
            elif value == 'def':
                answer=temp[index+1]
                ind=(answer.index('('))
                function.append(answer[:ind])
                break
            elif value == "=":
                for i in range(0,index):
                    lvari=temp[i]
                    if lvari.startswith("self"):
                        modvariable=lvari.split(".")[1]
                        variables.add(modvariable)
                    else:
                        variables.add(lvari)
                break
            else:
                continue        
result={"package":f"{package}",
        "function":f"{function}",
        "class":f"{classes}",
        "variable":f"{variables}"} 
jsonstr= json.dumps(result)# convert it into json
print(result)

        