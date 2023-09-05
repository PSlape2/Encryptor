from cryptography.fernet import Fernet
import os

def encrypt_path(directory, key):
  files = []
  for file in detect_files(directory):
    files.append("files/" + file)
  for file in files:
    if(not encrypt_file(file, key)):
      for filer in detect_files(file):
        files.append(file + "/"+ filer)
    
def decrypt_path(directory, key):
  files = []
  for file in detect_files(directory):
    files.append("files/" + file)
  for file in files:
    if(not decrypt_file(file, key)):
      for filer in detect_files(file):
        files.append(file + "/"+ filer)
    
def encrypt_file(file_path, key):
  try:
    with open(file_path, 'rb') as file:
        file_data = file.read()
  except:
    return False
  else:
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(file_data)
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)
    return True

def decrypt_file(file_path, key):
  try:
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
  except:
    return False
  else:
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(file_path, 'wb') as file:
        file.write(decrypted_data)
    return True

def write_key(key, path):
  with open((path + ".key"), 'wb') as file:
    file.write(key)
    
def read_key(path):
  f = open((path + ".key"), 'rb').read()
  os.remove(path + ".key")
  return f

def detect_files(path = None):
  return os.listdir(path)


  
  
    