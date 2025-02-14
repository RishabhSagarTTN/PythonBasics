class MathOperations:
    def __init__(self):
        pass
    def add(self, a, b, c=0): # add method for the addition of the two or three argument
        return a + b + c

addition=MathOperations() # making of the instance of the class
result1= addition.add(1, 2)
print(result1) 
result2= addition.add(1, 2, 3)
print(result2)  