import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Klasa służąca to wytrenowania modeluSVM
# na podstawie podanego pliku .csv (kompatybilne z plikiem cech na github)
# oraz wykorzystania go do klasyfikowania nowych zdjęc
# plik = sciezka do pliku

class KlasaSVM:
    def __init__(self,plik,rozdzielacz=';') -> None:
        self.dane = pd.read_csv(plik, delimiter=rozdzielacz,encoding='latin-1') 
    # trenuje model na podstawie podanych danych
    # oraz zwraca jego ACCURACY (0.00 - 1.00)
    def trenuj(self):    
        
        dane_labels = self.dane.loc[:,'-- Rodzaj --']
        dane_data = self.dane.drop(['-- Rodzaj --','-- Numer --'], axis=1)
        #utworzenie zestawów danych treningowych i uczących
        x_uczacy, x_testujacy, y_uczacy, y_testujacy = train_test_split(dane_data,dane_labels,test_size=0.2)
        #Standaryzacja danych wejsciowych
        self.sc = StandardScaler()
        self.sc.fit(x_uczacy)
        x_uczacy_standaryzacja = self.sc.transform(x_uczacy)
        x_testujacy_standaryzacja = self.sc.transform(x_testujacy)
        #SVM
        self.model = SVC(C=8)
        self.model.fit(x_uczacy_standaryzacja, y_uczacy)
        #predykcja klasy
        y_przewidziane = self.model.predict(x_testujacy_standaryzacja)
        #sprawdzanie ACCURACY modelu
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
        klasa = self.predict(obiekty_standaryzacja)
        return klasa
    
    # Klasyfikuje zestawy cech w podanym np.array (jednowymiarowym)
    # jako typ bakterii
    # array powinien zawierac same cechy, bez numerów wierszy
    # (czyli bez wartosci z kolumn: '-- Rodzaj --' oraz '-- Numer --')
    # obiekt = np.array z cechami
    # UWAGA Przed użyciem należy wytrenować model
    # za pomocą funkcji: trenuj()
    def klasyfikuj_obiekt(self, obiekt):
        obiekt = obiekt.reshape(1,len(obiekt))
        obiekt_frame = pd.DataFrame(obiekt)
        obiekt_standaryzacja = self.sc.transform(obiekt_frame)
        klasa = self.model.predict(obiekt_standaryzacja)
        return klasa
    
    # zwraca ile iteracji (epok) wykonał model podczas uczenia
    def podaj_ile_iteracji(self):
        return self.model.n_iter_
    
    # zwraca ile unikalnych cech znalazł model
    def podaj_ile_features(self):
        return self.model.n_features_in_
    
    # zwraca jakie nazwy klas znalazł model
    def podaj_jakie_klasy(self):
        return self.model.classes_
    
    # WAGI występują tylko dla modelu liniowego
    
#Przykład użycia
#s = KlasaSVM("40cech.csv")
#print(s.trenuj()) #podaje Accuracy
#d = [28.741631493408274,5.360991032043724,21.421728238195172,64.94259236155875,8.055668446138315,20.513544403613473,420.8055039990217,1.9360553107179206,0.8754247654506639,12.623575776798784,0.8361189712211248,22.57783802517774,509.75876989116193,24.174863584974894,1.9498242485257695,1.4118752111750705,2.0495744327319074,1.944556893302151,0.8594690587282647,0.1691207028789002,1.5031384506422736,0.1691717235560541,2.048641416406421,5.085721043458969,24.883347025678788,98.20455253576421,0.08417378182669942,98.20455253576421,0.007087467472322455,0.4287757085332598,41.824265691821054,0.42872244127371345,21.393420772942246,133.98332833909942,41.8229841433753,6.588062741482279,6.498011669740134,13.585929289891467,13.585929289891467,25.305539403091313]
#print(s.klasyfikuj_obiekt(np.array(d)))
