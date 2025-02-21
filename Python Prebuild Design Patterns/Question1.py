class Prime:
    def __init__(self,number):
        self.numbers=number


    def test_primeNumber(self,number):
        """Function to test weather the number is prime or not"""
        if number <2: return False
        for i in range(2,int(number**0.5)+1):
            if number %i==0:
                return False
        return True 

                   
    
    def generate_primeNumber(self,number=1):
        """Function to generate the prime number starting from 2, it uses the generator so that it will generate the prime number every time you need
        and as many as we need"""
        self.number=number
        while True:
            self.number+=1
            for i in range(2,int(self.number**0.5)+1):
                if self.number %i==0:
                    break
            else:
                yield self.number

    def generate_primeNumberGreater(self,number):    
        """function to generate the greater prime number than the given number"""  
        self.numbergreater=number
        while True:
            self.numbergreater+=1
            for i in range(2,int(self.numbergreater**0.5)):
                if self.numbergreater %i==0:
                    break
            else:
                return self.numbergreater
            
    def generate_primeNumberLess(self,number):
        """Function to generate prime number less than the given number"""
        self.numberless=number
        while True:
            if self.numberless<0:
                return "No Prime number is less than the given number"
            self.numberless-=1
            for i in range(2,int(self.numberless**0.5)):
                if self.numberless %i==0:
                    break
            else:
                return self.numberless

    def generate_allprimeNumberbetween(self,smallest,largest):
        """generate the prime number in the given range"""
        self.ans=[]
        if smallest<0:
            smallest=1
        temp=self.__core(largest)
        for i in temp:
            if i>smallest and i<largest:
                self.ans.append(i)
        return self.ans
       

    def __core(self,lnumber):
        """It is the core function which generates all the prime till n number using the Sieve of Eratosthenes(it has better time complexity)"""
        prime=[True]*lnumber
        ans=[]
        for i in range(2,len(prime)):
            if prime[i]==True:
                for j in range(i*i,len(prime),i):
                    prime[j]=False
        for i in range(2,len(prime)):
            if prime[i]==True:
                ans.append(i)        
        return ans  


    def __len__(self):
        """It is a magic function, it check the size of the list structure which is made in generating the prime number in a given range"""
        return len(self.ans)
    
    def __str__(self):
        """User friendly string representation of the Prime object"""
        return f"Prime({self.numbers})"

    def __repr__(self):
        """Detailed string representation for debugging or inspection"""
        return f"The current prime number is {self.numbers}"

    def __add__(self,other):
        """Add a number to the current prime value and generate the next prime"""
        temp=self.generate_primeNumber(self.numbers+other)
        self.numbers=next(temp)
        return self.numbers

    def __iadd__(self,other):
        """Add a number to the current prime value and update it, returning the Prime object"""
        temp=self.generate_primeNumber(self.numbers+other)
        self.numbers=next(temp)
        return self # it will return the updated instance 
        
       
Number = Prime(11)

# Generate Prime Numbers
generatingPrimeNumber = Number.generate_primeNumber()
print(f"Generated Prime Numbers: {next(generatingPrimeNumber)}, {next(generatingPrimeNumber)}")

# Test if a number is prime
print(f"Is 5 a prime number? {Number.test_primeNumber(5)}")

# Generate a prime number less than a given number
print(f"Prime number less than 20: {Number.generate_primeNumberLess(20)}")

# Generate all prime numbers between two given numbers
print(f"Prime numbers between -10 and 30: {Number.generate_allprimeNumberbetween(-10, 30)}")

# Generate a prime number greater than a given number
print(f"Prime number greater than 20: {Number.generate_primeNumberGreater(20)}")

# Length of the list of primes in the generated range
print(f"Length of the prime list: {len(Number)}")

# Add a number to the current prime and generate the next prime
print(f"Prime after adding 6: {Number + 6}")

# Current state of the Prime object
print(f"Current Prime object: {Number}")

# Update the Prime object by adding 5
Number += 5
print(f"Prime object after incrementing by 5: {Number}")