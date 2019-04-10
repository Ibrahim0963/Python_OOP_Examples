# A simple class make in python
# Ibrahim alakeel

class infos():
    def __init__(self,name, lastname, age, address, sex):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.address = address
        self.sex = sex

    def ib_yname(self):
        print("Your name is : ",self.name)
    def ib_ylastname(self):
        print("Your lastname is : ", self.lastname)
    def ib_yage(self):
        print("Your age is : ", self.age)
    def ib_yaddress(self):
        print("Your address is : ", self.address)

class infos2(infos):
    def ib_ysex(self):
        print("Your sex is : ", self.sex)



        
name = input("*Enter your name :")
while name == "":
    print("Your name is required !!!!")
    name = input("Enter your name :")
    
lastname = input("*Enter your lastname :")
while lastname == "":
    print("Your lastname is required !!!!")
    lastname = input("Enter your lastname :")
    
age = input("Enter your age :")
address = input("Enter your address :")
sex = input("Enter your sex :")


i = infos2(name,lastname,age=None,address=None,sex=None)
print("\n\nYour infos here :\n")
i.ib_yname()
i.ib_ylastname()
i.ib_yage()
i.ib_yaddress()
i.ib_ysex()




#
