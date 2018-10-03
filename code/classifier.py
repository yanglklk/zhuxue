path1=r'D:\BaiduNetdiskDownload\zizhu\zizhu\test'
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn import preprocessing

train=pd.read_csv(path1+r'\train.csv',encoding='gbk')
test=pd.read_csv(path1+r'\test.csv',encoding='gbk')
train.index=train.id
test.index=test.id
train=train[train.amount>0]
# train=train.drop(['id','amount'],axis=1)
# label=train.amount
# train_X=data
# test_X=data[4100:]
# train_y=label
# test_y=label[4100:]

train_X=train.drop(['id','amount'],axis=1)
test_X=test.drop('id',axis=1)
train_y=train.amount
print(train_X.describe(),'\n',test_X.describe())

from sklearn.multiclass import  OneVsRestClassifier
from sklearn.linear_model import SGDRegressor
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn.tree import ExtraTreeClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.cluster import KMeans
km=KMeans(n_clusters=3,random_state=0)
nb=DecisionTreeClassifier()

svc=LinearSVC(random_state=0)


# nb.fit(train_X,train_y)
# y_pb=nb.predict(test_X)
# train_y=pd.DataFrame(train_y)
# # test_y=pd.DataFrame(test_y)
# result=pd.DataFrame(y_pb,index=test_X.index)
# # print(train_y.index,result.index)
# # result=pd.merge(result,test_y,on='id')
# # print(y_pb)
# result.columns=['amount']
# result=result[result.amount>0]
# result=pd.merge(result,test_X,on='id')
#
# # result=result.groupby('amount').count()
# result.to_csv(path1+r'\result.csv')