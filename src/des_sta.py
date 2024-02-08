from PyQt5.QtCore import QAbstractTableModel, Qt

import numpy
import matplotlib.pyplot as plt
import seaborn

from collections import Counter
import random

class pandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data


    def rowCount(self, parent=None):
        return self._data.shape[1]

    def columnCount(self, parnet=None):
        return self._data.shape[0]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.column(), index.row()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.index[col]
        if orientation == Qt.Vertical and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None

def show_cate_des(df, col_name):
    plt.rcParams['font.family'] = "Arial Unicode MS"
    count = Counter(df[col_name])
    bars = list(count)
    height = []
    for i in bars:
        height.append(count[i])
    y_pos = numpy.arange(len(bars))

    plt.bar(y_pos, height, color=(0.2, 0.4, 0.6, 0.6), edgecolor="blue")
    plt.xticks(y_pos, bars)
    plt.title(col_name)
    plt.xlabel("value")
    plt.ylabel("freq")
    filename = "img/"+col_name+"_des.png"
    plt.savefig(filename)
    plt.close()
    return bars, height, filename

def show_conti_des(df, col_name):
    plt.rcParams['font.family'] = "Arial Unicode MS"
    fig, ax = plt.subplots()
    plt.title(col_name)
    plt.xlabel("value")
    plt.ylabel("density")
    x = df[col_name].iloc[:]
    seaborn.kdeplot(x, shade=True, color="blue")
    filename = "img/"+col_name+"_des.png"
    plt.savefig(filename)
    plt.close()
    return filename


def show_grouped_des(df_col, col_name):
    plt.rcParams['font.family'] = "Arial Unicode MS"
    count = Counter(df_col)
    bars = list(count)
    height = []
    for i in bars:
        height.append(count[i])
    y_pos = numpy.arange(len(bars))

    plt.bar(y_pos, height, color=(0.2, 0.4, 0.6, 0.6), edgecolor="blue")
    plt.xticks(y_pos, bars)
    plt.title(col_name)
    plt.xlabel("value")
    plt.ylabel("freq")
    filename = "img/"+col_name+"_des.png"
    plt.savefig(filename)
    plt.close()
    return bars, height, filename