import operator
from itertools import (
    accumulate, chain, combinations, combinations_with_replacement,
    compress, count, cycle, dropwhile, groupby, islice,
    pairwise, permutations, product, repeat, starmap, takewhile
)
from functools import (
    cache, cached_property, cmp_to_key, lru_cache, partial,
    partialmethod, reduce, singledispatch, total_ordering
)

# --- 10 ITERTOOLS EXAMPLES ---
# 1. count: Infinite counter
ex1 = list(islice(count(10, 2), 5))  # [10, 12, 14, 16, 18]

# 2. cycle: Repeat sequence endlessly
ex2 = list(islice(cycle([1, 2]), 5))  # [1, 2, 1, 2, 1]

# 3. repeat: Repeat single value n times
ex3 = list(repeat("A", 3))  # ['A', 'A', 'A']

# 4. accumulate: Running totals
ex4 = list(accumulate([1, 2, 3, 4]))  # [1, 3, 6, 10]

# 5. chain: Combine multiple iterables
ex5 = list(chain([1, 2], [3, 4]))  # [1, 2, 3, 4]

# 6. pairwise: Adjacent overlapping pairs
ex6 = list(pairwise([1, 2, 3, 4]))  # [(1, 2), (2, 3), (3, 4)]

# 7. product: Cartesian product
ex7 = list(product([1, 2], ['a', 'b']))  # [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]

# 8. permutations: Ordered arrangements
ex8 = list(permutations([1, 2], 2))  # [(1, 2), (2, 1)]

# 9. combinations: Unordered selections
ex9 = list(combinations([1, 2, 3], 2))  # [(1, 2), (1, 3), (2, 3)]

# 10. groupby: Group adjacent keys
ex10 = {k: list(g) for k, g in groupby("AABBBCCA")}  # {'A': ['A', 'A'], 'B': ['B', 'B', 'B'], 'C': ['C', 'C'], 'A': ['A']}


# --- 10 FUNCTOOLS EXAMPLES ---
# 11. reduce: Cumulative computation
ex11 = reduce(operator.add, [1, 2, 3, 4, 5])  # 15

# 12. partial: Preset function arguments
power_of_two = partial(pow, 2)
ex12 = power_of_two(3)  # 2^3 = 8

# 13. lru_cache: Memoized function calls
@lru_cache(maxsize=4)
def fib(n):
    return n if n < 2 else fib(n-1) + fib(n-2)
ex13 = fib(6)  # 8

# 14. cache: Unlimited memoized function calls
@cache
def expensive_sq(x):
    return x * x
ex14 = expensive_sq(9)  # 81

# 15. cmp_to_key: Legacy comparator to sort key
ex15 = sorted([3, 1, 4, 2], key=cmp_to_key(lambda a, b: b - a))  # [4, 3, 2, 1]

# 16. total_ordering: Class comparison helper
@total_ordering
class Item:
    def __init__(self, val): self.val = val
    def __eq__(self, other): return self.val == other.val
    def __lt__(self, other): return self.val < other.val
ex16 = Item(1) < Item(2)  # True

# 17. singledispatch: Generic function dispatch
@singledispatch
def fmt(arg): return "Base"
@fmt.register(int)
def _(arg): return f"Int: {arg}"
ex17 = fmt(42)  # 'Int: 42'

# 18. cached_property: Property value caching per instance
class Data:
    @cached_property
    def heavy(self): return "computed"
ex18 = Data().heavy  # 'computed'

# 19. starmap (from itertools, often paired with functools concepts): Apply function from unpacked args
ex19 = list(starmap(pow, [(2, 3), (3, 2)]))  # [8, 9]

# 20. partialmethod: Partial for class methods
class MyClass:
    def method(self, a, b): return a + b
    m_plus_5 = partialmethod(method, 5)
ex20 = MyClass().m_plus_5(10)  # 15
