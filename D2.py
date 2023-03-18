# list-->Ordered--default index

'''
list1=[]
print(list1,type(list1))
list2=[10,20,30,40]
print(list2,type(list2))
list3=[10,20.2,30+3j,True,"Python"]
print(list3,type(list3))
list4=list([100,200,300,400])
print(list4,type(list4))
list5=[101,201,301,401]
print(list5,type(list5))
list5.append(501)
print(list5,type(list5))
list5.extend([601,701,801])
print(list5,type(list5))
list5.insert(0,51) #index,value
print(list5,type(list5))
list5.insert(4,350) #index,value
print(list5,type(list5))
list5.remove(801)
print(list5,type(list5))
list5.pop()
print(list5,type(list5))
list5.pop(0)
print(list5,type(list5))
del list5[1]
print(list5,type(list5))

'''

# Answer 1

'''
def function(str1):
    l_count=0
    d_count=0
    for i in str1:
        if i.isalpha():
            l_count=l_count+1
        elif i.isdigit():
            d_count=d_count+1
        else:
                continue
    return[l_count,d_count]
print(function("Infosys 123"))
print(function("ABCDE"))


'''

# Answer 2
'''
def find_pairs_of_numbers(num_list,n):
    count=0
    for x in num_list:  #[1,2,7,4,5,6,0,3]
        index=num_list.index(x)+1 #index=1
        for y in range(index,len(num_list)): #1,7
            if x+num_list[y]==n:
                count+=1  #count=1
    return count
num_list=[1,2,7,4,5,6,0,3]
n=6
print(find_pairs_of_numbers(num_list,n))


'''

# Answer 3
'''
def function1(str1):
    if len(str1)<2:
        return -1
    else:
        return str1[0:2]+str1[-2:]
print(function1("W3Resource"))
print(function1("W3"))
print(function1("A"))

'''

# Answer 4
'''
def add_string(str1):    #str1=string
    length=len(str1)     #6
    if length>2:        #str i n g
        if str1[-3:]== 'ing':   #-3 -2 -1
            str1 += 'ly'      #string+ly=stringly
        else:
            str1 += 'ing'   #sleep+ing=sleeping
    return str1  
print(add_string('sleep'))  #sleeping
print(add_string('is'))  #is
print(add_string('string'))  #stringly

'''
# Answer 5
'''
a=int(input())
b=a*2
res=list(map(int,str(a)))
res1=list(map(int,str(b)))
if(sorted(res)==sorted(res1)):
    print("True")
else:
    print("False")

'''
'''
def check_double(number):   #125874
    num1=str(number*2)   #251748
    number=str(number)    #125874
    count=0
    for x in number: #125874
        if x in num1: #251748
            count+=1   #count=1
        else:
            return False

    if count==len(number):
        return True
print(check_double(245))
print(check_double(125874))

'''
# Answer 6

'''
def find_more_than_average(tup):
    average=sum(tup)/len(tup)
    count=0
    for i in tup:
        if(i>average):
            count+=1
    print(count*10)

def generate_freq(tup):
    l=[]
    for i in range(0,26):
        l.append(tup.count(i))
    print(l)

def sort_marks(tup):
    print(sorted(list(tup)))

tup=tuple(map(int,input().split()))
find_more_than_average(tup)
generate_freq(tup)
sort_marks(tup)

'''
# Answer 7

'''
wishes={"Merry":"God",
        "Christmas":"Jul",
        "And":"Och",
        "Happy":"Gott",
        "New":"Nytt",
        "Year":"Ar"}
print(wishes["Merry"],wishes["Christmas"])
print(wishes["Happy"],wishes["New"],wishes["Year"])

'''
'''
def translate(dict1,list1):
    list2=[]
    for i in list1: #"Merry"
        list2.append(dict1[i])
    return list2
dict1={"Merry":"God",
        "Christmas":"Jul",
        "And":"Och",
        "Happy":"Gott",
        "New":"Nytt",
        "Year":"Ar"}
list1=["Merry","Christmas"]
list2=["New","Year"]
print(translate(dict1,list1))
print(translate(dict1,list2))

'''
# Answer 8
'''
n1=int(input("Enter n1:"))
n2=int(input("Enter n2:"))
result=[]
for i in range(n1,n2+1):  #1,4-->1 2 3
    result.append(i)
print(result)
result=[i for i in range(n1,n2+1)]
print(result)
array=[i for i in range(n1,n2+1)]
print(array) #[1,2,3]

result=[]
for i in range(len(array)): #i=0
    for j in range(i,len(array)): #i=0,1,2
        result.append(array[i:j+1]) #[0:1]=[1],
print(result)                      #[0:2]=[1,2]
l1=[array[i:j+1] for i in range(len(array)) for j in range(i,len(array))]
print(l1)
c=0
for i in l1: #[[1],[1,2],[1,2,3],[2],[2,3],[3]]
    if sum(i)%2!=0:
        c+=1 #c=4
print(c)
'''
'''
result=[]
for i in range(n1,n2+1): #1,4-->1 2 3
    result.append(i)
print(result)
'''

'''
-----------
#List Comprehension version

#for loop version -->odd elements
#l1=int(input())
result=[]
for i in range(l1): #
    if i%2!=0:
        result.append(i)
print(result)
print([i for i in range(l1)if i%2!=0])

#for loop version-->even elements
result=[]
for i in range(11): #
    if i%2==0:
        result.append(i)
print(result)
print([i if i%2!=0 else i**2 for i in range(11)])


for i in range(l1):
    if i%2!=0:
        result.append(i)
    else:
        result.append(i**2)
print(result)
print([i if i%2!=0 else i**2 for i in range ([l1])])
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
#for loop -->odd-->square it
#even -->cube it

l1=int(input())
print([i**2 if i%2!=0 else i*i*i for i in range([l1])])
-----------
'''
# list comprehension
'''
#for loop version
result=[]
for i in range (11):
    result.append(i)
print(result)

#list comprehension version
print([i for i in range(11)])
#for loop version --->odd elements
result=[]
for i in range(11):
    if i%2!=0:
        result.append(i)
print(result)
print([i for i in range(11)if i%2!=0])

#for loop version --->even elements
result=[]
for i in range(11):
    if i%2!=0:
        result.append(i)
    else:
        result.append(i**2)
print(result)
print([i if i%2!=0 else i**2 for i in range(11)])
'''

mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# for loop -->odd-->square it
# even -->cube it
'''
result=[]
for row in mat:
    for ele in row:
        row_data=[]
        if ele%2!=0:
            row_data.append(ele**2)
        else:
            row_data.append(ele**3)
    result.append(row_data)
print(result)
'''
# List comprehension
print([ele * 2 if ele % 2 != 0 else ele * 3
       for row in mat for ele in row])
print([[ele * 2 if ele % 2 != 0 else ele * 3 for ele in row]
       for row in mat])