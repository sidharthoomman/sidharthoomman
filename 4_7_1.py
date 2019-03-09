# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 23:06:58 2019

@author: User
"""
df=[]
import numpy
import pandas as pd
file='MockCallCenterData.csv'
data=pd.read_csv(file)
df=pd.DataFrame(data)
df.head()
# Adding a category 
df['Category']= df['ResponseId']
cols=len(df.columns)
rows=len(df.index)

df1=[]
df1=pd.DataFrame()
x=0        
while(x<rows):
        temp=len(str(df.iloc[x][17]))
        if temp==3:
                df1 = df1.append(pd.DataFrame(['CGP'], index = [x], columns=['Cat']))
        if temp==4:
                df1 = df1.append(pd.DataFrame(['HFG'], index = [x], columns=['Cat']))
        if temp==5:
                df1 = df1.append(pd.DataFrame(['INCG'], index = [x], columns=['Cat']))
        if temp==6:
                df1 = df1.append(pd.DataFrame(['INTGROUP'], index = [x], columns=['Cat']))
        x=x+1
        
df = pd.merge(df,df1, on=df.index, how='inner')
export_csv = df.to_csv (r'C:\Users\User\BeWorks\df.csv', index = None, header=True)
export_csv = df1.to_csv (r'C:\Users\User\BeWorks\df1.csv', index = None, header=True)

import matplotlib.pyplot as plt

# code to increase display size
import pandas as pd
pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
print(df.groupby('Cat').size())
boxplot= df.boxplot(column=['Q17_1_Cares','Q19_1_highQ','Q21_1_favop'],by=['Cat'])

list(df.columns.values)

import numpy
import pandas
import scipy

#############setting up ANNOVA modeling #############3
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# idea junkyar
cw_lm_cares=ols('Q17_1_Cares ~ C(Cat) + C(Q39_elec) + C(Q39_1_thermos) + C(Q57_edu) + C(Q55_salary) + C(Q38_gender) + C(Q36_age) + C(Q10_organic) + C(Q5_socks)', data=df).fit() #Specify C for Categorical
cw_lm_product=ols('Q19_1_highQ ~ C(Cat) + C(Q39_elec) + C(Q39_1_thermos) + C(Q57_edu) + C(Q55_salary) + C(Q38_gender) + C(Q36_age) + C(Q10_organic)  + C(Q5_socks)', data=df).fit() #Specify C for Categorical
cw_lm_recommend=ols('Q21_1_favop ~ C(Cat) + C(Q39_elec) + C(Q39_1_thermos) + C(Q57_edu) + C(Q55_salary) + C(Q38_gender) + C(Q36_age) + C(Q10_organic) + C(Q5_socks)', data=df).fit() #Specify C for Categorical

print(cw_lm_cares.summary())
print(cw_lm_product.summary())
print(cw_lm_recommend.summary())
'''
1. Dont do fitness of test
https://stackoverflow.com/questions/25537399/anova-in-python-using-pandas-dataframe-with-statsmodels-or-scipy
'''