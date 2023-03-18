'''
#Python  programming

#Datatypes

name="Mukeshini"
print("name",name,type(name))
rollno=12
print("rollno",rollno,type(rollno))

#Decision making statements
#read a number
#multiple 3
#multiple 5
#multiple 3 and 5
#else print invalid

number=int(input("Enter an integer number"))
print(number,type(number))
if number%3==0 and number%5==0:
    print("Its a multiple of 3 and 5")
elif number%5==0:
    print("Its a multiple of 5")
elif number%3==0:
    print("Its a multiple of 3")
else:
    print("Invalid")
'''

'''
#print(*no of Objects,sep=' ',endend='\n')
#for loop
#range function

#1 to 100
for i in range(1,101):
    #range(start,end,step)
    print(i,end=' ')
print()

#100 to 1
for i in range(100,0,-1):
    #range(start,end,step)
    print(i,end=' ')
print(i)

#odd number between 1 to 100
for i in range(1,101,2):
    #range(start,end,step)
    print(i,end=' ')
print()

#99 97 ...
for i in range(99,0,-2):
        print(i,end=' ')
print()

#even number between 1 to 100
for i in range(2,101,2):
    #range(start,end,step)
    print(i,end=' ')
print()

#100 98 96...2
for i in range(100,1,-2):
    print(i,end=' ')
print()

'''

'''
#break
for i in range(1,101):
    '''   ''' if i==50:
        break   '''  '''
    print(i,end=" ")
else:
    print("else statement")

'''

'''  
#continue
for i in range(1,101):
    if i==50:
        continue
    print(i,end=" ")
for i in range(1,101):
    if i==50:
        pass
    #likewise in null statement in other languages pass is used in python,unlike to go to an empty statement pass keyword is used
    print(i,end=" ")


'''

'''
#functions
def function1():
    print("its a function1")
function1()
def function2(num1,num2):
    print("num1",num1,"num2",num2)
    #print()_str_
function2(10,20)
def function3(num1,num2):
    num3=num1+num2
    return num3
print("value returned",function3(100,200))
def function4(num1,num2):
    num3=num1+num2
    return num3
print("value returned",function4(10,20.2))
def function5(num1,num2):
    num3=float(num1)+num2
    return num3
print("value returned",function5('10',20.2))

'''

'''
#categories of functions
#based on arguments

#1:positional arguments
def function1(num1,num2,num3,num4):
    print("num1",num1,"num2",num2,"num3",num3,"num4",num4)
function1(10,20,30,40)
function1(100,"200",300,400)

#2 Keyword Arguments

def function2(num1,num2,num3,num4):
    print("num1",num1,"num2",num2,"num3",num3,"num4",num4)
function2(num4=10,num1=20,num2=30,num3=40)
function2(num4=10,num1=10,num2=30,num3=40)


#3 Default Arguments
def function3(name,rollno,branch="CSE",collegename="GIET"):
    print(name,rollno,branch,collegename)
function3("Potti",11,"CSE")
function3("Babu",12,"CSE")
function3("Kanha",13)
function3("Aaru",14,"ECE")


#4 Variable no. of argumnents
def function4(*var):#tuple=
    for i in var:
        print(i,end=' ')


function4(10,20)
print()
function4(10,20,30,40)
print()
function4(10,20,30,40,50,60)
print()

def add(*var):#tuple=
    sum1=0
    for i in var:#10,20
        sum1=sum1+i
    return(sum1)
print(add(10,20))
print(add(10,20,30,40))
print(add(10,20,30,40,50,60))

'''

'''
#Answer 1

num1=int(input())
num2=int(input())
num3=int(input())
if num1==7:
    print(num2*num3)
elif num2==7:
    print(num3)
elif num3==7:
    print(-1)
else:
    print(num1*num2*num3)

'''

'''

#Answer 2

def currencycal(AmountINR,curr):
    if curr=="Euro":
        print(AmountINR*0.01417)
    elif curr=="British Pound":
        print(AmountINR*0.0100)
    elif curr=="Australian Dollar":
        print(AmountINR*0.02140)
    elif curr=="Canadian Dollar":
        print(AmountINR*0.02027)
    else:
        print(-1)
currencycal(300,"Euro")
currencycal(300,"British Pound")
currencycal(300,"Australian Dollar")
currencycal(300,"Canadian Dollar")

'''

'''

#Answer 3

n_adults=int(input("Enter the number of adults"))
n_childs=int(input("Enter the number of childs"))
print((((n_adults*37550.0)+(n_childs*37550.0/3))*1.07)*0.90)


"""total=((n_adults*37550.0)+(n_childs*37550.0/3))
print(total)
total1=total*0.07
total2=total+total1
print("With ur service tax",total2)
total_amount=total2*0.90
print(total_amount)"""


'''