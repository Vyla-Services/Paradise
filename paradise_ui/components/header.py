from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout
from PySide6.QtCore import Signal

class Header(QWidget):
    navigate = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout(self)

        self.btn_pack = QPushButton("Pack")
        self.btn_extract = QPushButton("Extract")
        self.btn_list = QPushButton("Inspect")

        layout.addWidget(self.btn_pack)
        layout.addWidget(self.btn_extract)
        layout.addWidget(self.btn_list)

        self.btn_pack.clicked.connect(lambda: self.navigate.emit(0))
        self.btn_extract.clicked.connect(lambda: self.navigate.emit(1))
        self.btn_list.clicked.connect(lambda: self.navigate.emit(2))
