from itertools import count,repeat,product,permutations,combinations,accumulate,groupby
import operator
for i in count(50):
    if i>60:
        break
    print(i)

#2 task
for i in repeat("Welcome",6):
    print(i)

#3 task
data1=product([5,6],[3,9])
print(list(data1))

#4 task
data2=permutations(['A','B','C'],2)
print(list(data2))

#5 task
print(list(combinations([4,5,6,7],2)))

#6 accumulate

print(list(accumulate([9,4,5,3,7],operator.add)))

#7 Groupby
data=[1,1,1,1,2,2,2,2,3,3,4,4,4,6,6,7,8,8,8,9]
for key,group in groupby(data):
      print(key,list(group))

#8 task
print(list(product(['A','B'], repeat=3)))
