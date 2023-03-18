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
'''
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
#for loop -->odd-->square it
#even -->cube it
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
#List comprehension
print([ele*2 if ele%2!=0 else ele*3
       for row in mat for ele in row])
print([[ele*2 if ele%2!=0 else ele*3 for ele in row]
       for row in mat])
'''

# Answer 1
'''
mylist= [9, 3, 6, 1, 5, 0, 8, 2, 4, 7]
list_b= [6, 4, 6, 1, 2, 2]
dict={}
for i in list_b:
    dict[i]=mylist.index(i)
print(dict)
result=[]
for i in list_b:
    result.append((i,mylist.index(i)))
print(result)
print([(i,mylist.index(i))for i in list_b])
'''
# Answer 2
'''
sentences=["a new world record was set",
           "in the holy city of ayodhya",
           "on the eve of diwali on tuesday",
           "with over 3 lakh diya or earthen lamps",
           "lit up simultaneously on the banks of sarayu river"]
stopwords=['for','a','of','the','and','to','in','on','with','was']
result=[]
for sentence in sentences:#"a new world record was set"
    row_data=[]
    for word in sentence.split():
        if word not in stopwords:
            row_data.append(word) #new world record set
    result.append(row_data)
print(result)
print([[word for word in sentence.split() if word not in stopwords]
       for sentence in sentences])
'''
# Answer 3

'''s=list(map(int,input().split(',')))
print(sum(s[:s.index(5)])+sum(s[s.index(8)+1:]))'''

'''
array=list(map(int,input().split(","))) #3,2,6,5,1,4,8,9
num1=sum(array[:array.index(5)])+sum(array[array.index(8)+1:])
print(num1)
l=array[array.index(5):array.index(8)+1]
#print(l)
num2=""
for i in l:
    num2+=str(i)
#print(num2)
print(int(num2)+num1)
'''

# Answer 4

s = input().split(",")  # rhdt:246,ghftd:1246
stt = []
numm = []
for i in s:
    s1, n = i.split(":")
    stt.append(s1)  # stt=[rhdt,ghftd]
    numm.append(n)  # numm=[246,1246]


def rotate(ss, n):  # ss=rhdt,n=246
    n = str👎
    s = 0
    for i in n:
        s += int(i) ** 2
    if s % 2 == 0:
        return ss[-1] + ss[:-1]  # rhdt trhqd
    else:
        return ss[2:] + ss[:2]  # ghftd ftdgh


for i in range(len(numm)):  # i=0
    print(rotate(stt[i], numm[i]))