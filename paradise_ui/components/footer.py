from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout

class Footer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout(self)
        self.label = QLabel("Paradise © 2026")
        layout.addWidget(self.label)
