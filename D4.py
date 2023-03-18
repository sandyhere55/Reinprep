#Question 1
'''nearest_palindrome()... which accepts a number
and returns the nearest palindrome greater
than the given number
         Sample input    Expected output:
           99               101
           1221             1331
'''
#Answer 1
'''
import sys
def Next_Smallest_Palindrome(num):
    for i in range(num+1,sys.maxsize):  #100
        if str(i)==str(i)[::-1]:  #100=001  1==1 #0==0
            return i
print(Next_Smallest_Palindrome(99))
print(Next_Smallest_Palindrome(1221))
'''
#Answer 2
'''
def max_visited_speciality(patient_medical_speciality_list,
                           medical_speciality):
    max_visit=0
    P=patient_medical_speciality_list.count('P')
    E=patient_medical_speciality_list.count('E')
    O=patient_medical_speciality_list.count('O')
    if P>E and P>0:
        speciality= medical_speciality['P']
    elif E>0:
        speciality= medical_speciality['E']
    else:
        speciality= medical_speciality['O']
    return speciality
patient_medical_speciality_list=[101,'P',102,'P',302,'P',
                                 305,'P',401,'E',656,'E']
medical_speciality={'P':'Pediatrics','O':'Orthopedics','E':'ENT'}
speciality= max_visited_speciality(patient_medical_speciality_list,
                                   medical_speciality)
print(speciality)
'''

#Answer 3
'''s1=str("I like Python")
s2=str("Java is a very popular language")
a=list(set(s1)&set(s2))
for i in a:
    print(i)
'''

#What is the output of the below code snippet?
'''
class Example:
    def _init_(self,num):
        self.num=num
    def set_num(self,num):
        self.num=num
    def get_num(self):
        return self.num
obj=Example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())
'''

#What is the output of the below code snippet?
'''
class Example:
    def _init_(self,num):
        self.num=num
    def set_num(self,num):
        num=num
    def get_num(self):
        return self.num
obj=Example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())
'''

#Output?
'''
class Customer:
    def _init_(self):
        self.cust_id=100
c1=Customer()
print(c1.cust_id)
'''
'''
class Customer:   #Error 
    def _init_(self,id):
        id=100
c1=Customer()
print(c1.cid)
'''
'''
class Customer:
    def _init_(self,id):
        self.id=100
c1=Customer(200)
print(c1.id)
'''

#What is the output of the below code snippet?
'''
class Book:
    def _init_(self):
        self.title=None
my_fav=Book()
my_fav.title="Head First Programming"
your_fav=Book()
your_fav.title="Learn Python the way"
my_fav.title="Learning Python"
print("My favorite is",my_fav.title)
print("your's is",your_fav.title)
'''

#What would be the output if we print the reference variable?
'''
class Shoe:
    def _init_(self,price,material):
        self.price= price
        self.material= material
s1=Shoe(1000,"Canvas")
print("The unique id of the object",id(s1))
'''
'''
class Shoe:
    def _init_(self,price,material):
        self.price= price
        self.material= material
    def _str_(self):
        return "Shoe with price:"+ str(self.price)+" and material:" + self.material

s1=Shoe(1000,"Canvas")
print(s1)
'''
'''
class Mobile:
    def _init_(self):
        print(id(self))
    def display(self):
        print("Displaying details")
    def purchase(self):
        self.display()
        print("Calculating price")
#Mobile().purchase()
#Mobile().purchase()
m1=Mobile()
print(m1)
m2=Mobile()
print(m2)
m1=m2
print(m1)
print(m2)
'''
#
'''
class Mobile:
    def _init_(self,brand,price):
        self.brand= brand
        self.price= price
        self.total_price = None
    def purchase(self):
        if self.brand == "Apple":
            discount= 10
        else:
            discount = 5
        self.total_price = self.price - self.price * (discount/100)
        print("Total price of",self.brand,"mobile is",self.total_price)

mob1=Mobile("Apple",20000)
mob2=Mobile("Samsung",10000)
mob1.purchase()
mob2.purchase()
'''

#
'''
class Customer:
    def _init_(self,cust_id,name,age,wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance
    def set_balance(self,amount):
        if amount < 50000 and amount > 0:
            self.__wallet_balance += amount
    #def show_balance(self):
            #print("The balance is",self.__wallet_balance)
    def get_wallet_balance(self):
        return self.__wallet_balance
c1=Customer(100,"Aaru",25,1000)
print(c1.get_wallet_balance())
 c1.update_balance(500)
 c1.show_balance()
c1.get_wallet_balance
#print(c1._wallet_balance)..._wallet_balance gives error 
c1.set_balance(5000)
print(c1.get_wallet_balance())
'''
'''
class Dam:
    def _init_(self,name,length):
        self.name=name
        self.__length=length
    def get_length(self):
        return self.__length
dam1=Dam("ABC dam",3.5)
print("Dam name:",dam1.name)
print("dam Length",dam1.get_length())
'''

#What is the output?

class Table:
    def _init_(self):
        self.no_of_legs=4
        self.glass_top=None
        self.wooden_top=None
dining_table=Table()
back_table=Table()
front_table=back_table
back_table=dining_table
print(id(dining_table),id(back_table),id(front