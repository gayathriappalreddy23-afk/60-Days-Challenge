#Functional Programming in Python
#lambda, map(), filter(), zip(), enumerate(), any(), all()

#1 Task
lambda_result=lambda x:x*x
print("Square of a number 5 :",lambda_result(5))

#2 Task
arr=[1,2,3,4]
Map_result=list(map(lambda x:x*x,arr))
print("\n\nSquare of an list values :",Map_result)

#3 Task
arr=[1,2,3,4,5,6]
filter_result=list(filter(lambda x:x%2==0,arr))
print("\n\nEven Numbers :",filter_result)

#4 Task
Names=["Indu","Siri","Hema","Sita"]
Marks=[90,89,34,78]
Departments=["CSE","IT","EEE","CSM"]
zip_result=list(zip(Names,Marks,Departments))
print("\n\nZip the Names, Marks , and Department :",zip_result)

#5 Task
arr=[9,8,7,6,5]
print("\n\n")
for index,value in enumerate(arr):
    print("Index: ",index,"Value: ",value)

#6 Task
arr=[0,3,0,0,0]
print("\n\nThe result in any function using list[0,3,0,0,0]: ",any(arr))
arr1=[0,0,0,0]
print("The result in any function using list[0,0,0,0]: ",any(arr1))
arr2=[0,-9,0,0,0]
print("The result in any function using list[0,-9,0,0,0]: ",any(arr2))

#7 Task
arr2=[4,-9,8,2,1]
print("\n\nThe result in 'all' function using list[4,-9,8,2,1]: ",all(arr2))
arr=[0,3,0,0,0]
print("The result in 'all' function using list[0,3,0,0,0]: ",all(arr))
arr1=[0,0,0,0]
print("The result in 'all' function using list[0,0,0,0]: ",all(arr1))
arr2=[0,-9,0,0,0]
print("The result in 'all' function using list[0,-9,0,0,0]: ",all(arr2))

