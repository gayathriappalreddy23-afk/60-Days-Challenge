import re
str="Education"
str=str.lower()

#1 Task

count=0
for i in str:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        count+=1
        
print(count)

#2 Task

count=sum(1 for i in str if i in "aeiou")
print(count)

#3 Task

res=sum(str.count(v) for v in ("aeiou"))
print(res)

#4 Task
count=len(re.findall(r'[aeiou]',str))
print(count)

#5 Task
count=sum(map(lambda x:x in 'aeiou',str))
print(count)

#6
from collections import Counter
def NonRepeat(s):
    res=Counter(s)
    print(res)
    for k,v in res.items():
        if v==1:
            return k

str="leetcode"
print(NonRepeat(str))  


#7
def NonRepeat(s):
    data={}
    for i in s:
        data[i]=data.get(i,0)+1
    print(data)
    for k,v in data.items():
        if v==1:
            return k

str="leetcode"
print(NonRepeat(str))

#8

def NonRepeat(s):
    unique=filter(lambda c:s.find(c)==s.rfind(c),s)
    return next(unique,None)

str="leetcode"
print(NonRepeat(str))

#9

students = [
    {"name":"Ram","marks":80},
    {"name":"Hari","marks":92},
    {"name":"Sai","marks":65},
    {"name":"Anu","marks":98}
]
highscore=[s for s in students if s["marks"]>90]
print(highscore)

marks=[s["marks"] for s in students]
avg=sum(marks)/len(students)
print(avg)

Topper=max(students,key=lambda x:x["marks"])
print("Topper Name: ",Topper["name"])

Arrange=sorted(students,key=lambda x:x["marks"],reverse=True)
print("Sorted data list: ",Arrange)

    
    





