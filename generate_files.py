import os

def create_files(directory, number_of_files):
    if not os.path.exists(directory):
        os.makedirs(directory)
    for i in range(1, number_of_files + 1):
        file_name= f"file_{i}.txt"
        file_path = os.path.join(directory, file_name)
        with open(file_path, 'w') as file:
            file.write(str(i)+ "Legends never die, they just update !")  
directory ="/home/vmadmin/workspace/randsomware/files"   
number_of_files = 1000
create_files(directory, number_of_files)           