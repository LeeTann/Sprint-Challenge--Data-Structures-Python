import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# # slightly better
# duplicates = []
# for name_1 in names_1:
#     duplicates.append(name_1)

# for name_2 in names_2:
#     if name_2 in duplicates:
#         name_2 == name_1

# better
duplicates = []
dict_names = {}

for name_1 in names_1:
    dict_names[name_1] = True

for name_2 in names_2:
    if name_2 in dict_names:
        duplicates.append(name_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

