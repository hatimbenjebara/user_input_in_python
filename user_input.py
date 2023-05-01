username= input("enter username :")
print("username is : "+ username)
class person: 
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduction(self):
        print(f"hello, my name is {self.name} and i am {self.age} years old.")
class client(person):
    def __init__(self, name, age, address):
        super().__init__(name, age)
        self.address = address
    def introduction (self):
           print(f"hello dear client Ms{self.name}, you have {self.age} years old ago and you are living in {self.address}") 
client_1= client("hatim benjebara", 35, "8 avenue des FAR")
client_1.introduction()
#input information
input_name = input("give me the name :")
input_age = int(input("give me the age: "))
input_address = input("give me the address :" )
clien_2 = client(input_name, input_age, input_address)
clien_2.introduction()

