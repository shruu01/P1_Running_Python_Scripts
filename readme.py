import os

folder_path = r"E:\sem_3\programming_3\P1_Running_Python_Scripts"
file_name = "readme.txt"

file_path = os.path.join(folder_path, file_name)

file_obj = open(file_path, 'r')

# -----to read letters (5) = hello---- otherwise reads every thing--------
# print(file_obj.read())

# -----to read one line------
# print(file_obj.readline())

# ----to read every list of all line------
# print(file_obj.readlines())

#

lines = file_obj.readlines()

count = 1
for line in lines:
    print("{} - {}".format(count, line))
    count = count +  1

