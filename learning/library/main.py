from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout
from tech_art_tools import TechArtTool

from helper_object import ListItem
if __name__ == "__main__":

    app = QApplication()
    window = QWidget()

    ver_layout = QVBoxLayout()
    ver_layout.addLayout(TechArtTool().get_widget())
    

    for x in range(10):
        ver_layout.addLayout(ListItem("aichan" +str(x)).get_widget())

    window.setLayout(ver_layout)
    window.show()
    app.exec_()