import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pandas as pd
import numpy

df = pd.read_csv('/Users/kaku/Documents/輔大/專題/數據/csv/00-train.csv')

class Window(QWidget):
    def __init__(self, data, lst, lst2):
        QAbstractTableModel.__init__(self)
        self._data = data
        self.layoutH = QHBoxLayout()
        con = []
        nomi = []

        for i in range(data):
            self.checkbox = QCheckBox("%s" % header[i])
            ele = contain[i]

            self.layoutH.addWidget(self.checkbox)
            self.layoutH.setAlignment(Qt.AlignCenter)

        self.label = QLabel("selected: ")
        self.button = QPushButton("Submit")
        self.button.clicked.connect(self.ButtonClicked)

        layoutV = QVBoxLayout(self)
        layoutV.addLayout(self.layoutH)
        layoutV.addWidget(self.label)
        layoutV.addWidget(self.button)

    def ButtonClicked(self):
        lst = []
        for i in range(self.layoutH.count()):
            chBox = self.layoutH.itemAt(i).widget()
            if chBox.isChecked():
                lst.append(chBox.text())
        self.label.setText("Choosed variables: " + str(lst))

    def rowCount(self, parent=None):
        print(self._data.shape[0])
        return self._data.shape[0]

if __name__ == '__main__':
    app = QApplication(sys.argv)
    i = Window.rowCount(df, parent=None)
    header = []
    contain = []
    df.columns = df.columns.str.strip()
    contains = df.loc[0]
    for string in df.columns:
        header.append(string)
    for string in contains:
        contain.append(string)
    window = Window(i, header, contain)
    window.resize(1134, 739)
    window.show()
    sys.exit(app.exec_())