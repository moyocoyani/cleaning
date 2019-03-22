import numpy pandas as pd
import numpy as np

#You open some dataset, and it comes with a summary for the size; number of columns;
#how many features have null values, and where are them; and information about duplicates

def characterizingDF(df):
    print('The dataset has ',len(df), ' total rows')
    print('The dataset has ',len(df.columns), ' total columns')
    print('These are the variables and their types ', df.dtypes)
    print('This where you can find null values:\n',df.isnull().sum(axis=0))
    print('You have',len(df[df.duplicated(keep=False)]),'duplicates')
    print('And these are the duplicate rows',df[df.duplicated(keep=False)])
