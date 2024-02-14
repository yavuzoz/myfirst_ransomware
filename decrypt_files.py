import os
from cryptography.fernet import Fernet

directory_ransomware = "/home/vmadmin/workspace/ransomware/files"
os.chdir(directory_ransomware)

files = [file for file in os.listdir() if os.path.isfile(file)]

with open("master_key.key", "rb") as master_key:
    key = master_key.read()

for file in files:
    with open(file, "rb") as the_file:
        content = the_file.read()
    
    try:
        content_decrypted = Fernet(key).decrypt(content)
        with open(file, "wb") as the_file:
            the_file.write(content_decrypted)
    except Exception as e:
        print(f"Error decrypting {file}: {e}")

print("Your files were decrypted by the man from world !!")
