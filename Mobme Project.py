# -*- coding: utf-8 -*-
# https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
"""
Created on Mon Feb 18 14:49:29 2019

@author: User
"""
## Importing Libraries 
# Load libraries
import sys
import scipy
import numpy
import matplotlib
import pandas
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
#\
# importing data as pandas
# https://www.dataquest.io/blog/excel-and-pandas/
location = 'Model13_.xlsx'
dataset = pandas.read_excel(location)
dataset.head()
dataset_new = pd.DataFrame(dataset)
Y = dataset_new.iloc[:, 0:1]
X = dataset_new.iloc[:, 1:13]

validation_size = 0.20
seed=7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)


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


scoring = 'accuracy'



# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))
# evaluate each model in turn
models
results = []
names = []
for name, model in models:
	kfold = model_selection.KFold(n_splits=10, random_state=seed)
	cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
	results.append(cv_results)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)
