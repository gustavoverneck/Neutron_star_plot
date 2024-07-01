# src/classes

import os
import multiprocessing
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
from src.setup import main_directory, open_directory_in_file_explorer
from time import sleep

class Data:
    def __init__(self, values, magnetic_field="0.0", model="GM1"):
        print(datetime.now(), " - Preparando dados.")
        self.rawValues = values
        self.readValues()
        self.magnetic_field = magnetic_field
        self.model = model
        self.data = []


        # STRINGS
        self.max = f"max"


        # Plotting settings
        self.legend_fontsize = 6
        self.linewidth = 0.5
        self.grid_alpha = 0.5
        self.grid_linestyle = "--"
        self.decimal_precision = 4
        self.dpi = 600


        self.colors = colors1 = ["r", "g", "b", "c", "m", "y", "k", "pink", 'crimson', 'maroon', 'gold', 'darkorange', 'darkgreen', 'lime', 'gray']
        for value in self.values:
            self.data.append(DataValues(value))

        print(datetime.now(), " - Produzinho gráficos.")
        self.plottingEOS()
        self.plottingTOV()
        self.plottingPnB()
        self.plottingZoomedEOS()
        self.plottingZoomedTOV()
        print(datetime.now(), " - Abrindo diretório de saída.")
        open_directory_in_file_explorer(f"{main_directory}/output")

    def readValues(self):
        self.values = []
        self.valuesTitles = []
        for v in self.rawValues:
            self.values.append(v.split(", ")[0].split("\n")[0])
            self.valuesTitles.append(v.split(", ")[1])

    def plottingEOS(self):
        plt.clf()
        for value in self.data:
            color = self.colors[self.values.index(value.title)]
            max_m = value.max_m
            max_r = value.r_max_m
            csi = value.title
            plt.plot(value.e, value.p, label=f"$\\xi ={self.valuesTitles[self.values.index(value.title)]} : "+r"R_{max}"+f"={round(max_r, self.decimal_precision)} km, "+r"M_{max}="+f"{round(max_m, self.decimal_precision)} M_\odot$", color=color, linewidth=self.linewidth)
        plt.legend(fontsize=self.legend_fontsize)
        plt.grid(linestyle=self.grid_linestyle, alpha=self.grid_alpha)
        plt.title(f"{self.model} - Equations of State for {self.magnetic_field} G")
        plt.ylabel("$\epsilon$ $[fm^{-4}]$")
        plt.xlabel("$p$ $[fm^{-4}]$")
        plt.savefig("output/eos.svg", dpi=self.dpi)
        print(datetime.now(), " - Gráfico das equações de estado foi gerado.")

    def plottingTOV(self):
        plt.clf()
        for value in self.data:
            color = self.colors[self.values.index(value.title)]
            max_m = value.max_m
            max_r = value.r_max_m
            csi = value.title
            plt.plot(value.r, value.m, label=f"$\\xi ={self.valuesTitles[self.values.index(value.title)]} : "+r"R_{max}"+f"={round(max_r, self.decimal_precision)} km, "+r"M_{max}="+f"{round(max_m, self.decimal_precision)} M_\odot$", color=color, linewidth=self.linewidth)
            plt.plot(value.r_max_m, value.max_m, marker=".", color=color, markersize=10)
        plt.legend(fontsize=self.legend_fontsize)
        plt.title(f"{self.model} - Mass-Radius Diagram for {self.magnetic_field} G")
        plt.xlabel("$Radius$ $[km]$")
        plt.grid(linestyle=self.grid_linestyle, alpha=self.grid_alpha)
        plt.ylabel("$Mass [M_{\odot}]$")
        plt.savefig("output/mr.svg", dpi=self.dpi)
        print(datetime.now(), " - Gráfico massa-raio foi gerado.")
    
    def plottingPnB(self):
        plt.clf()
        for value in self.data:
            max_m = value.max_m
            max_r = value.r_max_m
            csi = value.title
            color = self.colors[self.values.index(value.title)]
            plt.plot(value.nB, value.p, label=f"$\\xi ={self.valuesTitles[self.values.index(value.title)]} : "+r"R_{max}"+f"={round(max_r, self.decimal_precision)} km, "+r"M_{max}="+f"{round(max_m, self.decimal_precision)} M_\odot$", color=color, linewidth=self.linewidth)
        plt.legend(fontsize=self.legend_fontsize)
        plt.grid(linestyle=self.grid_linestyle, alpha=self.grid_alpha)
        plt.title(f"{self.model} - Pressure-Baryon Number Density relation for {self.magnetic_field} G")
        plt.xlabel("$n_B \;\; [fm^{-3}]$")
        plt.ylabel("$p \;\;[fm^{-4}]$")
        plt.savefig("output/pnb.svg", dpi=self.dpi)
        print(datetime.now(), " - Gráfico pressão-densidade de número bariônico foi gerado.")

    def plottingZoomedEOS(self):
        plt.clf()
        for value in self.data:
            color = self.colors[self.values.index(value.title)]
            max_m = value.max_m
            max_r = value.r_max_m
            csi = value.title
            plt.plot(value.e, value.p, label=f"$\\xi ={self.valuesTitles[self.values.index(value.title)]} : "+r"R_{max}"+f"={round(max_r, self.decimal_precision)} km, "+r"M_{max}="+f"{round(max_m, self.decimal_precision)} M_\odot$", color=color, linewidth=self.linewidth)
        plt.xticks([])
        plt.yticks([])
        plt.xlim(0.7, 0.9)
        plt.ylim(0.9, 1.5)
        plt.savefig("output/zoomed_eos.svg", dpi=self.dpi)
        print(datetime.now(), " - Gráfico das equações de estado com zoom foi gerado.")

    def plottingZoomedTOV(self):
        plt.clf()
        for value in self.data:
            color = self.colors[self.values.index(value.title)]
            max_m = value.max_m
            max_r = value.r_max_m
            csi = value.title
            plt.plot(value.r, value.m, label=f"$\\xi ={self.valuesTitles[self.values.index(value.title)]} : R_{self.max} {round(max_r, self.decimal_precision)} km, M_{self.max} {round(max_m, self.decimal_precision)} M_\odot$", color=color, linewidth=self.linewidth)
            plt.plot(value.r_max_m, value.max_m, marker=".", color=color, markersize=10)
        plt.xticks([])
        plt.yticks([])
        plt.xlim(12.6, 13.1)
        plt.ylim(1.60, 1.9)
        plt.savefig("output/zoomed_mr.svg", dpi=self.dpi)
        print(datetime.now(), " - Gráfico massa-raio com zoom foi gerado.")
    
    def __str__(self):
        return f"Data({self.values})"

class DataValues:
    def __init__(self, title):
        self.title=title
        self.nB = []
        self.e = []
        self.p = []
        self.m = []
        self.r = []
        self.importData("eos")
        self.importData("tov")
        self.max_m = max(self.m)
        self.r_max_m = self.r[self.m.index(self.max_m)]


    def importData(self, filetype):
        print(datetime.now(), f" - Importando dados {filetype} para csi={self.title}.")
        if filetype=="eos":
            with open(f"input/eos_{self.title}.dat", "r") as f1:
                for line1 in f1.readlines():
                    line1 = line1.split()
                    self.nB.append(float(line1[0]))
                    self.e.append(float(line1[1]))
                    self.p.append(float(line1[2]))
            del line1
        
        elif filetype=="tov":
            with open(f"input/tov_{self.title}.out", "r") as f2:
                for line2 in f2.readlines():
                    line2 = line2.split()
                    self.m.append(float(line2[1]))
                    self.r.append(float(line2[2]))
                del line2
        else:
            raise ValueError("Invalid type.")

    def __str__(self):
        return f"Data(csi={self.title})"