# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 18:14:05 2021

@author: Geoff
"""

import unittest
import testing_scripts.test_NB as nb_test_script
import testing_scripts.test_KNN as knn_test_script

def suite():
    suite = unittest.TestSuite()
    
    # Naive Bayes Unit Tests
    suite.addTest(nb_test_script.TestNaiveBayes('test_estimate_probability'))
    suite.addTest(nb_test_script.TestNaiveBayes('test_predict'))
    
    # K Nearest Neighbors Unit Tests
    suite.addTest(knn_test_script.TestKNN('test_predict'))
    
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())