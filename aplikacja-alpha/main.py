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
