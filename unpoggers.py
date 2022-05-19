#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

#find all files in the cwd

files = []

for file in os.listdir():
	if file == "poggers.py" or file == "theKey.key" or file == "unpoggers.py":
		continue
	if os.path.isfile(file):
		files.append(file)
	

print(files)


with open("theKey.key", "rb") as thekey:
        key = thekey.read()


for file in files:
	with open(file, "rb") as thefile:
		encrypted_contents = thefile.read()
	contents_decrypted = Fernet(key).decrypt(encrypted_contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_decrypted)


print("You just got untrolled")
