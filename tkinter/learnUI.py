import sys
import os
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QUrl

if __name__ == "__main__":
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()
    
    # Get the absolute path of the QML file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    qml_file = os.path.join(current_dir, "qtquick.qml")
    
    print(f"Attempting to load QML file: {qml_file}")
    print(f"File exists: {os.path.exists(qml_file)}")
    
    # Load the QML file using QUrl
    engine.load(QUrl.fromLocalFile(qml_file))
    
    if not engine.rootObjects():
        print(f"Error: Unable to load {qml_file}")
        print(f"Engine errors: {engine.warnings()}")
        sys.exit(-1)
    
    sys.exit(app.exec_())