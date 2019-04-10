#ibrahim alakeel

class employee():
    def employer(self,name):
        print("your name is : ",name)
    def work_days(self,days):
        print("your work days (day 8 hours work) are : ",days , "days")
    def money_per_hour(self,money):
        print("Your money per hour are : ",money , "$")
    def salary(self,days,money):
        print("Your salary of ", days ," days work is : ",(days*money), "$")



#name = input("Enter your name : ")
#work_days = input("Enter your work_days (day 8 hours work) : ")
#money_per_hour = input("Enter the cost of one hour : ")

e = employee()
e.employer("ibrahim")
e.work_days(12)
e.money_per_hour(50)
e.salary(12,50)





####
