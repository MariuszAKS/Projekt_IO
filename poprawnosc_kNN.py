import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestClassifier


# importuje plik z danymi
cechy = pd.read_csv("cechy40.csv", decimal=".", sep=";")
Y = cechy["-- Rodzaj --"]
X = cechy.drop(["-- Rodzaj --", "-- Numer --"], axis=1)
licznik = 0


for i in range(0, len(X)):
    # odrzucam z modelu trenującego i-ty wiersz i zapisuje go do zmiennej X_test
    X_test = X.iloc[i]
    trenujacy_X = X.drop([i], axis=0)
    trenujacy_Y = Y.drop([i], axis=0)

    # model testujacy
    X_test = X_test.values
    # model trenujacy
    X_Train = trenujacy_X.values
    Y_Train = trenujacy_Y.values

    # algorytm kNN dla n = 3
    knn = KNeighborsRegressor(n_neighbors=3)
    knn.fit(X_Train, Y_Train)
    y_przewidywany = knn.predict([X_test])
    for j in range(len(y_przewidywany)):
        y_przewidywany[j] = round(y_przewidywany[j], 0)

    if y_przewidywany[0] == Y[i]:
        licznik += 1
print("Ilosc poprawnych dopasowan wynosi: ", licznik)
print("Poprawnosc wynosi: ", licznik/127*100, '%')