
try:
    a=10
    b=0
    result=a/b
    print("Result: ",result)
except ZeroDivisionError:
    print("Error:Number cannot divisible by Zero")
finally:
    print("Program executed Successfully in ZeroDivisionError")
    
#ValueError
try:
    number=int(input("\n\nEnter a value: "))
    print("Number is:",number)
except ValueError:
    print("Error: Please enter a valid integer.")
finally:
    print("Program executed Successfully in ValueError")

#3    
try:
    num = int(input("\n\nEnter a number:"))
    print("Result: ",10 / num)
except ValueError:
    print("Invalid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
    
#4
try:
    num=int(input("\n\nEnter any interger: "))
except ValueError:
    print("Invalid input")
else:
    print("You entered : ",num)
    
#5
try:
    file=open("student.txt")
except FileNotFoundError:
    print("\n\nFilen Not Found")
finally:
    print("Program Finished.")

#6
try:
    age=15
    if age<18:
        raise ValueError("Age must be 18 or above.")
except ValueError as e:
    print("\n\nError: ",e)
    

#7  
class InvalidAgeError(Exception):
    pass

age = 15
try:
    if age < 18:
        raise InvalidAgeError("Not eligible to vote.") 
except InvalidAgeError as e:
    print("\n\nCustom Error Handled:", e)
    
#8
try:
    items=[4,2,5]
    print(items)
    print(items[4])
except IndexError:
    print("\n\nError: List Index out of the bound range.")
    
#9
try:
    a=10
    print(b)
except NameError:
    print("\n\nError: Variable 'b' is not defined.")

#10
try:
    a="Hello"
    b=5
    print(a+b)
except TypeError:
    print("\n\nError: Cannot add string to integer")

#11
try:
    data={'Hello':3,'Welcome':4,"world":1}
    print(data["Happy"])
except KeyError:
    print("\n\nError: Dictionary key not found")
    
#12
try:
    balance=20000
    print("\n\nCheck balance: ",balance)
    deposit=400
    print("Deposit amount: ",deposit)
    total=balance+deposit
    print("Total amount: ",total)
    withdraw=90000
    if withdraw>total:
        raise ValueError("Withdraw amount is greater than actual balance amount")
except ValueError:
    print("Error: Withdraw amount is greater than actual balance amount")
finally:
    print("Thank you for using our ATM.")
        
#13
try:
    balance = 20000
    print(f"\n\nCurrent Balance: ₹{balance}")
    
    deposit = int(input("Enter deposit amount: "))
    if deposit < 0:
        raise ValueError("Deposit amount cannot be negative.")
        
    print(f"Deposit amount: ₹{deposit}")
    total = balance + deposit
    print(f"Total available amount: ₹{total}")
    
    withdraw = int(input("Enter withdrawal amount: "))
    if withdraw < 0:
        raise ValueError("Withdrawal amount cannot be negative.")
    if withdraw > total:
        raise ValueError("Withdrawal amount is greater than actual balance amount.")
        
    total -= withdraw
    print(f"Withdrawal successful! Remaining balance: ₹{total}")

except ValueError as e:
    print(f"Transaction Error: {e}")

finally:
    print("Thank you for using our ATM.")

#output
  
ERROR!
Error:Number cannot divisible by Zero
Program executed Successfully in ZeroDivisionError


Enter a value: 21
Number is: 21
Program executed Successfully in ValueError


Enter a number:Hello
Invalid number.


Enter any interger: Welcome
ERROR!
Invalid input


Filen Not Found
Program Finished.


Error:  Age must be 18 or above.


Custom Error Handled: Not eligible to vote.
[4, 2, 5]


Error: List Index out of the bound range.
0


Error: Cannot add string to integer
ERROR!


Error: Dictionary key not found


Check balance:  20000
Deposit amount:  400
Total amount:  20400
Error: Withdraw amount is greater than actual balance amount
Thank you for using our ATM.


Current Balance: ₹20000
Enter deposit amount: 890
Deposit amount: ₹890
Total available amount: ₹20890
Enter withdrawal amount: 900000
ERROR!
Transaction Error: Withdrawal amount is greater than actual balance amount.
Thank you for using our ATM.
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    2
