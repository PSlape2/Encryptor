from cryptography.fernet import Fernet
import methods as en

mode = input("Enter mode: ")

if (mode == "!"):
  key = Fernet.generate_key()
  path = input("Enter path: ")
  name = input("Key name: ")
  en.encrypt_file(path, key)
  en.write_key(key, name)
elif mode == "!!":
  path = input("Enter path: ")
  name = input("Key name: ")
  key = en.read_key(name)
  en.decrypt_file(path, key)
elif mode == "1":
  key = Fernet.generate_key()
  path = input("Directory: ")
  name = input("Enter name for key: ")
  en.encrypt_path(path, key)
  en.write_key(key, name)
elif mode == "2":
  path = input("Directory: ")
  name = input("Enter key name: ")
  key = en.read_key(name)
  en.decrypt_path(path, key)
