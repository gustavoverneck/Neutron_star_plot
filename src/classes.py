# src/classes

import os
import multiprocessing
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

class Data:
    def __init__(self, values):
        print(datetime.now(), " - Preparando dados.")
        self.values = values
        self.data = []
        for value in self.values:
            self.data.append(DataValues(value))
        print(datetime.now(), " - Produzinho gráficos.")
        self.plottingEOS()
        self.plottingTOV()

    def __str__(self):
        return f"Data({self.values})"
    
    def plottingEOS(self):
        plt.clf()
        for value in self.data:
            plt.plot(value.e, value.p, label=f"${value.title}$")
        plt.legend()
        plt.savefig("output/eos.png", dpi=450)
        print(datetime.now(), " - Gráfico das equações de estado foi gerado.")

    def plottingTOV(self):
        plt.clf()
        for value in self.data:
            plt.plot(value.r, value.m, label=f"${value.title}$")
        plt.legend()
        plt.savefig("output/mr.png", dpi=450)
        print(datetime.now(), " - Gráfico massa-raio foi gerado.")
    
    def plottingPopulation(self):
        pass
    

class DataValues:
    def __init__(self, title):
        self.title=title
        self.e = []
        self.p = []
        self.m = []
        self.r = []
        self.importData("eos")
        self.importData("tov")

    def importData(self, filetype):
        print(datetime.now(), f" - Importando dados {filetype} para csi={self.title}.")
        if filetype=="eos":
            with open(f"input/eos_{self.title}.dat", "r") as f1:
                for line1 in f1.readlines():
                    line1 = line1.split()
                    self.e.append(float(line1[0]))
                    self.p.append(float(line1[1]))
            del line1
        
        elif filetype=="tov":
            with open(f"input/eos_{self.title}.dat", "r") as f2:
                for line2 in f2.readlines():
                    line2 = line2.split()
                    self.m.append(float(line2[0]))
                    self.r.append(float(line2[1]))
        else:
            raise ValueError("Invalid type.")
    

    def __str__(self):
        return f"Data(csi={self.title})"