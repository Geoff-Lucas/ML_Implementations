# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 17:41:57 2021

@author: Geoff
"""

import unittest
import pandas as pd
import NaiveBayes

class TestNaiveBayes(unittest.TestCase):
    
    def __init__(self, *args, **kwargs):
        super(TestNaiveBayes, self).__init__(*args, **kwargs)
        
        self.dataset1 = pd.DataFrame(
            [['a', 'c', 'f'],
             ['a', 'c', 'f'],
             ['a', 'd', 'f'],
             ['b', 'd', 'g'],
             ['b', 'e', 'h']],
            columns = ['Var1', 'Var2', 'target'])  
        
        self.dataset2 = pd.DataFrame(
            [['a', 'c'],
             ['a', 'c'],
             ['b', 'd']],
            columns = ['Var1', 'Var2'])
        
        self.tester = NaiveBayes.NaiveBayes()
        self.tester.train(self.dataset1, 'target')
        
    def test_estimate_probability(self):
        
        results = [[('f', 0.5714285714285715),
                         ('g', 0.2142857142857143),
                         ('h', 0.2142857142857143)],
                        [('f', 0.5714285714285715),
                         ('g', 0.2142857142857143),
                         ('h', 0.2142857142857143)],
                        [('f', 0.03571428571428571),
                         ('g', 0.6428571428571428),
                         ('h', 0.3214285714285714)]]
        
        self.assertEqual(self.tester.estimate_probability(self.dataset2), results)
        
    def test_predict(self):
        self.assertEqual(self.tester.predict(self.dataset2), ['f', 'f', 'g'])
        
if __name__ == '__main__':
    unittest.main()
    
    
    
    
