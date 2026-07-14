from itertools import count,cycle,repeat,product,permutations,combinations,combinations_with_replacement, accumulate,groupby
import operator
for i in count(15):
    if i>20:
        break
    print(i)

#2
data=cycle(["Ram","Sita"])
for i in range(6):
    print(next(data))
#3
for i in repeat("Hello",5):
    print(i)

#4
colors=product([1,2],["Blue","White"])
print(list(colors))

#5
per=list(permutations([2,3,4],2))
print(per)

#6
Comb=combinations([8,9,6],2)
print(list(Comb))

#7
list1=[7,3,9]
CR=combinations_with_replacement([list1],2)
print(list(CR))

#8
Mul=accumulate([1,2,3,4],operator.mul)
print(list(Mul))

#9
list2=[8,8,8,8,1,1,1,4,4,4,8,8,9,1]
for key,group in groupby(list2):
    print(key, list(group))
