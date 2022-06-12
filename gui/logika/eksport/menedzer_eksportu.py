from typing import List

from ...zawartosc.widgety.element_listy import ElementListy
from PyQt6.QtWidgets import QFileDialog, QWidget
# from PyQt6 import QtGui
from fpdf import FPDF

class MenedzerEksportu:
    def __init__(self, lista_elementow: List[ElementListy], rodzic : QWidget) -> None:
        self.__lista_elementow = lista_elementow
        self.rodzic = rodzic

    def eksportuj(self):
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
                pass
            for i in range(len(self.__lista_elementow)):
                with open(sciezka, "a") as plik:
                    plik.write(f"{self.__lista_elementow[i].nazwa};{self.__lista_elementow[i].rodzaj}" + "\n")
        elif rozszerzenie == 'pdf':
            pdf = FPDF()
            for i in range(len(self.__lista_elementow)):
                pdf.add_page()
                pdf.set_font("Arial", size = 15)
                proporcje = self.__lista_elementow[i].zdjecie.pixmap().height()/self.__lista_elementow[i].zdjecie.pixmap().width()
                pdf.set_x(100 + pdf.w/2)
                pdf.set_y(100 + (pdf.w/4.0)*proporcje)
                pdf.cell(10, 10, f"{self.__lista_elementow[i].nazwa} {self.__lista_elementow[i].rodzaj}", 0, 0)
                pdf.set_y(10)
                pdf.image(self.__lista_elementow[i].sciezka, x = 10, y = 10, w=pdf.w/2.0, h=(pdf.w/2.0)*proporcje)

            pdf.output(sciezka, 'F')
