import pandas as pd
pd.options.mode.chained_assignment = None
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def show_missing(df):
    import missingno as msno
    msno.matrix(df, labels=False)
    plt.ylabel("Missing Value")

    filename = "img/missing_value.png"
    plt.savefig(filename)
    plt.close()
    return filename

def group_data(df,col_name,point):
    converted_lst = []
    index_list = list(df.index.values)
    for i in index_list:
        a = df[col_name][i]
        count = 0
        for b in point:
            if a >= b:
                count+=1
        converted_lst.append(count)
    return converted_lst

def str_to_num(df, col_name):
    if df[col_name].dtype == "object":
        labels, uniques = pd.factorize(df[col_name])
        return labels



