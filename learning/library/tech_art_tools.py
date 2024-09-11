from helper_object import HelperObject
from PySide2.QtWidgets import QPushButton, QHBoxLayout, QVBoxLayout

class TechArtTool(HelperObject):
    def __init__(self):
        self.push_btn = None
        self.v_layout = None

        self.v_layout = QVBoxLayout()

    def get_widget(self):
        h_layout = QHBoxLayout()
        self.v_layout.addLayout(h_layout)
        self.push_btn = QPushButton("Tech art tool")
        h_layout.addWidget(self.push_btn)
        h_layout.addWidget(QPushButton("test"))
        return self.v_layout