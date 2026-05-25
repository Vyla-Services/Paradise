from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QStackedWidget
from PySide6.QtGui import QIcon
from .components.header import Header
from .components.footer import Footer
from .components.pack_settings import PackSettings
from .components.extract_settings import ExtractSettings
from .components.file_table import FileTable
import sys
import os
import json

class ParadiseApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Paradise Packer")
        self.setMinimumSize(900, 600)
        self.load_theme()

        layout = QVBoxLayout(self)
        self.header = Header(self)
        layout.addWidget(self.header)

        self.stack = QStackedWidget(self)
        self.page_pack = PackSettings(self)
        self.page_extract = ExtractSettings(self)
        self.page_list = FileTable(self)

        self.stack.addWidget(self.page_pack)
        self.stack.addWidget(self.page_extract)
        self.stack.addWidget(self.page_list)

        layout.addWidget(self.stack)
        self.footer = Footer(self)
        layout.addWidget(self.footer)

        self.header.navigate.connect(self.switch_page)

    def switch_page(self, index):
        self.stack.setCurrentIndex(index)

    def load_theme(self):
        theme_path = os.path.join(os.path.dirname(__file__), "assets/themes/dark.json")
        with open(theme_path, "r") as f:
            theme = json.load(f)
        self.setStyleSheet(theme["stylesheet"])

def run():
    app = QApplication(sys.argv)
    window = ParadiseApp()
    window.show()
    sys.exit(app.exec())
