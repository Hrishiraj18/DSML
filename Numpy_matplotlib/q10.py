import numpy as np
import random
from collections import Counter
total_rolls=1000
rolls=[random.randint(1,6) for i in range (total_rolls)]
occurrence=Counter(rolls)
print("Occurrences of roll outcomes:")
for item,count in occurrence.items():
    print(f"Number {item} : {count} times ")
