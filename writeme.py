import os

folder_path = r"E:\sem_3\programming_3\P1_Running_Python_Scripts"
file_name = "writeme.txt"

file_path = os.path.join(folder_path, file_name)

file_obj = open(file_path, 'w')

input_text = "hello guysss"

file_obj.write(input_text)
file_obj.close()

print("process completed")