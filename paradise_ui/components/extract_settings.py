from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel
from paradise_core import extract_pak

class ExtractSettings(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)

        self.label_pak = QLabel("Input .pak: None")
        self.label_out = QLabel("Output Folder: None")

        self.btn_pak = QPushButton("Select .pak")
        self.btn_out = QPushButton("Select Output Folder")
        self.btn_run = QPushButton("Extract")

        layout.addWidget(self.label_pak)
        layout.addWidget(self.btn_pak)
        layout.addWidget(self.label_out)
        layout.addWidget(self.btn_out)
        layout.addWidget(self.btn_run)

        self.pak_path = None
        self.out_dir = None

        self.btn_pak.clicked.connect(self.select_pak)
        self.btn_out.clicked.connect(self.select_out)
        self.btn_run.clicked.connect(self.run_extract)

    def select_pak(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select Pack", filter="Paradise Pack (*.pak)")
        if path:
            self.pak_path = path
            self.label_pak.setText(f"Input .pak: {path}")

    def select_out(self):
        path = QFileDialog.getExistingDirectory(self, "Select Output Folder")
        if path:
            self.out_dir = path
            self.label_out.setText(f"Output Folder: {path}")

    def run_extract(self):
        if self.pak_path and self.out_dir:
            extract_pak(self.pak_path, self.out_dir)
