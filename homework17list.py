import random
from collections import Counter

# Creating a list with 100 random integers in the range from 1 to 10
random_list = [random.randint(1, 10) for _ in range(100)]

# Counting the occurrences of each element
element_count = Counter(random_list)

# Printing the count of each element
for element, count in element_count.items():
    print(f"Number {element} occurs {count} times.")