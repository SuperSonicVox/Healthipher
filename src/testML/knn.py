from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier as KNC
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.metrics import accuracy_score, roc_curve, auc, f1_score
import os


def training(df, neighbor):
    x_train, x_test, y_train, y_test = train_test_split(df.iloc[:, 0:-1], df.iloc[:, -1], \
                                                        train_size=0.8, test_size=0.2, random_state=24)
    lr = KNC(n_neighbors=int(neighbor))
    lr.fit(x_train, y_train)
    pre = lr.predict(x_test)
    cm = metrics.confusion_matrix(y_test, pre)
    sens_score = (cm[0, 0] / (cm[0, 0] + cm[0, 1])).round(6)
    spec_score = (cm[1, 1] / (cm[1, 0] + cm[1, 1])).round(6)

    # precision(PPV) and NPV
    precision = (cm[0, 0] / (cm[0, 0] + cm[1, 0])).round(6)
    npv_score = (cm[1, 1] / (cm[0, 1] + cm[1, 1])).round(6)
    f1score = f1_score(y_test, pre).round(6)

    # auc value
    fpr, tpr, _ = roc_curve(y_test, pre)
    roc_auc = auc(fpr, tpr)

    return y_test, pre, accuracy_score(y_test, pre).round(6), sens_score, spec_score, roc_auc, precision, npv_score, f1score

def conf_matrix(y_test, pre):
    # self.count += 1
    data = {'y_Actual': y_test, 'y_Predicted': pre}
    df = pd.DataFrame(data, columns=['y_Actual', 'y_Predicted'])
    confusion_matrix = pd.crosstab(df['y_Actual'], df['y_Predicted'], rownames=['Actual'], colnames=['Predicted'])
    con_fig = plt.figure()
    plt.title("Confusion Matrix")
    sns.heatmap(confusion_matrix, annot=True, linewidths=.5)

    filename = "img/knn_confu.png"
    plt.savefig(filename)
    plt.close()
    return filename

def roccurve(y_test, pre):
    fpr, tpr, threshold = roc_curve(y_test, pre)
    roc_auc = auc(fpr, tpr)
    plt.title('Receiver Operating Characteristic')
    plt.plot(fpr, tpr, 'b', label='AUC = %0.2f' % roc_auc)
    plt.legend(loc='lower right')
    plt.plot([0, 1], [0, 1], 'r--')
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.ylabel('True Positive Rate')
    plt.xlabel('False Positive Rate')

    filename = "img/knn_roc.png"
    plt.savefig(filename)
    plt.close()
    return filename
    #plt.show()