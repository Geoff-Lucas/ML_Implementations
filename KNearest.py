# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 18:00:11 2021

@author: Geoff
"""


import pandas as pd
from Algorithm import Algorithm

##################
# Training
##################

class KNearest(Algorithm):
    
    def __init__(self):
        super().__init__()
    
    def train(self, df, target):
        
        # For K-Nearest Neighbor, basically just store the dataset for now
    
        self._columns = df.columns.tolist()
        self._target = target
        self._columns.remove(self._target)
        self._classes = df[target].unique()
        self._df = df
        self._target_col_index = self._df.columns.get_loc(target)
        self._classes = self._df[target].unique().tolist()
        self._columns_lookup = {col:i for i, col in enumerate(self._columns)}
        
        # TODO: Look at adding the ability to segment the dataset into multiple sections
        # TODO: Add basic ability to differentiate between categorical vars and likely numeric vars (maybe form is numeric && > 15 unique values)
        
    def estimate_probability(self, df):
        print("K-Nearest Neighbor does not output probabilities.")
    
    def predict(self, df_to_predict, k):
        
        def sort_key(dist):
            return dist[0]
        
        predictions = []
        df_predict_cols = df_to_predict.columns.tolist()
        
        # Check to make sure col to predict isn't included in dataset
        if self._target in df_predict_cols:
            df_to_predict.drop(self._target, axis = 1, inplace = True)
            df_predict_cols.remove(self._target)
            
        order = []
        for col in df_predict_cols:
            order.append(self._columns.index(col))
        
        for row in df_to_predict.itertuples(index = False):
            distances = []
                        
            for obs in self._df.itertuples(index = False):
                distance = 0
            
                for i, col in enumerate(row):
                    # TODO: Handle numeric variables differently
                    if col != obs[order[i]]: 
                        distance += 1
                
                distances.append((distance, obs[self._target_col_index]))
                
            distances.sort(key = sort_key)
            
            k_neighbors = distances[:k]
            
            classes = []
            for neighbor in k_neighbors:
                classes.append(neighbor[1])
                
            highest = 0
            prediction = None
            for c in self._classes:
                if classes.count(c) > highest: 
                    highest = classes.count(c)
                    prediction = c
                
            predictions.append(prediction)
            
        return predictions




df = pd.read_csv(r'C:\Users\Geoff\ML_Implementations\data\bikes_nominal.csv')
target = "type"
        
NB = KNearest()
NB.train(df, target)
test_df = df.copy()
NB.predict(test_df, 3)
