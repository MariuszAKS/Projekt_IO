# -*- coding: utf-8 -*-

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn import metrics
#importuję plik z cechami do dataframe
cechy = pd.read_csv("cechy.csv", decimal=".", sep=";")
#usuwam dwie pierwsze kolumny, aby zostały tylko komulny z cechami
X = cechy.drop(["-- Rodzaj --", "-- Numer --"], axis=1)
X = X.values
y = cechy["-- Rodzaj --"]
y = y.values
#dzielę zbiory na podzbiór treningowy i podzbiór testowy
X_Train, X_Test, y_Train, y_Test = train_test_split(X, y, test_size=0.5)
#klasyfikacja kNN
knn = KNeighborsRegressor(n_neighbors=3)
knn.fit(X_Train, y_Train)
#przewidywany rodzaj
y_przewidywany = knn.predict(X_Train)
print(y_przewidywany)
for i in range(len(y_przewidywany)):
    y_przewidywany[i] = round(y_przewidywany[i], 0)
# accuracy (zgodność dopasowania)
print("Accuracy:", metrics.accuracy_score(y_Test, y_przewidywany))

