# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 21:04:22 2021

@author: Geoff
"""

import pandas as pd


class Dataset():
    
    def __init__(self, file_loc, target):
        
        self.file_location = file_loc
        self.dataset_df = pd.read_csv(file_loc)
        self.target = target
        
        temp = file_loc.split("\\")
        self.dataset_name = temp[-1]
        self.dataset_len = len(self.dataset_df)
        
        self.infer_datatypes()
        
        
    def infer_datatypes(self):
        
        self.dataset_dtypes = {}
        dtypes = self.dataset_df.dtypes
        
        for index, dtype in zip(dtypes.index.tolist(), dtypes):
                        
            if dtype == "object" or dtype == "str":
                self.dataset_dtypes[index] = "string"
        
            elif str(dtype).startswith("int"):
                self.dataset_dtypes[index] = "int"
                
            elif str(dtype).startswith("float"):
                self.dataset_dtypes[index] = "float"
                
            elif dtype == 'datetime64':
                self.dataset_dtypes[index] = 'datetime'
            
            else:
                self.dataset_dtypes[index] = dtype
                
    def dataset_change_controller(self):
        pass
                
                
    def print_dataset_types(self):
        
        print(f"\nDatatypes for dataset: {self.dataset_name}")
        print(f"Current target is: {self.target}\n")
        
        for index, (var_name, var_type) in enumerate(self.dataset_dtypes.items()):
            print(f"{index}) {var_name:30}  {var_type}")
            
        print("\nOptions:\na) Change Target Variable\nb) Change Variabe Type\nc) Continue to Algorithm\n")
            
    def change_target(self):
        var_choice = input("Which variable should the new target be? ")
        
        while var_choice.lower() != 'q':
        
            try:
                self.target = list(self.dataset_dtypes)[int(var_choice)]
                break
                    
            except:
                var_choice = ("That selection is not valid, please type the number of the variable to change the target to or Q to quit: ")
        
    def change_dataset_types(self):
        
        list_of_dtypes = ['string', 'int32', 'int64', 'float32', 'float64', 'datetime64']
        dtypes_dict = {(i + 1):dtype for i, dtype in enumerate(list_of_dtypes)}
        
        user_input = input("Which variable should be changed? ")
        
        while user_input.lower() != 'q':

            try:
                column_to_change = list(self.dataset_dtypes)[int(user_input)]
                break
                    
            except:
                user_input = input("That selection is not valid, please type the number of the variable to change or Q to quit: ")
            
        while user_input.lower() != 'q':
            
            print("Variable options are \n1) string \n2) int32 \n3) int64 \n4) float32 \n5) float64 \n6) datetime")
            user_input = input(f"Please enter the type of variable {column_to_change} should be: ")
            
            try:
                var_dtype = int(user_input)
                if var_dtype < 1 or var_dtype > 6:
                    raise Exception("Out of range of inputs.")
                
                break
            
            except:
                pass
            
        self.dataset_df = self.dataset_df.astype({column_to_change:dtypes_dict.get(var_dtype)})         
        self.dataset_dtypes[column_to_change] = dtypes_dict.get(var_dtype)
    
    def scale_dataset():
        pass
        
        
        
        
        
        
        
        
        
file_loc = r'C:\Users\Geoff\ML_Implementations\data\breast_cancer_train.csv'
target = "class"

data = Dataset(file_loc, target)
data.print_dataset_types()
data.change_target()
data.target
data.print_dataset_types()
data.change_dataset_types()        
data.dataset_df.dtypes
