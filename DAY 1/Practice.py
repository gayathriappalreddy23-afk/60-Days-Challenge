from collections import Counter,defaultdict,deque,namedtuple
data=[9,3,4,7,1,7,8,2,9,4,3]
count=Counter(data)
print(count)
print(count.most_common(2))
print(count.elements())

#1.2
text = "placement"

count = Counter(text)

print(count.most_common(1))

#2
d=defaultdict(list)
d["python"].append("Easy")
print(d)

#3
dq=deque()
dq.append(10)
dq.append(20)
dq.append(30)
print("Original deque: ",dq)
dq.popleft()
print("After Popleft:",dq)
dq.pop()
print("After Pop:",dq)

#4
St=namedtuple("Student",["Name","Age","Branch"])
s=St("Gayathri",1,"CSE")
print(s)
print(s.Name)

#Practice

print("*******Practice 1*********")
ch="hello Everyone"
count=Counter(ch)
print("Counting in each Character: ",count)
print("Most common 3 characters: ",count.most_common(3))
v=['a','e','i','o','u']
for i in count:
    if count in v:
        print(count)

de=deque()
de.append(8)
de.append(4)
de.append(3)
print("Original deque: ",de)
print("Reverse deque: ",de.reverse())

data=defaultdict(list)
data["CSE"].append("Gayathri")
data["CSE"].append("Indu")
data["CSR"].append("Siri")
print(data)
                   
Book=namedtuple("Book",["Name Of the Book", "Author"])
b=Book("Python Programming","Guido Vandro sum")
print(b)






















