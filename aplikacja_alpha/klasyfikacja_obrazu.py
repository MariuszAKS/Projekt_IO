# -*- coding: utf-8 -*-
"""
@package docstring
"""
import pandas as pd
import numpy as np
import random
from sklearn.ensemble import RandomForestClassifier

from typing import List


def klasyfikacja(cechy_obrazu: List) -> int:
    """
    Metoda służąca do przewidywania rodzaju bakterii dla danego obrazu z użyciem wytrenowanego modelu
    :param cechy_obrazu: Przechowuje cechy obrazu, który chcemy sklasyfikować (przyporzadkować do jednego rodzaju bakterii)
    :return: Numer przyporządkowanego rodzaju bakterii
    """
    cechy = pd.read_csv(r"aplikacja_alpha/40cech.csv", decimal=",", sep=";")

    # model treningowy: X to dataframe tylko z cechami (bez rodzaju bakterii i numeru zdjęcia), y to numery rodzajów
    x_train = np.array((cechy.drop(cechy.columns[[0, 1]], axis=1)))
    y_train = np.array(cechy["-- Rodzaj --"])

    #klasyfikator rf
    random.seed(100)
    clf = RandomForestClassifier(n_estimators=100, random_state=100)
    clf.fit(x_train, y_train)

    #przewidywany rodzaj na podstawie danych testowych
    print(cechy_obrazu)
    print(x_train)
    X_test = cechy_obrazu
    y_przewidywany = clf.predict(X_test)

    return y_przewidywany[0]
