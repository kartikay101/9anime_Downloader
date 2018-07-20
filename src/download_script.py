# @Author: Kartikay Shandil <kartikay101>
# @Date:   2018-07-20T14:41:40+05:30
# @Last modified by:   kartikay101
# @Last modified time: 2018-07-20T23:06:41+05:30

import subprocess
from subprocess import Popen
import time
import os

subprocess.Popen("uget-gtk")
filepath=os.path.realpath(__file__)
filepath=filepath.replace('/src/download_script.py','/res/')

links=open(filepath+"links.txt")
config=open(filepath+"config.cfg")

category=config.read()
category=category[:-1]

if category=='':
    category="1"

name=links.readline()
season=links.readline()

ititle="\""+name[:-1]+" S0"+season[:-1]+"Ep"

ep=1

for link in links:
    ctitle=ititle+str(ep)+".mp4\""
    command='./dnld_support.sh '+category+' '+ctitle+' '+link[:-1]
    print(command)
    ep=ep+1
    res=Popen([command],shell=True)
    time.sleep(4)
