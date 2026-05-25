from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFileDialog, QTableWidget, QTableWidgetItem
from paradise_core.index import read_index

class FileTable(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)

        self.btn_load = QPushButton("Select .pak")
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Path", "Raw Size", "Compressed", "Offset"])

        layout.addWidget(self.btn_load)
        layout.addWidget(self.table)

        self.btn_load.clicked.connect(self.load_pak)

    def load_pak(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select Pack", filter="Paradise Pack (*.pak)")
        if not path:
            return
        with open(path, "rb") as f:
            entries, _ = read_index(f)
        self.table.setRowCount(len(entries))
        for i, e in enumerate(entries):
            self.table.setItem(i, 0, QTableWidgetItem(e["path"]))
            self.table.setItem(i, 1, QTableWidgetItem(str(e["size_raw"])))
            self.table.setItem(i, 2, QTableWidgetItem(str(e["size_comp"])))
            self.table.setItem(i, 3, QTableWidgetItem(str(e["offset"])))
