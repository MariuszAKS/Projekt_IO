from typing import Any

from PyQt6.QtWidgets import QVBoxLayout, QListWidget

from ...zawartosc.widgety.element_listy import ElementListy


class MenedzerEksportu:
    def __init__(self, lista_elementow: QVBoxLayout) -> None:
        self.__lista_elementow = lista_elementow
        # lista_elementow.itemAt(0)

    def eksportuj(self):
        print("Powinien zadziałać eksport")
        elementy = []

        for i in range(self.__lista_elementow.count()):
            elementy.append(self.__lista_elementow.itemAt(i))

        print(f"Elementy: {elementy}")