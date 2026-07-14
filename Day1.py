data=[9,3,4,7,1,7,8,2,9,4,3]
print(max(data))
print(min(data))
print(sum(data))
even=0
odd=0
rev=[0]*len(data)
for i in data:
    if i%2==0:
        even+=1
    else:
        odd+=1
    
print("Even Numbers: ",even)
print("Odd Numbers: ",odd)
for i in range(len(data),0):
    rev.append(data[i])
print("Reverse an array: ",rev)
for i,value in enumerate(data):
    print("Index: ",i," Value: ",value)
