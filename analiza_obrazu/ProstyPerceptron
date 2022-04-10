import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score

# Klasa służąca to wytrenowania perceptronu
# na podstawie podanego pliku .csv (kompatybilne z plikiem cech na github)
# oraz wykorzystania go do klasyfikowania nowych zdjęc
# plik = sciezka do pliku

class ProstyPerceptron:
    def __init__(self,plik,rozdzielacz=';') -> None:
        self.dane = pd.read_csv(plik, delimiter=rozdzielacz,encoding='latin-1') 
        
    # trenuje model na podstawie podanych danych
    # oraz zwraca jego ACCURACY (0.00 - 1.00)
    def trenuj(self):    
        dane_labels = self.dane.loc[:,'-- Rodzaj --']
        dane_data = self.dane.drop(['-- Rodzaj --','-- Numer --'], axis=1) #ZMIENIĆ ZALEŻNIE OD NAZWY
        #utworzenie zestawów danych treningowych i uczących
        x_uczacy, x_testujacy, y_uczacy, y_testujacy = train_test_split(dane_data,dane_labels,test_size=0.2)
        #Standaryzacja danych wejsciowych
        self.sc = StandardScaler()
        self.sc.fit(x_uczacy)
        x_uczacy_standaryzacja = self.sc.transform(x_uczacy)
        x_testujacy_standaryzacja = self.sc.transform(x_testujacy)
        #perceptron
        self.prosty_perceptron = Perceptron(max_iter=1000, eta0=0.01, random_state = 1)
        self.prosty_perceptron.fit(x_uczacy_standaryzacja, y_uczacy)
        #predykcja klasy
        y_przewidziane = self.prosty_perceptron.predict(x_testujacy_standaryzacja)
        #sprawdzanie ACCURACCY modelu
        y_testujacy = np.array(y_testujacy)
                
        return '%.2f' % accuracy_score(y_testujacy, y_przewidziane)
        
    # Klasyfikuje zestawy cech w podanym pliku .csv jako typy bakterii
    # plik .csv powinien zawierac same cechy, bez numerów wierszy
    # plik = sciezka do pliku
    # rozdzielacz = czym rozdzielone sa cechy w pliku, domyslnie ';'
    # UWAGA Przed użyciem należy wytrenować model
    # za pomocą funkcji: trenuj()
    def klasyfikuj_csv(self, plik, rozdzielacz=';'):
        obiekty = pd.read_csv(plik, delimiter=rozdzielacz, encoding='latin-1')
        obiekty_standaryzacja = self.sc.transform(obiekty)
        klasa = self.prosty_perceptron.predict(obiekty_standaryzacja)
        return klasa
    
    # Klasyfikuje zestawy cech w podanym np.array (jednowymiarowym)
    # jako typ bakterii
    # array powinien zawierac same cechy, bez numerów wierszy
    # obiekt = np.array z cechami
    # UWAGA Przed użyciem należy wytrenować model
    # za pomocą funkcji: trenuj()
    def klasyfikuj_obiekt(self, obiekt):
        obiekt = obiekt.reshape(1,len(obiekt))
        obiekt_frame = pd.DataFrame(obiekt)
        obiekt_standaryzacja = self.sc.transform(obiekt_frame)
        klasa = self.prosty_perceptron.predict(obiekt_standaryzacja)
        return klasa
    
    # zwraca ile iteracji (epok) wykonał model podczas uczenia
    def podaj_ile_iteracji(self):
        return self.prosty_perceptron.n_iter_
    
    # zwraca ile unikalnych cech znalazł model
    def podaj_ile_features(self):
        return self.prosty_perceptron.n_features_in_
    
    # zwraca jakie nazwy klas znalazł model
    def podaj_jakie_klasy(self):
        return self.prosty_perceptron.classes_
    
    # Podaje obliczone WAGI dla każdego z atrybutów, zwarca np.ndarray
    # dwuwymiarową macierz
    # wiersze odpowiadają klasom
    # kolumny odpowiadają atrybutom
    def podaj_wagi(self):
        return self.prosty_perceptron.coef_
    
# Prosty przykład użycia
#p = ProstyPerceptron("cechy.csv")
#print(p.trenuj())
