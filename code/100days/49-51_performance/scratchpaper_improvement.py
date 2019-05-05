import random
import numpy as np
import cProfile

profiler = cProfile.Profile()
profiler.disable()



profiler.enable()

x = np.arange(1,1_000_000,1,dtype='int64')

randolist = []

for i in x:
    randolist.append(i*np.random.randint(1,1000))

y = sum(randolist)

profiler.disable()

profiler.print_stats(sort='cumtime')