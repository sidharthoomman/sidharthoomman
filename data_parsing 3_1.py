''' 
Developer Notes   
2/28  Line 38 Working  

'''


# Step 1 import file 
#importing numpy for checking datatype of a 
#data_list (Column number, name, data, missing data, correlation with Y)
import numpy
import pandas as pd
file = 'Model2.xlsx'
datax = pd.read_excel(file)
datax_frame = pd.DataFrame(datax)
num_cols = len(datax_frame.columns)
num_rows = len(datax_frame.index)
del data_list
data_list = []
# ---------------------------------------------------------------------- #
# Data Type Check - goes column by column 
# manually input datatype of each column 
#data_list (Column number, name, data_type, data, missing data, correlation with Y)
data_backup = pd.DataFrame()
x = 0
y = 0
x=x+1
# counter to check if there are more than 1 datatype
              # ------------------------------------------------------------------------ # 
# Step 1 : QA - Check if d
datax.head()
datax_frame.head()

data_list

## Step 3bAppeneding Column number and name, creating blank list file
## ----y = datax_frame.iloc[0,0]
# erroring out append with this loop - check if vairables are passing through 
data_list
z = 0
while(z < num_cols):
    y = datax_frame.columns[z] #taking the column name  
    print("Value of z is:", z)
    print("Value of y is:", y)
    a=input("Enter data type of Col: %s", %y) # manually inputting datatype of a col
    data_list.append([z,y,a,0,0,0])# appending column name
   
    z = z + 1 
# QA data_list
data_list[0:72]

# Null and total data counter counter 
z = 0 # null counter
x = 0               
while (x < num_rows):
    y = 0    
    while(y < num_cols):
        temp = datax_frame[x][y]
        if datax_frame[x][y] is null:
            z = z + 1
        y=y+1
    temp=data_list[x]
    not_null=num_cols-z
    data_list.pop([x])
    data_list.append([temp[0],temp[1],temp[2],z,not_null,0])
    x=x+1

# importing SQL library 
from sql import *
# Correlation Step 
{create volatile table1 
     as sel * from data_frame;
 x=0 = # col counter
 while(x<num_cols):
    a = datax_frame[x][1]
    y = data_frame[x][0]
    create volatile table2 
        as sel a,y from datax_frame
        where a=!'Null' and b=!'Null';
    df=pd.DataFrame(table1)
    
    s_corr = df.col_2.str.get_dummies(dummy_na=True)).corrwith(df.Score/df.Score.max())
    temp=data_list[x]
    data_list.pop([x])
    data_list.append([temp[0],temp[1],temp[2],temp[3],temp[4],s_corr])
    x=x+1

 # Makes sure new_list has columns seperated out as  columns = ['Sentence','Score'])
             '''
             df = pd.DataFrame([ ["hello there", 100],
                            ["hello kid",   95],
                    ["there kid",   5]
                    ], columns = ['Sentence','Score'])
            '''
            
''' Notes: get dummies converts categorial vairables into dummy variables
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.get_dummies.html
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.get_dummies.html
s_corr gives another list -so choose the max from it and set the condition
get_dummies prints out dummy values that can be held out for correlation analysis
dummy_na is True 
Score/Score Max gives correlation for dummy values 
'''

#Step 4 cleaning up the data: 
#data_list (Column number, name,data_type, data, missing data, correlation with Y) 
while (x<n_rows):
    if (data_list[x][2]/data_list[x][3] <0.25): #deleting column with less than 25 %data
        d
            
# counter to check if there are more than 1 datatype
# ------------------------------------------------------------------------ # 
