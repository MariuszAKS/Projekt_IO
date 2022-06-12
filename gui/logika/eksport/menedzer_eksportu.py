"""
@package docstring
"""
from typing import List

from ...zawartosc.widgety.element_listy import ElementListy
from PyQt6.QtWidgets import QFileDialog, QWidget
from fpdf import FPDF
import time

class MenedzerEksportu:
    """
    Klasa obługująca eksport
    """
    def __init__(self, lista_elementow: List[ElementListy], rodzic : QWidget) -> None:
        """
        Konstruktor kopiujący klasy eksport
        param: lista_elementow: Przechowuje elementy wyświetlone na ekranie
        param: rodzic: Widżet nadrzędny
        """
        self.__lista_elementow = lista_elementow
        self.rodzic = rodzic

    def eksportuj(self):
        """
        Metoda służąca do eksportu
        Eksportuje plik .csv lub .pdf w zależności od wyboru użytkownika
        """
        if len(self.__lista_elementow) == 0:
            return

        sciezka1 = QFileDialog().getSaveFileName(self.rodzic, 'Open a file', 'C:\\','csv plik (*.csv);;pdf plik (*.pdf)')
        rozszerzenie = sciezka1[1][:3]
        j = 0
        for i in range(len(sciezka1[0]) - 1, 0, -1):
            if sciezka1[0][i] == '.':
                j = i
                break
        sciezka = sciezka1[0][:j] + "." + rozszerzenie
        if rozszerzenie == 'csv':
            with open(sciezka, "w") as plik:
                plik.write(f"Nazwa:;Rodzaj:" + "\n")
            for i in range(len(self.__lista_elementow)):
                with open(sciezka, "a") as plik:
                    plik.write(f"{self.__lista_elementow[i].nazwa};{self.__lista_elementow[i].rodzaj}" + "\n")
        elif rozszerzenie == 'pdf':
            pdf = FPDF()

            max_x_zdjecia = 160
            max_y_zdjecia = 60

            pdf.add_page()
            pdf.set_font("Arial", 'B', size=30)
            pdf.set_y(15)
            pdf.set_x(25)
            pdf.cell(w=160, h=20, txt=f"Analiza obrazów", ln=1, align='C')
            pdf.set_x(25)
            pdf.cell(w=160, h=20, txt=f"{time.asctime(time.localtime(time.time()))}", ln=1, align='C')
            pdf.set_x(25)
            pdf.cell(w=160, h=20, txt=f"Elementów: {len(self.__lista_elementow)}", ln=1, align='C')
            pdf.set_y(pdf.get_y() + 25)

            pdf.set_font("Arial", size=15)
            i = 0
            j = 1

            while i < len(self.__lista_elementow):
                while pdf.get_y() < 270 and i < len(self.__lista_elementow):
                    print(f'Zdjęcie {i}')
                    print(f'y {pdf.get_y()}')
                    x_zdjecia = self.__lista_elementow[i].zdjecie.pixmap().width()
                    y_zdjecia = self.__lista_elementow[i].zdjecie.pixmap().height()

                    if x_zdjecia > max_x_zdjecia:
                        dzielnik = x_zdjecia / max_x_zdjecia
                        x_zdjecia = max_x_zdjecia
                        y_zdjecia /= dzielnik
                    if y_zdjecia > max_y_zdjecia:
                        dzielnik = y_zdjecia / max_y_zdjecia
                        y_zdjecia = max_y_zdjecia
                        x_zdjecia /= dzielnik
                    print(f'Wymiary zdjecia {x_zdjecia} {y_zdjecia}')
                    print(f'Pozycja zdjecia {(210 - x_zdjecia) / 2.0} {j * 90}')
                    print(self.__lista_elementow[i].sciezka)

                    pdf.image(self.__lista_elementow[i].sciezka, x=(210 - x_zdjecia) / 2.0, y=10 + (j * 90),
                              w=x_zdjecia, h=y_zdjecia)
                    pdf.set_y(pdf.get_y() + 60)
                    print(f'y {pdf.get_y()}')
                    pdf.set_x(25)
                    nazwa_latin1 = self.__lista_elementow[i].nazwa.encode('latin-1', 'replace').decode('latin-1')
                    pdf.cell(w=160, h=10, txt=f"Nazwa: {nazwa_latin1}", ln=1, align='C')
                    pdf.set_x(25)
                    pdf.cell(w=160, h=10, txt=f"Rodzaj: {self.__lista_elementow[i].rodzaj}", ln=1, align='C')
                    pdf.set_y(pdf.get_y() + 10)
                    print(f'y {pdf.get_y()}')

                    i += 1
                    j += 1

                if i < len(self.__lista_elementow):
                    pdf.add_page()
                    pdf.set_y(10)
                    j = 0
                    print(f'Nastepna strona, y {pdf.get_y()}')

            pdf.output(sciezka, 'F')
