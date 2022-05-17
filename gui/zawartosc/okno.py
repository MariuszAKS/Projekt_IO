from PyQt6.QtWidgets import QMainWindow


class GlowneOkno(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setGeometry(200, 200, 800, 600)
        self.show()


    # def wheelEvent(sel, event):
    #         print(event.angleDelta())
    #         super(GlowneOkno, self.glowne_okno)
