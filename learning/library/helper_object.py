from abc import ABC, abstractmethod
from PySide2.QtWidgets import QLayout, QHBoxLayout, QLabel, QCheckBox
from PySide2.QtCore import Qt

class HelperObject(ABC):
    @abstractmethod
    def get_widget(self) -> QLayout:
        raise NotImplementedError
    
class ListItem(ABC):
    def __init__(self, name:str):
        self.layout = QHBoxLayout()
        self._setup_main_layout()

        self.checkbox = QCheckBox()
        self.layout.addWidget(self.checkbox)
        label = QLabel(name)
        # label.setAlignment(QtCore.Qt.AlignLeft)
        self.layout.addWidget(label)

    def get_widget(self):
        return self.layout
    
    def _setup_main_layout(self):
        self.layout.setAlignment(Qt.AlignLeft)
        