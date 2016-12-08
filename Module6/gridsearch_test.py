# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 12:08:30 2016

@author: Andrew
"""

from scipy.stats import uniform
from scipy.stats import norm
 
from sklearn.grid_search import RandomizedSearchCV
from sklearn import metrics
 
# Designate distributions to sample hyperparameters from 
n_estimators = np.random.uniform(70, 80, 5).astype(int)
max_features = np.random.normal(6, 3, 5).astype(int)
 
# Check max_features>0 & max_features<=total number of features
max_features[max_features <= 0] = 1
max_features[max_features > X.shape[1]] = X.shape[1]
 
hyperparameters = {'n_estimators': list(n_estimators),
                   'max_features': list(max_features)}
 
print (hyperparameters)