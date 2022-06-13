from PyQt6.QtWidgets import QMainWindow


class MenedzerMotywow:
    """
    Klasa służaca do zmiany motywu
    """

    FOLDER_STYLOW = "gui/zawartosc/motywy/"

    def __init__(self, glowne_okno: QMainWindow) -> None:
        self.__glowne_okno = glowne_okno

    def ustaw_jasny(self) -> None:
        '''Ustawia jasny motyw'''

        styl = self.__odczytaj_styl("jasny.css")
        self.__glowne_okno.setStyleSheet(styl)

    def ustaw_ciemny(self) -> None:
        '''Ustawia ciemny motyw'''

        styl = self.__odczytaj_styl("ciemny.css")
        self.__glowne_okno.setStyleSheet(styl)

    def ustaw_wysoki_kontrast(self) -> None:
        '''Ustawia motyw o wysokim kontraście kolorów'''

        styl = self.__odczytaj_styl("wysoki_kontrast.css")
        self.__glowne_okno.setStyleSheet(styl)

    def ustaw_systemowy(self) -> None:
        '''Ustawia motyw systemowy'''

        styl = self.__odczytaj_styl(None)
        self.__glowne_okno.setStyleSheet(styl)

    def __odczytaj_styl(self, nazwa_pliku: str|None) -> str:
        """
        Odczytuje styl z pliku o podanej nazwie w folderze FOLDER_STYLOW
        :param nazwa_pliku: Nazwa pliku z motywem
        """

        styl = ""

        if nazwa_pliku is not None:
            sciezka_stylu = MenedzerMotywow.FOLDER_STYLOW + nazwa_pliku
            with open(sciezka_stylu, 'r') as plik:
                styl = plik.read()

        sciezka_stylu_ogolnego = MenedzerMotywow.FOLDER_STYLOW + "ogolny.css"
        with open(sciezka_stylu_ogolnego, 'r') as plik:
            styl += plik.read()

        return styl