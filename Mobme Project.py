# -*- coding: utf-8 -*-
# https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
"""
Created on Mon Feb 18 14:49:29 2019
Notes: 11:55 PM 
@author: User
"""

import sys
import scipy
import numpy
import matplotlib
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# https://www.dataquest.io/blog/excel-and-pandas/
location = 'File.xlsx'
data = pandas.read_excel(location)
data.head()
df = pd.DataFrame(data)
df1=[]
df.columns[1]
num_cols = len(df.columns)
num_rows = len(df.index)
# Add datacolumns for converting text to dummy variables in python

#loop to limit max length of a column
'''
df.columns
while (c in df.columns):   
    df_col_len = int(df[c].str.encode(encoding='utf-8').str.len().max())
    df_col_len        
x=0
df_col_len=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
df_col_len[2] = int(df['CUSTOMER_LOCATION'].str.encode(encoding='utf-8').str.len().max())
df_col_len[3] = int(df['CUSTOMER_LANGUAGE'].str.encode(encoding='utf-8').str.len().max())
df_col_len[4] = int(df['BRAND'].str.encode(encoding='utf-8').str.len().max())
df_col_len[5] = int(df['ZONE'].str.encode(encoding='utf-8').str.len().max())
df_col_len[6] = int(df['CIRCLE'].str.encode(encoding='utf-8').str.len().max())
df_col_len[7] = int(df['REASON_FOR_CALL'].str.encode(encoding='utf-8').str.len().max())
df_col_len[8] = int(df['REASON_FOR_CALL_SUBTYPE'].str.encode(encoding='utf-8').str.len().max())
df_col_len

df.iloc[3][4]
while(x<num_cols):
    if df_col_len[x]>20:
        df.drop(df.columns[[x]], axis = 1, inplace=True) # axis 1 for columns
    x=x+1
'''
####Thumbs up #################
isinstance(df.columns[1],(str,object))
df.columns[1].dtype
x=0
y=0
df2=pd.DataFrame()
num_cols = len(df.columns)
while(x<num_cols):
    if(isinstance(df.iloc[x][2],(str,object))):
        y=y+1
    x=x+1
y
import pandas as pd
pd.concat([pd.get_dummies(df.)], axis=1, keys=df.columns)

df2=pd.concat([pd.get_dummies(df, columns=['PINCODE', 'AGENT_NETWORK','CELL_SITE_ID','TRANSACTION_DATE'])])
export_csv = df2.to_csv (r'C:\Users\user\Desktop\df2.csv', index = None, header=True)

#df3=pd.concat([pd.get_dummies(df2, columns=['CUSTOMER_LANGUAGE','CIRCLE','REASON_FOR_CALL','REASON_FOR_CALL_SUBTYPE'])], axis=1, keys=df2.columns)
#df3
#export_csv = df3.to_csv(r'C:\USers\User\af.csv', index = None, header=True)
location = 'df2.csv'
data = pandas.read_csv(location)
dataset_new = pd.DataFrame(data)
num_cols = len(dataset_new.columns)
num_rows = len(dataset_new.index)
num_rows
num_cols
# remove text variables


Y = dataset_new.iloc[:,7:8]
X = dataset_new.iloc[:,8:4815]

Y
X
#####################Thumbsup################################
validation_size = 0.20
seed=7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

'''
#Summarizing the dataset
#shape
print(dataset.shape)
#head
print(dataset.head(20))
# descriptions
print(dataset.describe())

# Stopped as data load is showing some errors

# Statistical summary 
print(dataset.describe())
#class distribution
#univariate plots



# histograms ---- need to refine the data make sub data sets for subplots
dataset.hist()
plt.show()

# histograms ---- need to refine the data before watching plots make sub data sets for subplots

dataset.hist()
plt.show()

# Multivariate Plots

# scatter plot matrix
scatter_matrix(dataset)
plt.show()

# scatter plot matrix
scatter_matrix(dataset)
plt.show()

dataset
'''

scoring = 'accuracy'



# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
#models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))
# evaluate each model in turn
models
results = []
names = []
output=[]
for name, model in models:
	kfold = model_selection.KFold(n_splits=10, random_state=seed)
	cv_results = model_selection.cross_val_score(model, X_train, Y_train.values.ravel(), cv=kfold, scoring=scoring)
	results.append(cv_results)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())


fig = plt.figure()
fig.suptitle('Alogirthm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()
