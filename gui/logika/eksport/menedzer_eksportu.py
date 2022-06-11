from typing import List

from ...zawartosc.widgety.element_listy import ElementListy
from PyQt6.QtWidgets import QFileDialog, QWidget
from fpdf import FPDF
import datetime

class MenedzerEksportu:
    def __init__(self, lista_elementow: List[ElementListy]) -> None:
        self.__lista_elementow = lista_elementow

    def eksportuj(self, rodzic: QWidget):
        with open("wyniki.csv", "w") as plik:
            pass
        for i in range(len(self.__lista_elementow)):
            with open("wyniki.csv", "a") as plik:
                plik.write(f"{self.__lista_elementow[i].nazwa};{self.__lista_elementow[i].rodzaj}" + "\n")
        pdf = FPDF()
        y = 10
        for i in range(len(self.__lista_elementow)):
            pdf.add_page()
            pdf.set_font("Arial", size = 15)
            proporcje = self.__lista_elementow[i].zdjecie.pixmap().height()/self.__lista_elementow[i].zdjecie.pixmap().width()
            pdf.set_x(100 + pdf.w/2)
            pdf.set_y(100 + (pdf.w/4.0)*proporcje)
            pdf.cell(10, 10, f"{self.__lista_elementow[i].nazwa} {self.__lista_elementow[i].rodzaj}", 0, 0, 'L')
            pdf.set_y(10)
            pdf.image(self.__lista_elementow[i].sciezka, x = 10, y = 10, w=pdf.w/2.0, h=(pdf.w/2.0)*proporcje)

        pdf.output('wyniki.pdf', 'F')