from PyQt6.QtWidgets import QMainWindow


class GlowneOkno(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setGeometry(200, 200, 800, 600)
        self.showMaximized()
        self.show()
