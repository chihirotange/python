import unreal as ue
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout

app = QApplication.instance() or QApplication(sys.argv)
window = QMainWindow()

centralWidget = QWidget()
window.setCentralWidget(centralWidget) #mostly boilerplate

layout = QVBoxLayout()
centralWidget.setLayout(layout)

def on_button_clicked():
    allActors = ue.get_editor_subsystem(ue.EditorActorSubsystem).get_all_level_actors()
    ue.log(len(allActors))
    
button = QPushButton("click me ", window)
button.clicked.connect(on_button_clicked)

button2 = QPushButton("click me 2", window)
button2.clicked.connect(on_button_clicked)

layout.addWidget(button)
layout.addWidget(button2)



window.show()