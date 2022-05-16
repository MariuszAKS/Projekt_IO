# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

def klasyfikacja(cechy_obrazu):
    cechy = pd.read_csv(r"40cech.csv", decimal=",", sep=";")

    # model treningowy: X to dataframe tylko z cechami (bez rodzaju bakterii i numeru zdjęcia), y to numery rodzajów
    x_train = np.array((cechy.drop(cechy.columns[[0, 1]], axis=1)))
    y_train = np.array(cechy["-- Rodzaj --"])

    #klasyfikator rf
    clf = RandomForestClassifier(n_estimators=100)
    clf.fit(x_train, y_train)

    #przewidywany rodzaj na podstawie danych testowych
    X_test = cechy_obrazu
    y_przewidywany = clf.predict(X_test)

    return y_przewidywany