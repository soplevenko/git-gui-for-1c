"""
QML playground louncher.
Simple script for QML signal test purpose.
"""

import sys
from os import path as oslibpath

from PySide2.QtCore import QObject, Slot
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine

from scriptdir import get_qml_qurl

class FolderVerificator(QObject):
    """
    Folder path verificator class.
    Exposed to QML property folderVerificator.
    """

    def __init__(self):
        QObject.__init__(self)

    @Slot(str, result=str)
    def verify_folder(self, path):
        """
        Folder path verification function.
        Returns path if exists and empty string either.
        """
        return path if oslibpath.exists(path) else ""

if __name__ == "__main__":

    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    folder_verificator = FolderVerificator()
    engine.rootContext().setContextProperty("folderVerificator", folder_verificator)

    engine.load(get_qml_qurl("main.qml"))

    engine.rootObjects()[0].show()
    #if not engine.rootObjects():
    #    sys.exit(-1)

    sys.exit(app.exec_())
