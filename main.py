import getpass
import os
import platform
import sys
import glob
from dateien.pdf import pdf_ready
from dateien.word import word_p
from dateien.zip import zip
from dateien.excel import excel
from dateien.bilder import bilder
from dateien.anki import anki




    # Betriebsystem check
if sys.platform == "win" :
    path = "/home/vinpuch/Download"
elif sys.platform == "darwin":
    path = "/Users/vincentpuchner/Downloads"
elif sys.platform == "linux":
    if sys.platform == "linux":
        username = getpass.getuser()
        path = f"/home/{username}/Downloads"

    
pdf_ready(path)
word_p(path)
zip(path)
excel(path)
bilder(path)
anki(path)
print("Der Code wurde erfolgreich ausgeführt.")
