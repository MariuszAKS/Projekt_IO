from PyQt6.QtWidgets import QMainWindow
import qdarkstyle


class MenedzerMotywow:
    folder_stylow = "gui/zawartosc/motywy/"

    def __init__(self, glowne_okno: QMainWindow) -> None:
        self.__glowne_okno = glowne_okno

    def ustaw_jasny(self) -> None:
        styl = self.__odczytaj_styl("jasny.css")
        self.__glowne_okno.setStyleSheet(styl)

    def ustaw_ciemny(self) -> None:
        styl = self.__odczytaj_styl("ciemny.css")
        self.__glowne_okno.setStyleSheet(styl)

    def ustaw_wysoki_kontrast(self) -> None:
        styl = self.__odczytaj_styl("wysoki_kontrast.css")
        self.__glowne_okno.setStyleSheet(styl)

    def ustaw_systemowy(self) -> None:
        styl = self.__odczytaj_styl(None)
        self.__glowne_okno.setStyleSheet(styl)

    def __odczytaj_styl(self, nazwa_pliku: str|None) -> str:
        styl = ""

        if nazwa_pliku is not None:
            sciezka_stylu = MenedzerMotywow.folder_stylow + nazwa_pliku
            with open(sciezka_stylu, 'r') as plik:
                styl = plik.read()


        sciezka_stylu_ogolnego = MenedzerMotywow.folder_stylow + "ogolny.css"
        with open(sciezka_stylu_ogolnego, 'r') as plik:
            styl += plik.read()

        return styl