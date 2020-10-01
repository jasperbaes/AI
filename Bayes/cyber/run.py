import matplotlib.pyplot as plt
import pandas as pd
from numpy import genfromtxt
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score, confusion_matrix, f1_score, precision_score, recall_score)

def print_stats_metrics(y_test, y_pred):
    print('Accuracy: %.3f' % accuracy_score(y_test, y_pred))
    print('F1-measure: %.3f' % f1_score(y_test, y_pred))
    print('Recall: %.3f' % recall_score(y_test, y_pred))
    print('Precision: %.3f' % precision_score(y_test, y_pred))
    print('Confusion matrix: \n', confusion_matrix(y_test, y_pred))
    print('\n', pd.crosstab(y_test, y_pred, rownames=['True'], colnames=['Predicted'], margins=True))

features = genfromtxt('data2.csv', 
                        delimiter=',', 
                        usecols=(i for i in range(0,2)), 
                        dtype=int, 
                        skip_header=1)

class_value = genfromtxt('data2.csv', 
                        delimiter=',', 
                        usecols=(-1), 
                        dtype=str, 
                        skip_header=1)                    

# transforms the label to a number
labels = LabelEncoder().fit_transform(class_value)
features_normalized = StandardScaler().fit_transform(features)
x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size=0.40, random_state=0)

svm1 = svm.SVC()
svm1.fit(x_train, y_train)
y_pred = svm1.predict(x_test)
print_stats_metrics(y_test, y_pred)
