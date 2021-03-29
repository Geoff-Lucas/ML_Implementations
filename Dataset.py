# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 21:04:22 2021

@author: Geoff
"""

import pandas as pd


class dataset():
    
    def __init__(self, file_loc, target):
        
        self.file_location = file_loc
        self.dataset_df = pd.read_csv(file_loc)
        self.target = target
        
        temp = file_loc.split("\\")
        self.dataset_name = temp[-1]
        self.dataset_len = len(self.dataset_df)
        
    def infer_datatypes(self):
        
        self.dataset_dtypes = {}
        dtypes = self.dataset_df.dtypes
        
        for index, dtype in zip(dtypes.index.tolist(), dtypes):
            
            if dtype == "object" or dtype == 'string':
                self.dataset_dtypes[index] = "string"
        
            elif dtype.startswith("int"):
                self.dataset_dtypes[index] = "int"
                
            elif dtype.startswith("float"):
                self.dataset_dtypes[index] = "float"
                
            elif dtype == 'datetime64':
                self.dataset_dtypes[index] = 'datetime'
            
            else:
                self.dataset_dtypes[index] = dtype
                
    def print_dataset_types(self):
        
        print(f"\nDatatypes for dataset: {self.df_name}\n")
        
        for i, (var_name, var_type) in enumerate(self.dataset_dtypes.items()):
            print(f"{i}) {var_name:30}  {var_type}")
            
            
    def change_target():
        pass
    
    def change_dataset_types():
        pass
    
    def 
        
        
        
        
        
        
        
        
        
file_loc = r'C:\Users\Geoff\ML_Implementations\data\breast_cancer_train.csv'
target = "class"





        
        
