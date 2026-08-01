from collections import Counter
text="HappyDays"
count=Counter(text)
print("original text: ",text)
print("Counter used in text: ")
print(count)
print(count.most_common(2))
print(list(count.elements()))

#2
from collections import namedtuple
students=namedtuple("Student",["Name","Age","Branch","Section"])
s=students("Vani",19,"CSE","A")
print("\n\nNamedTuple used in Collections: ")
print(s)
print(s.Name)
print(s.Age)
print(s.Branch)
print(s.Section)
s=students("Hema",21,"EEE","B")
print(s)
print(s.Name)
print(s.Age)
print(s.Branch)
print(s.Section)

#3
from collections import defaultdict
Student=defaultdict(list)
Student["CSE"].append("Gayathri")
Student["EEE"].append("Honey")
print("\n\nDefaultDict is used in collections: ")
print(Student)
print(Student["CSE"])
print(Student["EEE"])
Student["IT"].append("Hasini")
Student["CSE"].insert(1,"Swetha")
print(Student)
print(Student["CSE"])
Student["IT"].insert(3,"Keerthi")
print(Student)
print(Student["IT"])
print(Student["EEE"])

4
from collections import deque
dq=deque()
dq.append(10)
dq.append(20)
print("\n\nDeque is used in Collections: ")
print(dq)
dq.appendleft(90)
print(dq)
dq.pop()
print("Pop the deque: ",dq)
dq.append(40)
dq.append(60)
print(dq)

#5
from collections import defaultdict
city_groups=defaultdict(list)
transactions = [
    {"city": "Mumbai", "amount": 500},
    {"city": "Delhi", "amount": 300},
    {"city": "Mumbai", "amount": 150},
]
for txn in transactions:
    city_groups[txn["city"]].append(txn["amount"])
print("\n\nTransaction data using defaultdict is :")
print(dict(city_groups))

#output
original text:  HappyDays
Counter used in text: 
Counter({'a': 2, 'p': 2, 'y': 2, 'H': 1, 'D': 1, 's': 1})
[('a', 2), ('p', 2)]
['H', 'a', 'a', 'p', 'p', 'y', 'y', 'D', 's']


NamedTuple used in Collections: 
Student(Name='Vani', Age=19, Branch='CSE', Section='A')
Vani
19
CSE
A
Student(Name='Hema', Age=21, Branch='EEE', Section='B')
Hema
21
EEE
B


DefaultDict is used in collections: 
defaultdict(<class 'list'>, {'CSE': ['Gayathri'], 'EEE': ['Honey']})
['Gayathri']
['Honey']
defaultdict(<class 'list'>, {'CSE': ['Gayathri', 'Swetha'], 'EEE': ['Honey'], 'IT': ['Hasini']})
['Gayathri', 'Swetha']
defaultdict(<class 'list'>, {'CSE': ['Gayathri', 'Swetha'], 'EEE': ['Honey'], 'IT': ['Hasini', 'Keerthi']})
['Hasini', 'Keerthi']
['Honey']


Deque is used in Collections: 
deque([10, 20])
deque([90, 10, 20])
Pop the deque:  deque([90, 10])
deque([90, 10, 40, 60])


Transaction data using defaultdict is :
{'Mumbai': [500, 150], 'Delhi': [300]}

=== Code Execution Successful ===
















