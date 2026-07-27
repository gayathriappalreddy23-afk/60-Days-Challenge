arr=[3,9,1,4,7,5,8]
print("Initial data: ",arr)
print("Sorted data: ",sorted(arr))
print("Reversed data: ",sorted(arr,reverse=True))

#2
tuple1=(5,2,6,3,1,8)
print("\n\nInitial tuple: ",tuple1)
print("Reverse tuple: ",tuple(reversed(tuple1)))

#3
s="Python"
print("\n\nIsInstance of String: " ,isinstance(s,str))

#4
class Parent:
    def display():
        print("Parent Class")
class Child(Parent):
    def display():
        print("Child Class")
print("\n\nCheck the ISSUBCLASS: ",issubclass(Child,Parent))

#5
class Student:
    def __init__(self,name,age,Marks):
        self.name=name
        self.age=age
        self.Marks=Marks
    def display(self):
        self.name="Indu"
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Marks: ",self.Marks)
s=Student("Hema",12,89)
s.display()
print("\n\nHasAttr is check the class Attribute(Name) or not: ",hasattr(s,"name"))
print("\n\nHasAttr is check the class Attribute(Marks) or not: ",hasattr(s,"Marks"))
print("\n\nHasAttr is check the class Attribute(Department) or not: ",hasattr(s,"Department"))
print("\n\nHasAttr is check the class Attribute(Age) or not: ",hasattr(s,"age"))
#6
print("\n\nGetAttr in a class variables: ",getattr(s,"name"))
print("\n\nGetAttr in a class variables: ",getattr(s,"age"))
# print("\n\nGetAttr in a class variables: ",getattr(s,"Department"))
print("\n\nGetAttr in a class variables: ",getattr(s,"Marks"))
t=Student("Vani",15,90)
print("\n\nGetAttr in a class variables: ",getattr(t,"name"))
print("\n\nGetAttr in a class variables: ",getattr(t,"age"))
# print("\n\nGetAttr in a class variables: ",getattr(t,"Department"))
print("\n\nGetAttr in a class variables: ",getattr(t,"Marks"))

#7
setattr(t,"Department","CSE")
print("\n\nSETATTR is used to set the data: ",t.Department)
setattr(t,"name","Sisira")
print("\n\nSETATTR is used to set the data: ",t.name)
setattr(t,"age",5)
print("\n\nSETATTR is used to set the data: ",t.age)
setattr(t,"Marks",80)
print("\n\nSETATTR is used to set the data: ",t.Marks)
setattr(t,"name","Hasini")
print("\n\nSETATTR is used to set the data: ",t.name)
setattr(t,"Marks",70)
print("\n\nSETATTR is used to set the data: ",t.Marks)

#8
delattr(t, "age")

if hasattr(t, "age"):
    print("\n\nDelete the attribute(age): ", t.age)
else:
    print("\n\nThe attribute 'age' was successfully deleted and no longer exists.")
    
#9
expression="25*4"
print("\n\nResult using eval(Multiplication): ",eval(expression))
expression="12+3"
print("\n\nResult using eval(Addition): ",eval(expression))
expression="7-3"
print("\n\nResult using eval(Subtraction): ",eval(expression))
expression="64/2"
print("\n\nResult using eval(Division): ",eval(expression))

#10
print("\n\nEXEC using to excute a loop: ")
code="""
for i in range(1,11):
    if i&1==0:
        print(i)
"""
exec(code)




