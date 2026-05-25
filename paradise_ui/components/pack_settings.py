from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QComboBox, QSpinBox
from paradise_core import pack_folder

class PackSettings(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)

        self.label_input = QLabel("Input Folder: None")
        self.label_output = QLabel("Output File: None")

        self.btn_input = QPushButton("Select Folder")
        self.btn_output = QPushButton("Select Output .pak")
        self.btn_run = QPushButton("Create Pack")

        self.combo_comp = QComboBox()
        self.combo_comp.addItems(["zlib", "lz4", "zstd"])

        self.spin_level = QSpinBox()
        self.spin_level.setRange(1, 22)
        self.spin_level.setValue(9)

        layout.addWidget(self.label_input)
        layout.addWidget(self.btn_input)
        layout.addWidget(self.label_output)
        layout.addWidget(self.btn_output)
        layout.addWidget(QLabel("Compression"))
        layout.addWidget(self.combo_comp)
        layout.addWidget(QLabel("Level"))
        layout.addWidget(self.spin_level)
        layout.addWidget(self.btn_run)

        self.input_dir = None
        self.output_file = None

        self.btn_input.clicked.connect(self.select_input)
        self.btn_output.clicked.connect(self.select_output)
        self.btn_run.clicked.connect(self.run_pack)

    def select_input(self):
        path = QFileDialog.getExistingDirectory(self, "Select Folder")
        if path:
            self.input_dir = path
            self.label_input.setText(f"Input Folder: {path}")

    def select_output(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save Pack", filter="Paradise Pack (*.pak)")
        if path:
            self.output_file = path
            self.label_output.setText(f"Output File: {path}")

    def run_pack(self):
        if self.input_dir and self.output_file:
            comp = self.combo_comp.currentText()
            lvl = self.spin_level.value()
            pack_folder(self.input_dir, self.output_file, comp, lvl)
