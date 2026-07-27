class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    def display(self):
        print("Name of the Student: ",self.name)
        print("Roll number: ",self.roll_no)
s=Student("Indu",1)
s.display()
setattr(s,"Department","CSE")
print("\nSet the new Attribute Department in Student class: ",s.Department)
print("\nHASATTR is used to check if cgpa is exist or not: ",hasattr(s,"cgpa"))
print("\nGETATTR is used to access default values(Name): ",getattr(s,"name"))
print("\nGETATTR is used to access default values(RollNumber): ",getattr(s,"roll_no"))
delattr(s,"name")
if hasattr(s,"name"):
    print("\nDelete the attribute(name): ",t.name)
else:
    print("\nThe attribute 'name' was successfully deleted and no longer exists.")

arr=[4,9,2,5,1,0,3,6]
print("\n\nOriginal list: ",arr)
print("\nSorted list: ",sorted(arr))
print("\nReversed list: ",sorted(arr,reverse=True))
    



