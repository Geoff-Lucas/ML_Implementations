# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 19:41:39 2021

@author: Geoff
"""

import unittest
import pandas as pd
import KNearest

class TestKNN(unittest.TestCase):
    
    def __init__(self, *args, **kwargs):
        super(TestKNN, self).__init__(*args, **kwargs)
        
        self.dataset1 = pd.DataFrame(
            [['a', 'c', 'f'],
             ['a', 'c', 'f'],
             ['a', 'd', 'f'],
             ['b', 'd', 'g'],
             ['b', 'e', 'h'],
             ['b', 'd', 'g']],
            columns = ['Var1', 'Var2', 'target'])  
        
        self.dataset2 = pd.DataFrame(
            [['a', 'c'],
             ['a', 'c'],
             ['b', 'd']],
            columns = ['Var1', 'Var2'])
        
        self.tester = KNearest.KNearest()
        self.tester.train(self.dataset1, 'target')
        
    def test_predict(self):
        self.assertEqual(self.tester.predict(self.dataset2, 2), ['f', 'f', 'g'])
        
if __name__ == '__main__':
    unittest.main()
    
    