import csv
with open(r"C:\Users\Cloud Analogy\Desktop\Learning\60DaysPython\students.csv","r") as file:
    reader =csv.reader(file)
    for row in reader:
        print(row)
        

#2
with open("students.csv","w",newline="") as file:
    writer=csv.writer(file)
    writer.writerow(["Name","Age","Branch"])
    writer.writerow(["Keerthi",21,"EEE"])

#3
with open("students.csv","r") as file:
    reader=csv.DictReader(file)

    for row in reader:
        print(row["Name"],row["Branch"])

#4

import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["Name", "Age", "Branch"]
    )

    writer.writeheader()

    writer.writerow({
        "Name": "Gayathri",
        "Age": 21,
        "Branch": "CSE"
    })

#5
import json

student = {
    "name": "Gayathri",
    "age": 21
}

print(json.dumps(student))

#6
import json

text = '{"name":"Gayathri","age":21}'

print(json.loads(text))

#7
import json

student = {
    "name": "Gayathri",
    "age": 21
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

#8
import json

with open("student.json", "r") as file:
    data = json.load(file)

print(data)  
