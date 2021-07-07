
import pandas as pd
import numpy as np


def missing (df,col,n1,n2):

    for c in col:
        
        df[c] = df.loc[df[c]].replace({c: {n1:np.nan, n2:np.nan}})
        
        na_ratio_1 = ((df[c].isnull().sum() / len(df[c]))*100)
        print (f'c: {na_ratio_1}')

        if na_ratio_1 > 0.0:
            df[c].fillna(df[c].mode()[0], inplace=True)
            na_ratio_2 = ((df[c].isnull().sum() / len(df[c]))*100)
            
            return na_ratio_2







    