import os
import getpass
import glob
import subprocess
import shutil


def bilder(path):
    dateien_suche = glob.glob(os.path.join(path, "*.jpeg")
                              + os.path.join(path, "*.jpg")
                              + os.path.join(path, "*.png")
                              + os.path.join(path, "*.gif")
                              + os.path.join(path, "*.bmp")
                              + os.path.join(path, "*.tiff")
                              + os.path.join(path, "*.tif")
                              + os.path.join(path, "*.mp4")
                              + os.path.join(path, "*.mov")
                              + os.path.join(path, "*.avi")
                              + os.path.join(path, "*.wmv")
                              + os.path.join(path, "*.mkv"))

    zielordner = path + "Bilder"

    if not os.path.exists(zielordner):
        os.makedirs(zielordner)

    for datei in dateien_suche:
        ziel = os.path.join(zielordner, os.path.basename(datei))
        if os.path.exists(ziel):
            print(f"{ziel} existiert bereits. Datei wird nicht bewegt.")
        else:
            shutil.move(datei, ziel)
            print(f"{datei} wurde nach {ziel} verschoben.")
