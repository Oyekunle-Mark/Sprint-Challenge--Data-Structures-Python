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


# STRETCH SOLUTION
# DOES NOT STORE NAMES IN MEMORY
# FINDS THE SAME 64 DUPLICATES BUT TAKES ABOUT 15 SECONDS

# Uncomment to test it out

# import time

# start_time = time.time()

# duplicates = 0

# with open('names_1.txt', 'r') as f:
#     for line in f:
#         with open('names_2.txt', 'r') as f2:
#             for line2 in f2:
#                 if line == line2:
#                     print(line)
#                     duplicates += 1


# end_time = time.time()

# print(f"Number of duplicates: {duplicates}")
# print(f"runtime: {end_time - start_time} seconds")
