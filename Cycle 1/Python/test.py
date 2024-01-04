import numpy as np
import random
from collections import Counter
total=1000

list=[random.randint(1,6) for i in range(total)]
times=Counter(list)
for item,values in times.items():
    print(f"Number {item}: {values} times")
