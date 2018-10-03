path=r'D:\BaiduNetdiskDownload\zizhu\zizhu'
path1=r'D:\BaiduNetdiskDownload\zizhu\zizhu\test'
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn import preprocessing
card=pd.read_csv(path1+r'\card_test.txt',header=None)
lib=pd.read_csv(path1+r'\library_test.txt',header=None)
borrow_1=pd.read_csv(path1+r'\borrow_test.txt',header=None,error_bad_lines=False)
dorm_1=pd.read_csv(path1+r'\dorm_test.txt',header=None)
ID=pd.read_csv(path1+r'\studentID_test.txt',header=None)
card.columns=['id','consume','where','how','time','amount','remainder']
lib.columns=['id','door','time']
borrow_1.columns=['id','time','book_name','book_num']
dorm_1.columns=['id','time','direction']

ID.columns=['id']
# y_pb=np.arange(10783)
# y_pb=pd.DataFrame(y_pb,index=ID.id)
#
# # result=pd.merge(ID,y_pb)
# print(y_pb)

en=card.pivot_table('amount',index='id',columns='how',aggfunc=sum)
en['engeer']=en['食堂']/en.sum(axis=1)
en=en.engeer.fillna(0)
en=pd.DataFrame(en)
lib.drop_duplicates('time',keep='first')
lib.time=lib.time.str[:10]
lib=lib.drop_duplicates(['id','time'],keep='first')
lib=lib.groupby('id').time.count()
lib=pd.DataFrame(lib)
lib.columns=['lib_count']
lib.lib_count=lib.lib_count/lib.lib_count.mean()

borrow_1=borrow_1.groupby('id').book_name.count()
borrow_1=pd.DataFrame(borrow_1)
borrow_1.columns=['book_count']
borrow_1.book_count=borrow_1.book_count/borrow_1.book_count.mean()


dorm_1=dorm_1.groupby(['id']).direction.mean()
dorm_1=pd.DataFrame(dorm_1)
dorm_1.columns=['iorate']



engeer=pd.read_csv(path+r'\train\card.csv',encoding='gbk')
engeer=engeer.set_index('id')
engeer=engeer.drop(['食堂','总计'],axis=1)
engeer.columns=['engeer']
lib_count=pd.read_csv(path+r'\train\lib_count.csv',header=None)
lib_count.columns=['id','lib_count']
lib_count=lib_count.set_index('id')
lib_count.lib_count=lib_count.lib_count/lib_count.lib_count.mean()
subsidy=pd.read_csv(path+r'\train\subsidy_train.txt',sep=',',header=None)
subsidy.columns=['id','amount']
subsidy=subsidy.set_index('id')
sub_label=subsidy.where(subsidy.amount!=1000,1)
sub_label=sub_label.where(subsidy.amount!=1500,2)
sub_label=sub_label.where(subsidy.amount!=2000,3)
subsidy1=sub_label
subsidy=subsidy1[subsidy1.amount>0]
score=pd.read_csv(path+r'\train\score_train.txt',sep=',',header=None)
score.columns=['id','dep','range']
score=score.set_index('id')
# data=pd.merge(pd.merge( pd.merge(subsidy,engeer,on='id'),lib_count,on='id'),score,on='id')
# score_prop=data.loc[:,['dep','range']]
# score_prop=score_prop.groupby(['dep']).count()
# s_prop=score.groupby('dep').count()
# print(score_prop/s_prop)
# print(score,subsidy1)
borrow=pd.read_csv(path+r'\train\borrow_train.txt',sep=',',header=None,error_bad_lines=False)
borrow.columns=['id','borrow_time','book_name','book_num']
borrow=borrow.set_index('id')
bg=borrow.groupby('id').book_name.count()
bg=pd.DataFrame(bg)
bg.columns=['book_count']
bg.book_count=bg.book_count/bg.book_count.mean()
dorm=pd.read_csv(path+r'\train\dorm_train.txt',sep=',',header=None)
dorm.columns=['id','time','direction']
dorm=dorm.set_index('id')
dorm.time=dorm.time.str[:10]
dg=dorm.groupby(['id']).direction.mean()
dg=pd.DataFrame(dg)
dg.columns=['iorate']
# print(data,bg)
train=pd.merge(pd.merge(pd.merge( pd.merge(subsidy1,engeer,on='id'),lib_count,on='id'),bg,on='id'),dg,on='id')
test=pd.merge(pd.merge(pd.merge(en,lib,on='id'),borrow_1,on='id'),dorm_1,on='id')

train.to_csv(path1+r'\train.csv',encoding='gbk')
test.to_csv(path1+r'\test.csv',encoding='gbk')

