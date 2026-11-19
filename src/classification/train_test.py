import numpy as np
import pandas as pd
from sklearn.ensemble import (RandomForestClassifier,GradientBoostingClassifier,HistGradientBoostingClassifier)
from sklearn.model_selection import train_test_split

data = pd.read_csv('../data/cupid_algorithm_dataset.csv',)
y = data["compatible"]
x = data.drop(columns=[
        "compatible",
        "compatibility_score",
        "relationship_longevity_months",
        "pair_id",])
x = pd.get_dummies(x)
x_train, x_test, y_train, y_test  = train_test_split(x, y, test_size=0.25, random_state=42)

def train_arbre_aleatoire():

    modele_rf = RandomForestClassifier(
        n_estimators=200, 
        criterion='gini',
        max_depth=12,
        min_samples_split=2,
        min_samples_leaf=20,
        min_weight_fraction_leaf=0.0,
        max_features='sqrt',
        max_leaf_nodes=None,
        min_impurity_decrease=0.0,
        bootstrap=True,
        oob_score=False,
        n_jobs=None,
        random_state=None,
        verbose=0,
        warm_start=False,
        class_weight=None,
        ccp_alpha=0.0,
        max_samples=None,)

    return(modele_rf.fit(x_train, y_train))


def train_GBM():
    modele_gbm = GradientBoostingClassifier(
        loss='log_loss',
        learning_rate=0.1,
        n_estimators=100,
        subsample=1.0,
        criterion='deprecated',
        min_samples_split=2,
        min_samples_leaf=1,
        min_weight_fraction_leaf=0.0,
        max_depth=3,
        min_impurity_decrease=0.0,
        init=None,
        random_state=None,
        max_features=None,
        verbose=0,
        max_leaf_nodes=None,
        warm_start=False,
        validation_fraction=0.1,
        n_iter_no_change=None,
        tol=0.0001,
        ccp_alpha=0.0)

    return(modele_gbm.fit(x_train, y_train))


def train_HGBC():
    modele_hgbc = HistGradientBoostingClassifier(
        loss='log_loss',
        learning_rate=0.1,
        max_iter=100,
        max_leaf_nodes=31,
        max_depth=None,
        min_samples_leaf=20,
        l2_regularization=0.0,
        max_bins=255,
        categorical_features=None,
        monotonic_cst=None,
        warm_start=False,
        early_stopping=True,
        scoring='loss',
        validation_fraction=0.1,
        n_iter_no_change=10,
        tol=1e-07,
        verbose=0)

    return(modele_hgbc.fit(x_train, y_train))
