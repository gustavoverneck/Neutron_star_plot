from datetime import datetime
from src.setup import importValues, createOutputDir, removeOutputDir, main_directory
from src.classes import Data


if __name__ == "__main__":
    print(datetime.now(), " - Inicializando aplicação.\n")
    removeOutputDir()
    createOutputDir()
    values = importValues("valores.dat")
    dados = Data(values, magnetic_field="$B=10^{17}$", model="GM1")
    