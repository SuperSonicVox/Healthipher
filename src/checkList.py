import pandas as pd
import numpy

def nomi_or_conti(df):
    contain = []
    header = []
    df.columns = df.columns.str.strip()
    contains = df.loc[0]
    i_ = rowCount(df, parent=None)
    for string in df.columns:
        header.append(string)
    for string in contains:
        contain.append(string)

    _data = i_
    con = []
    nomi = []

    for i in range(i_):
        ele = contain[i]
        if isinstance(ele, str): #True -> str -> nomi
            con.append(ele)
        elif isinstance(ele, numpy.int64): #True -> 整數 -> nomi
            con.append(ele)
        else: #False -> float -> 連續
            nomi.append(ele)

    print(con, nomi)

def rowCount(self, parent=None):
    return self._data.shape[0]

'''df = pd.read_csv('/Users/kaku/Documents/輔大/專題/數據/csv/00-train.csv')
nomi_or_conti(df)'''
