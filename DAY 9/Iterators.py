#1 
numbers=[10,20,30,40,50]
it=iter(numbers)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
#After completing an array it raise an error stop iteration
#2
company="Google"
itt=iter(company)
print(next(itt))
print(next(itt))
print(next(itt))

#3
arr=iter([3,6,4,2,7,9])
print(next(arr))
print(next(arr))

#4
def numbers():
    yield 10
    yield 20
    yield 30
for i in numbers():
    print(i)
    
#5
square=(x*x for x in range(5))
print(next(square))
print(next(square))
print(next(square))
print(next(square))

#6
square=[x*x for x in range(5)]
print(square)

#7
class Count:
    def __init__(self):
        self.num=1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num<=5:
            value=self.num
            self.num+=1
            return value
        raise StopIteration
        
obj=Count()
for i in obj:
    print(i)
