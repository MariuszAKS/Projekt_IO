from PyQt6.QtWidgets import QMainWindow


class MenedzerMotywow:
    folder_stylow = "gui/zawartosc/motywy/"

    def __init__(self, glowne_okno: QMainWindow) -> None:
        self.__glowne_okno = glowne_okno

    def ustaw_jasny(self) -> None:
        styl = self.__odczytaj_styl("jasny.css")
        self.__glowne_okno.setStyleSheet(styl)
        pass

    def ustaw_ciemny(self) -> None:
        styl = self.__odczytaj_styl("ciemny.css")
        self.__glowne_okno.setStyleSheet(styl)
        pass

    def ustaw_wysoki_kontrast(self) -> None:
        styl = self.__odczytaj_styl("wysoki_kontrast.css")
        self.__glowne_okno.setStyleSheet(styl)
        pass

    def ustaw_systemowy(self) -> None:
        styl = ""
        self.__glowne_okno.setStyleSheet(styl)
        pass

    def __odczytaj_styl(self, nazwa_pliku: str) -> str:
        styl = ""
        sciezka_stylu = MenedzerMotywow.folder_stylow + nazwa_pliku
        with open(sciezka_stylu, 'r') as plik:
            styl = plik.read()

        return styl