"""
QML playground louncher.
Simple script for QML file test lounch purpose.
"""

import sys

from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine

from scriptdir import get_qml_qurl

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    engine.load(get_qml_qurl("main.qml"))

    engine.rootObjects()[0].show()
    #if not engine.rootObjects():
    #    sys.exit(-1)

    sys.exit(app.exec_())
    