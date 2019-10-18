import time
# import the Counter class and deque function from the collections library
from collections import Counter, deque

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

# create a counter of names_1
names_1 = Counter(names_1)

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# create a counter of names_2
names_2 = Counter(names_2)

# initialize a deque to hold the duplicates
duplicates = deque()

# for every key in the names_1 counter
for name in names_1:
    # if the key is also present in names_2 counter
    if name in names_2:
        # add it to the duplicates deque
        duplicates.append(name)

end_time = time.time()

print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
