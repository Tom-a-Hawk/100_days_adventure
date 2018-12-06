import random
import cProfile

profiler = cProfile.Profile()
profiler.disable()



profiler.enable()
random_list = []

for i in range(1,1_000_000):
    x = i * random.randint(1,1000)
    random_list.append(x)


y = sum(random_list)

print(y)
profiler.disable()

profiler.print_stats(sort='cumtime')