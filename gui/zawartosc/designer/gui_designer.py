# Form implementation generated from reading ui file '/home/adrian/repos/Projekt_IO/gui/zawartosc/designer/gui_designer.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1033, 831)
        MainWindow.setMinimumSize(QtCore.QSize(500, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pasek_boczny = QtWidgets.QWidget(self.centralwidget)
        self.pasek_boczny.setObjectName("pasek_boczny")
        self.pasek_boczny_rozstawienie = QtWidgets.QVBoxLayout(self.pasek_boczny)
        self.pasek_boczny_rozstawienie.setContentsMargins(-1, 37, -1, -1)
        self.pasek_boczny_rozstawienie.setObjectName("pasek_boczny_rozstawienie")
        self.przycisk_dodaj = QtWidgets.QPushButton(self.pasek_boczny)
        self.przycisk_dodaj.setMinimumSize(QtCore.QSize(84, 65))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.przycisk_dodaj.setFont(font)
        self.przycisk_dodaj.setText("")
        self.przycisk_dodaj.setIconSize(QtCore.QSize(32, 32))
        self.przycisk_dodaj.setObjectName("przycisk_dodaj")
        self.pasek_boczny_rozstawienie.addWidget(self.przycisk_dodaj, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.przycisk_eksport = QtWidgets.QPushButton(self.pasek_boczny)
        self.przycisk_eksport.setMinimumSize(QtCore.QSize(84, 65))
        self.przycisk_eksport.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.przycisk_eksport.setFont(font)
        self.przycisk_eksport.setText("")
        self.przycisk_eksport.setIconSize(QtCore.QSize(32, 32))
        self.przycisk_eksport.setAutoDefault(False)
        self.przycisk_eksport.setDefault(False)
        self.przycisk_eksport.setFlat(False)
        self.przycisk_eksport.setObjectName("przycisk_eksport")
        self.pasek_boczny_rozstawienie.addWidget(self.przycisk_eksport)
        self.przycisk_wyczysc = QtWidgets.QPushButton(self.pasek_boczny)
        self.przycisk_wyczysc.setMinimumSize(QtCore.QSize(84, 65))
        self.przycisk_wyczysc.setText("")
        self.przycisk_wyczysc.setIconSize(QtCore.QSize(32, 32))
        self.przycisk_wyczysc.setObjectName("przycisk_wyczysc")
        self.pasek_boczny_rozstawienie.addWidget(self.przycisk_wyczysc)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.pasek_boczny_rozstawienie.addItem(spacerItem)
        self.horizontalLayout_2.addWidget(self.pasek_boczny)
        self.rozstawienie_srodek = QtWidgets.QVBoxLayout()
        self.rozstawienie_srodek.setObjectName("rozstawienie_srodek")
        self.pasek_gorny = QtWidgets.QHBoxLayout()
        self.pasek_gorny.setSpacing(0)
        self.pasek_gorny.setObjectName("pasek_gorny")
        self.przycisk_zdjecie = QtWidgets.QPushButton(self.centralwidget)
        self.przycisk_zdjecie.setEnabled(True)
        self.przycisk_zdjecie.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.przycisk_zdjecie.setLocale(QtCore.QLocale(QtCore.QLocale.Language.Polish, QtCore.QLocale.Country.Poland))
        self.przycisk_zdjecie.setCheckable(False)
        self.przycisk_zdjecie.setFlat(False)
        self.przycisk_zdjecie.setObjectName("przycisk_zdjecie")
        self.pasek_gorny.addWidget(self.przycisk_zdjecie)
        self.przycisk_nazwa = QtWidgets.QPushButton(self.centralwidget)
        self.przycisk_nazwa.setFlat(False)
        self.przycisk_nazwa.setObjectName("przycisk_nazwa")
        self.pasek_gorny.addWidget(self.przycisk_nazwa)
        self.przycisk_rodzaj = QtWidgets.QPushButton(self.centralwidget)
        self.przycisk_rodzaj.setLocale(QtCore.QLocale(QtCore.QLocale.Language.Polish, QtCore.QLocale.Country.Poland))
        self.przycisk_rodzaj.setFlat(False)
        self.przycisk_rodzaj.setObjectName("przycisk_rodzaj")
        self.pasek_gorny.addWidget(self.przycisk_rodzaj)
        self.rozstawienie_srodek.addLayout(self.pasek_gorny)
        self.lista = QtWidgets.QScrollArea(self.centralwidget)
        self.lista.setEnabled(True)
        self.lista.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.lista.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.lista.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.lista.setWidgetResizable(True)
        self.lista.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.lista.setObjectName("lista")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 867, 703))
        self.scrollAreaWidgetContents.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.rozstawienie_listy_elementow = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.rozstawienie_listy_elementow.setContentsMargins(-1, -1, -1, 11)
        self.rozstawienie_listy_elementow.setObjectName("rozstawienie_listy_elementow")
        self.lista.setWidget(self.scrollAreaWidgetContents)
        self.rozstawienie_srodek.addWidget(self.lista)
        self.pasek_ladowania = QtWidgets.QProgressBar(self.centralwidget)
        self.pasek_ladowania.setProperty("value", 0)
        self.pasek_ladowania.setObjectName("pasek_ladowania")
        self.rozstawienie_srodek.addWidget(self.pasek_ladowania)
        self.horizontalLayout_2.addLayout(self.rozstawienie_srodek)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1033, 32))
        self.menuBar.setObjectName("menuBar")
        self.menuUstawienia = QtWidgets.QMenu(self.menuBar)
        self.menuUstawienia.setObjectName("menuUstawienia")
        self.menu_motyw = QtWidgets.QMenu(self.menuUstawienia)
        self.menu_motyw.setObjectName("menu_motyw")
        MainWindow.setMenuBar(self.menuBar)
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionLoad = QtGui.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.akcja_systemowy = QtGui.QAction(MainWindow)
        self.akcja_systemowy.setObjectName("akcja_systemowy")
        self.akcja_jasny = QtGui.QAction(MainWindow)
        self.akcja_jasny.setObjectName("akcja_jasny")
        self.akcja_ciemny = QtGui.QAction(MainWindow)
        self.akcja_ciemny.setObjectName("akcja_ciemny")
        self.akcja_czcionka = QtGui.QAction(MainWindow)
        self.akcja_czcionka.setObjectName("akcja_czcionka")
        self.akcja_wysoki_kontrast = QtGui.QAction(MainWindow)
        self.akcja_wysoki_kontrast.setObjectName("akcja_wysoki_kontrast")
        self.akcja_polski = QtGui.QAction(MainWindow)
        self.akcja_polski.setObjectName("akcja_polski")
        self.akcja_angielski = QtGui.QAction(MainWindow)
        self.akcja_angielski.setObjectName("akcja_angielski")
        self.akcja_zasoby = QtGui.QAction(MainWindow)
        self.akcja_zasoby.setObjectName("akcja_zasoby")
        self.menu_motyw.addAction(self.akcja_systemowy)
        self.menu_motyw.addAction(self.akcja_jasny)
        self.menu_motyw.addAction(self.akcja_ciemny)
        self.menu_motyw.addAction(self.akcja_wysoki_kontrast)
        self.menuUstawienia.addAction(self.menu_motyw.menuAction())
        self.menuUstawienia.addAction(self.akcja_zasoby)
        self.menuBar.addAction(self.menuUstawienia.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Aplikacja do identyfikacji bakterii"))
        self.przycisk_zdjecie.setText(_translate("MainWindow", "Zdjęcie"))
        self.przycisk_nazwa.setText(_translate("MainWindow", "Nazwa"))
        self.przycisk_rodzaj.setText(_translate("MainWindow", "Rodzaj"))
        self.menuUstawienia.setTitle(_translate("MainWindow", "Ustawienia"))
        self.menu_motyw.setTitle(_translate("MainWindow", "Motyw"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.akcja_systemowy.setText(_translate("MainWindow", "Systemowy"))
        self.akcja_jasny.setText(_translate("MainWindow", "Jasny"))
        self.akcja_ciemny.setText(_translate("MainWindow", "Ciemny (domyślny)"))
        self.akcja_czcionka.setText(_translate("MainWindow", "Czcionka (w trakcie tworzenia)"))
        self.akcja_wysoki_kontrast.setText(_translate("MainWindow", "Wysoki kontrast"))
        self.akcja_polski.setText(_translate("MainWindow", "Polski (domyślny)"))
        self.akcja_angielski.setText(_translate("MainWindow", "English"))
        self.akcja_zasoby.setText(_translate("MainWindow", "Zasoby"))
