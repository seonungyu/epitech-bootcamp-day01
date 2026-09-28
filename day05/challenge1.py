import random
import time

start = time.time()
numbers = [random.randint(0, 1000000) for i in range(1000000)]
numbers.sort()
print(numbers[:10])
print(time.time() - start)
