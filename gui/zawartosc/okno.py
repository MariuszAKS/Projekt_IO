from PyQt6.QtWidgets import QMainWindow


class GlowneOkno(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setGeometry(0, 0, 800, 600)
        self.showMaximized()
        self.show()


