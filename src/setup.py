# /src/setup.py

import os
import shutil
from datetime import datetime

main_directory = os.getcwd()


def importValues(filename):
    with open(f"{main_directory}/input/{filename}") as f:
        print(datetime.now(), " - Lendo valores de entrada.")
        return [str(a).split("\n")[0] for a in f.readlines()]

def createOutputDir(name="output"):
    if not os.path.exists(f'{main_directory}/{name}'):
        print(datetime.now(), f" - Criando diretório {name}.")
        os.makedirs(f'{main_directory}/{name}')
    
def removeOutputDir(name="output"):
    if os.path.exists(f'{main_directory}/{name}'):
        print(datetime.now(), f" - Removendo diretório {name}.")
        shutil.rmtree(f'{main_directory}/{name}')

