#1
arr=[1,2,3,4,5,6,7,8]
result=list(map(lambda x:x*x, filter(lambda x:x%2==0,arr)))
print("Result: ",result)

#2
Names=["Rama","Sita","Pinky","Ravi","Lucky","Indu","Siri"]
Marks=[90,23,48,78,67,98,59]
zip_result=list(zip(Names,Marks))
print("\n\nZip Result: ",zip_result)

#3
fil_result=list(filter(lambda x:x>60,Marks))
print("\nstudents who scored above 60: ",fil_result)

#4
map_result=list(filter(lambda x:x+5,Marks))
print("\nstudents to add bonus marks (+5): ",map_result)

#5
print("\nstudents to display ranks based on Marks: ")
Marks=sorted(Marks,reverse=True)
for index,value in enumerate(Marks):
    if value>=90:
        rank=index+1
    elif value>=75:
        rank=index+1
    elif value>=60:
        rank=index+1
    else:
        rank=index+1
    print("value: ",value,"Rank: ",rank)
        
    
#6
pass_percentage=30
all_passed=all(score>=pass_percentage for score in Marks)
print("\nCheck eveyone passed these exam or not: ",all_passed)

#7
any_got_max_marks=any(score==100 for score in Marks)
print("\nCheck if any student scored 100: ",any_got_max_marks)
