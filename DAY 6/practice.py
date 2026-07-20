# Task
try:
    with open("Student.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Error: Student.txt does not exist yet.")

# Fix for overwriting/writing cleanly (#6)
with open("Student.txt", "w") as file:
    file.write("Departments\n CSE \n EEE \n CSM \n IT \n CSD\n")

# Fix for appending safely (#3)
with open("Student.txt", "a") as file:
    file.write("Thank You\n")

# Fix for reading list cleanly with try-except (#7 & #8)
try:
    with open("Student.txt", "r") as file:
        students_list = file.readlines()  # This populates the variable safely
        
        for index, student in enumerate(students_list, start=1):
            print(f"{index}. {student.strip()}")
except FileNotFoundError:
    print("Error: Could not read file because it doesn't exist.")


#1 Task
file=open("Student.txt","r")
print(file.read())
#file.close()

#2
file=open("Student.txt","w")
file.write("\nHello Everyone")

#3
file=open("Student.txt","a")
file.write("\nThank You")


#4
with open("Student.txt","r") as file:
    print(file.readline())
    
#5
file=open("New.txt","x")

#6
file=open("Student.txt","w")
file.write("Departments\n CSE \n EEE \n CSM \n IT \n CSD")

#7
file=open("Student.txt","r")
print(file.readlines())

#8 
try:
    for index, student in enumerate(students, start=1):
                print(f"{index}. {student.strip()}")
except FileNotFoundError:
    print(f"Error The file '{FILE_NAME}' does not exist")

