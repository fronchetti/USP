#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Felipe Fronchetti'
__contact__ = 'fronchetti@usp.br'

from sklearn.model_selection import GridSearchCV
from sklearn.multiclass import OneVsRestClassifier
from sklearn.multiclass import OneVsOneClassifier
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import StratifiedKFold
from imblearn.pipeline import Pipeline

def hyperparameters_tuning(classifier, hyperparameters, strategy, oversample, X_train, y_train):
    pipeline_args = []

    if oversample:
        oversample = ('smt', SMOTE())
        pipeline_args.append(oversample)

    if strategy == 'one-vs-rest':
        strategy = ('clf', OneVsRestClassifier(classifier))

    if strategy == 'one-vs-one':
        strategy = ('clf', OneVsOneClassifier(classifier))

    pipeline_args.append(strategy)
    pipeline = Pipeline(pipeline_args)

    cross_validation = StratifiedKFold(n_splits=10)
    model = GridSearchCV(classifier, hyperparameters, scoring="f1_weighted", cv=cross_validation)
    model.fit(X_train, y_train)

    return model.best_params_
