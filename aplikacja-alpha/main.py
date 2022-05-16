# import csv
# import numpy as np
#
# import analiza_jednego
# import analiza_wszystkie_cechy
# import klasyfikacja_rf
# import klasyfikacja_rf_featselect
import generowanie_cech
import klasyfikacja_obrazu


# Zdobądź ścieżkę do pliku (na razie wpisana w funkcji na stałe)
# Wygeneruj cechy (plik generowanie_cech)
# random forest, gdzie train - macierz wszystkich cech obrazow, train - wygenerowane cechy badanego)
# Zwróć wynik, do której kategorii zaklasyfikowało obraz

sciezka_do_pliku = 'Bakterie\\Pseudomonas\\p00018.png'
# sciezka_do_pliku = 'E_sakazakii.jpg'

cechy = generowanie_cech.generowanie_cech(sciezka_do_pliku)
wynik = klasyfikacja_obrazu.klasyfikacja([cechy])

if wynik == 1:
    print('Bradyrhizobium')
elif wynik == 2:
    print('Enterobacter')
elif wynik == 3:
    print('Pantoea')
elif wynik == 4:
    print('Pseudomonas')
elif wynik == 5:
    print('Rhizobium')
else:
    print('Cos poszlo nie tak!')








# klasyfikacja_rf_featselect.klasyfikacja_rf_main()

# sciezka_do_pliku = 'Bakterie\\Bradyrhizobium\\b00001.png'

# analiza_jednego.Analizuj(sciezka_do_pliku)
# analiza_wszystkie_cechy.oblicz_cechy()


# with open('rf.csv', 'w', newline='') as plik:
#     w = csv.writer(plik, delimiter=';')
#
#     nazwy_kolumn, waznosc_cechy, accuracy = klasyfikacja_rf.klasyfikacja()
#     w.writerow(np.concatenate((['Accuracy'], nazwy_kolumn), axis=None))
#     wiersz = np.concatenate((accuracy, waznosc_cechy), axis=None)
#     w.writerow(wiersz)
#
#     for i in range(0, 199):
#         _, waznosc_cechy, accuracy = klasyfikacja_rf.klasyfikacja()
#         wiersz = np.concatenate((accuracy, waznosc_cechy), axis=None)
#         w.writerow(wiersz)
