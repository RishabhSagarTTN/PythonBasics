class Database:
    instance = 0
    def __new__(cls, *args, **kwargs):
        if cls.instance==0:# limiting the class to create only one instance
            cls.instance = super().__new__(cls)
        return cls.instance
    
    def __init__(self):
       pass

db1 = Database()
db2 = Database()
db3 = Database()
print(db3 is db2)  # checking weather the instance for the class is same or different
