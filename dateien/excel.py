import os
import getpass
import glob
import subprocess
import shutil
import main


def excel(path):
    dateien_suche = glob.glob(os.path.join(path, "*.xlsx"))

    print(dateien_suche)

    zielordner = path + "Excel"

    if not os.path.exists(zielordner):
        os.makedirs(zielordner)

    for datei in dateien_suche:
        ziel = os.path.join(zielordner, os.path.basename(datei))
        if os.path.exists(ziel):
            print(f"{ziel} existiert bereits. Datei wird nicht bewegt.")

        else:
            shutil.move(datei, ziel)
            print(f"{datei} wurde nach {ziel} verschoben.")



