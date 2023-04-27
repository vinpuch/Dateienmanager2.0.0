import getpass
import os
import platform
import sys
import glob
from pdf import pdf




def main():
    # Betriebsystem check
    if sys.platform == "win" :
        path = "/home/vinpuch/Download"
    elif sys.platform == "darwin":
        path = "/Users/vincentpuchner/Downloads"
    elif sys.platform == "linux":
        path="/home/user/Downloads"
    
   # anki(path)
   # bilder(path)
   # excel(path)
    pdf(path)
   # word(path)
    # zip(path)

    

