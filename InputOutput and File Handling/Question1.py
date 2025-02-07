with open('number.txt','r') as file:
    with open('odd.txt','w') as odd:
            with open('even.txt','w') as even:
                    with open('float.txt','w') as floats:
                        # write the odd,even and the float number with there repective file namefrom the number.txt
                        for i in file:
                            i = i.strip().lstrip("-")
                            if i.isdigit():# if itis digit then check for odd and even else it is float 
                                if int(i)%2==0:
                                    even.write(f"{i}\n")
                                else:
                                    odd.write(f"{i}\n")
                            else:
                                floats.write(f"{i}\n")


