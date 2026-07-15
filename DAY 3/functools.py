from functools import reduce,partial,cmp_to_key,lru_cache,wraps
arr=[10,20,30,40]
result=reduce(lambda x,y:x+y,arr)
print("The result using Reduce to add of arr values: ",result)
result2=reduce(lambda x,y:x*y,arr)
print("The result using Reduce to multiplication of arr values: ",result2)

#2Task
def fun(base,exponent):
    return base**exponent

square=partial(fun,exponent=2)
cube=partial(fun,exponent=3)
print("Square of a number 5 = ",square(5))
print("Cube of a number 5 = ",cube(5))
#it is ok in simple funcions but large code better in partial
print("Square of a number 5 = ",fun(5,2))
print("Cube of a number 5 = ",fun(5,3))

#3Task
def fibonanci(n):
    if n<2:
        return n
    return fibonanci(n-1)+fibonanci(n-2)
print("Fibonanci of 1 to 8: ",fibonanci(8))


#4 Task

def decorator(compare):
    @wraps(compare)
    def wrapper(*args,**kwargs):
        print("Before Comparing..")
        return compare(*args,**kwargs)
    return wrapper

#5 Task
@decorator
def compare(a,b):
    return a-b
numbers=[9,3,4,1]
numbers.sort(key=cmp_to_key(compare))
print(numbers)

#6 Task
# without using "lru_cache" also poosible but in large data set if you try to calculate fibonacci(50), your computer will freeze or run forever. 
@lru_cache(maxsize=None)
def fibonanci(n):
    if n<2:
        return n
    return fibonanci(n-1)+fibonanci(n-2)
print("Fibonanci series using lru_cache from 1 to 90: ",fibonanci(90))
