# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 17:27:22 2021

@author: Geoff
"""

import pandas as pd
from Algorithm import Algorithm

##################
# Training
##################


class NaiveBayes(Algorithm):
    
    def __init__(self):
        pass
    
    def train(self, df, target):
    
        self._columns = df.columns.tolist()
        self._target = target
        
        self._counts = {}
        self._totals = {}
            
        self._columns_lookup = {col:i for i, col in enumerate(self._columns)}
            
        self._columns.remove(self._target)
        self._classes = df[target].unique()   
        
        # TODO: Add basic ability to differentiate between categorical vars and likely numeric vars (maybe form is numeric && > 15 unique values)
        
        # TODO: Add ability to record mean / std for numeric vars
        
        # Record the totals
        for clas in self._classes:
            reduced = df[df['class'] == clas]
        
            for col in self._columns:
                values = reduced[col].value_counts()
                # Note: I'm summing each col individually incase there are NAs in the
                # data, so this will purposely discount them
                self._totals[clas, col] = values.sum(skipna = True)
                
                for level, value in zip(values.index, values):
                    self._counts[clas, col, level] = value


    def estimate_probability(self, df):
        
        class_conditional_probs_for_dataset = []
        
        for row in df.itertuples(index = False):
            class_conditionals_for_row = []
        
            for clas in self._classes:
                class_conditional_prob = 1
                
                for col in self._columns:
                    
                    # TODO: add ability to estimate numeric variable based on Gaussian Distribution
                    class_conditional_prob *= self._counts.get((clas, col, row[self._columns_lookup.get(col)]), .5) / self._totals[clas, col]
                    
                class_conditionals_for_row.append((clas, class_conditional_prob))
            
            class_conditional_probs_for_dataset.append(class_conditionals_for_row)
            
        # Normalizing to probabilities
        normalized_conditionals = []
        
        for row in class_conditional_probs_for_dataset:
            temp = 0
            new_row = []
            
            for pair in row:
                temp += pair[1]
                
            for pair in row:
                new_row.append((pair[0], pair[1] / temp))
                
            normalized_conditionals.append(new_row)
        
        return normalized_conditionals
    
    def predict(self, df):
        
        predictions = []
        normalized_conditionals = self.estimate_probability(df)
        
        for row in normalized_conditionals:
            highest, pred = 0, ''
            
            for clas in row:
                if clas[1] > highest:
                    highest = clas[1]
                    pred = clas[0]
                
            predictions.append(pred)
            
        return predictions
                    
    
    
        
df = pd.read_csv(r'C:\Users\Geoff\ML_Implementations\data\breast_cancer_train.csv')
target = "class"        
        
NB = NaiveBayes()
NB.train(df, target)
NB.estimate_probability(df.head())
NB.predict(df[220:227])
