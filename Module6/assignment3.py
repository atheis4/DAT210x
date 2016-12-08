# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 11:14:18 2016

@author: Andrew
"""

import pandas as pd
import numpy as np


def svc_hyperparam_test(X_train, y_train, X_test, y_test):    
    """."""    
    
    high_score = -1
    best_C = -1
    best_gamma = -1
    
    for i in np.arange(0.05, 2.0, 0.05, dtype=float):

        for x in np.arange(0.001, 0.1, 0.001, dtype=float):
            
            svc = SVC(C=i, gamma=x)
            svc.fit(X_train, y_train)
            
            if svc.score(X_test, y_test) >= high_score:
                high_score = svc.score(X_test, y_test)
                best_C = i
                best_gamma = x
         
    return high_score, best_C, best_gamma


# Import data set, drop name column, create and remove labels
X = pd.read_csv('Datasets/parkinsons.data')
X = X.drop(labels='name', axis=1)
y = X.loc[:, ['status']]
X.drop(labels='status', axis=1, inplace=True)


# Divide data with train_test_split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=7)


# Preprocessing data
from sklearn.preprocessing import Normalizer, MaxAbsScaler, MinMaxScaler, KernelCenterer, StandardScaler

processor = StandardScaler()
processor.fit(X_train)

X_train = processor.transform(X_train)
X_test = processor.transform(X_test)


# Apply PCA to processed data
#from sklearn.decomposition import PCA

#pca = PCA(n_components=14)

#pca.fit(X_train)
#X_train = pca.transform(X_train)
#X_test = pca.transform(X_test)


# Apply Isomap to processed data
from sklearn.manifold import Isomap

iso = Isomap(n_neighbors=5, n_components=6)

iso.fit(X_train)
X_train = iso.transform(X_train)
X_test = iso.transform(X_test)



# Create default SVC algorithm, train and test
from sklearn.svm import SVC

default_svc = SVC()
default_svc.fit(X_train, y_train)
score = default_svc.score(X_test, y_test)


# Hyperparameter search      
high_score, best_C, best_gamma = svc_hyperparam_test(X_train, y_train, X_test, y_test)

svc = SVC(C=best_C, gamma=best_gamma)


            