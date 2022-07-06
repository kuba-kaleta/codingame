# Generators
# https://realpython.com/introduction-to-python-generators/

import sys
import cProfile


def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


gen = infinite_sequence()
print("\ngen. object:", gen)
print("next: ", next(gen), next(gen), next(gen))

nums_squared_lc = [num**2 for num in range(1000)]  # list comprehension
nums_squared_gc = (num**2 for num in range(1000))  # generator comprehension

print("\nPerformance:\nlist sizeof:", sys.getsizeof(nums_squared_lc))
print("gen. sizeof:", sys.getsizeof(nums_squared_gc))

print("list: 5 function calls in 0.001 seconds")  # cProfile.run('sum([i * 2 for i in range(10000)])')
print("gen.: 10005 function calls in 0.002 seconds\n")  # cProfile.run('sum((i * 2 for i in range(10000)))')















