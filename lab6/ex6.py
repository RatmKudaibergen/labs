import os
 
path = r'/Users/Ратмир/PycharmProjects/PP2_2024Spring/lab_6/dir-and-files/ex06_A-Z_files'
 
if not os.path.exists(path):
    os.makedirs(path)
 
for i in range(ord('A'), ord('Z') + 1):
    file_path = os.path.join(path, f"{chr(i)}.txt")    
    with open(file_path, 'w'): 
