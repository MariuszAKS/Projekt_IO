from typing import List

from ...zawartosc.widgety.element_listy import ElementListy


class MenedzerEksportu:
    def __init__(self, lista_elementow: List[ElementListy]) -> None:
        self.__lista_elementow = lista_elementow

    def eksportuj(self):
        print("Powinien zadziałać eksport")

        print(f"Elementy: {self.__lista_elementow[0].nazwa}")