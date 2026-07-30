import re
email="Student123@gmail.com"
result=r"\w+@gmail\.com"
print(re.match(result,email))

pattern=r"^[\w\.-]+@[\w]\.\w$"
result2=re.match(pattern,email)
print("\nCheck the mail:","Matching email" if result2 else "Not Match")

phoneNo="9234678991"
pattern2=r"\d{10}"
result3=re.fullmatch(pattern2,phoneNo)
print("\n\nPhone Number Validation(",phoneNo,"): "
,"Valid" if result3 else "Not Valid")
phoneNo2="9234671"
result4=re.fullmatch(pattern2,phoneNo2)
print("\n\nPhone Number Validation(",phoneNo2,"): "
,"Valid" if result4 else "Not Valid")

print("\n\nExtract Numbers:")
text = "Order 123 Amount 450"
print("Normal text: ",text)
print("Only Numbers: ")
print(re.findall(r"\d+",text))

text="Python is used to learn easy and simple syntax."
result5=re.match("Python",text)
print("\n\nStart at text(",result5.group(),")->","Match" if result5 else "Not Match")
result8=re.match("simple",text)
print("\n\nStart at text(simple)->","Match" if result8 else "Not Match")

result6=re.search("learn",text)
print("\n\nSearch at text(",result6.group(),")->","Match" if result6 else "Not Match")
result7=re.search("Developer",text)
print("\n\nSearch at text(Developer)->","Match" if result7 else "Not Match")

text3="Age 21 Roll 105 Marks 98"
print("\n\nOriginal Text:",text3)
print("All Numbers in a text: ",re.findall(r"\d+",text3))

text4="I learn Java"
print("\n\nReplace the text:")
print("Before text: ",text4)
print("After text: ",re.sub("Java","Python",text4))

text5="HTML,CSS,JS,Python"
print("\n\nSplit the text: ",re.split(",",text5))

text6="Python is a programming language. Processing packages perform many tasks perfectly in real time"
result8=re.findall(r"\b[pP]\w+",text6)
print("\n\nFindall start with word: ")
for i in result8:
    print(i)

print("\nWord Starting at p after split applying the original data:")
words=re.split("\W+",text6)
for word in words:
    if re.match(r"^[pP]",word):
        print(word)
text = "WELCOME to the Python workshop. ERROR codes 404 and 500 were found in the LOG file."
uppercase_words=re.findall(r"\b[A-Z]+\b",text)
print("\n\nUppercase words found:", uppercase_words)

sentence = "The team scored 42 points in game 1 and 57 points in game 2."
No_Of_Digits=re.findall(r"\d+",sentence)
print("\n\nThe Digits in a Sentence: ",No_Of_Digits)
print("Total No.of Count: ",len(No_Of_Digits))

print("\n\n=== STUDENT REGISTRATION VALIDATOR ===")

print("\n\n--- 1. Email Validation ---")
email_input="Student342@university.edu"
email_pattern=r"^[\w\.-]+@\w+\.\w+$"
is_email_valid=re.match(email_pattern,email_input)
print("User Email: ",email_input)
print("Email validataion: ","Valid" if is_email_valid else "invalid")

print("\n\n--- 2. Mobile Number Validation ---")
mobile_input = "9876543210"
mobile_pattern=r"\d{10}"
is_mobile_valid=re.fullmatch(mobile_pattern,mobile_input)
print("Mobile Number: ",mobile_input)
print("Mobile Validation: ","Valid Number" if is_mobile_valid else "Invalid Number")

print("\n\n--- 3. Roll Number Extraction ---")
sentence = "The admission desk assigned Roll No: CS2026105 to the new candidate."
roll_pattern =r"\b[A-Za-z0-9]{5,12}\b"
extracted_roll=re.search(roll_pattern,sentence)
print("Source Sentence: ",sentence)
print("Extracted Roll Number: ", extracted_roll.group() if extracted_roll else "Not Found")

print("\n\n--- 4. Status Update (Replace Fail with Pass) ---")
result_string = "Final Status: Fail in Mathematics, Fail in Physics"
updated_status =re.sub(r"\bFail\b","Pass",result_string)
print("Original Record:", result_string)
print("Updated Record :", updated_status)

print("\n\n--- 5. Subject List Parsing ---")
subject_data = "Mathematics,Physics,Chemistry,Computer Science,English"
parsed_subjects =re.split(",",subject_data)
print("Raw Subject Data:", subject_data)
print("Parsed Array List:")
for index,subject in enumerate(parsed_subjects,1):
    print(f"  Subject {index}: {subject.strip()}")

#output
Original email:  Student123@gmail.com
1)check email is valid or not: valid email

2)Check the mail: Not Match


Phone Number Validation( 9234678991 ):  Valid


Phone Number Validation( 9234671 ):  Not Valid


Extract Numbers:
Normal text:  Order 123 Amount 450
Only Numbers: 
['123', '450']


Start at text( Python )-> Match


Start at text(simple)-> Not Match


Search at text( learn )-> Match


Search at text(Developer)-> Not Match


Original Text: Age 21 Roll 105 Marks 98
All Numbers in a text:  ['21', '105', '98']


Replace the text:
Before text:  I learn Java
After text:  I learn Python


Split the text:  ['HTML', 'CSS', 'JS', 'Python']


Findall start with word: 
Python
programming
Processing
packages
perform
perfectly

Word Starting at p after split applying the original data:
Python
programming
Processing
packages
perform
perfectly


Uppercase words found: ['WELCOME', 'ERROR', 'LOG']


The Digits in a Sentence:  ['42', '1', '57', '2']
Total No.of Count:  4


=== STUDENT REGISTRATION VALIDATOR ===


--- 1. Email Validation ---
User Email:  Student342@university.edu
Email validataion:  Valid


--- 2. Mobile Number Validation ---
Mobile Number:  9876543210
Mobile Validation:  Valid Number


--- 3. Roll Number Extraction ---
Source Sentence:  The admission desk assigned Roll No: CS2026105 to the new candidate.
Extracted Roll Number:  admission


--- 4. Status Update (Replace Fail with Pass) ---
Original Record: Final Status: Fail in Mathematics, Fail in Physics
Updated Record : Final Status: Pass in Mathematics, Pass in Physics


--- 5. Subject List Parsing ---
Raw Subject Data: Mathematics,Physics,Chemistry,Computer Science,English
Parsed Array List:
  Subject 1: Mathematics
  Subject 2: Physics
  Subject 3: Chemistry
  Subject 4: Computer Science
  Subject 5: English

=== Code Execution Successful ===




