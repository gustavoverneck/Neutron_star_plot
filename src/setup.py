# /src/setup.py
import sys, subprocess, os
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


def open_directory_in_file_explorer(path):
    if not os.path.isdir(path):
        raise ValueError(f"The path '{path}' is not a valid directory.")
    
    if os.name == 'nt':  # Windows
        os.startfile(path)
    elif os.name == 'posix':
        if sys.platform == 'darwin':  # macOS
            subprocess.run(['open', path])
        else:  # Linux
            subprocess.run(['xdg-open', path])
    else:
        raise OSError(f"It was not possible to open output directory in {os.name}.")
