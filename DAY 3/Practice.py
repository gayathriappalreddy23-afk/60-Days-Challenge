from functools import reduce,partial,lru_cache,wraps
data=[9,3,2,4,5]
sum_result=reduce(lambda a,b:a+b,data)
print("The sum of data: ",sum_result)

#2
Mul_result=reduce(lambda a,b:a*b,data)
print("The Product of data: ",Mul_result)

#3

def fun(base,exp):
    return base**exp
result=partial(fun,exp=5)
print("Cube of a number:",result(5))

#4
@lru_cache(maxsize=None)
def fib(n):
    if n<2:
        return n
    return fib(n-1)+fib(n-2)

print("Fibonanci series 1 to 50: ")
for i in range(9):
    print(fib(i), end=" ")

#5
def My_decorator(add):
    @wraps(add)
    def wrapper(*args,**kwargs):
        print("\n\n-----Before-----")
        return add(*args,**kwargs)
    return wrapper
@My_decorator
def add(a,b):
    return a+b
print("Adding two numbers: ",add(7,5))

#6

arr=[6,3,2,8,4,9,12,8,45,34]
max_result=reduce(lambda a,b:a if a>b else b,arr)
print("Maximum number in a data: ",max_result)



