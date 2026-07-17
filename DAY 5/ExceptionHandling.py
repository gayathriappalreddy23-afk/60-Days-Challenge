try:
    a=10
    b=0
    result=a/b
    print("Result : ",result)
except ZeroDivisionError:
    print("Error: Number Cannot divide by zero.")

#2
try:
   age=int(input("\n\nEnter your age: "))
   print("My age is: ",age)
except ValueError:
    print("Error: Please enter a valid integer number")
    
#3
try:
   arr=[1,2,3,4,5]
   print("\n\nArray index 6:",arr[6])
except IndexError:
    print("\n\nError: Index Out Of range")

#4
try:
   user={
       "Name":"Indu",
       "Age":18
       }
   print(user["Marks"])
except KeyError:
    print("\n\nError: The specific key not found in the dictionary.")

#5
try:
   a=10
   b=2
   print("Result of data:",a*b)
except ZeroDivisionError:
    print("\n\nZero Division Error")
else:
    print("Else Block: Runs because no exception Occured.")
finally:
    print("Finally Block: Always runs no matter.")

#6
try:
   age=4
   if age<0:
       raise ValueError("Age Cannot be negative.")
    
except ValueError as e:
    print("\n\nCaught an error: ",e)

#7
class InvalidSalaryError(Exception):
    pass
try:
   salary=20000
   if salary<0:
       raise InvalidSalaryError("Salry Cannot be less than 0.")
    #print("Salary accepted : ",salary)
except InvalidSalaryError as e:
    print("\n\nCustom Error Triggered: ",e)

#8
balance=9000
try:
   print("\n\nCurrent Balance: ",balance)
   withdraw=460
   if withdraw<=0:
       raise ValueError("Withdrawal amount must be greater than zero.")
    
    #if withdraw>balance:
       # raise ValueError("Insufficient funds in your account.")

    #balance-=withdraw
    #print(f"Withdrawal successful! Remaining balance: {balance}")
   
except ValueError as e:
    print("Input Error: ",e)
except RuntimeError as e:
    print("Transaction Error: ",e)
finally:
    print("\nThank you for using our ATM.")
