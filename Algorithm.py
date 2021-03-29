# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 20:55:11 2021

@author: Geoff
"""

# This isn't really super useful right now, but I want to provide for a 
# common API for future use.

from abc import ABC, abstractmethod

class Algorithm(ABC):
    
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def train(self, df, target):
        pass
    
    @abstractmethod
    def estimate_probability(self, df):
        pass
    
    @abstractmethod
    def predict(self, df_to_predict):
        pass