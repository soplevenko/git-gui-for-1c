"""Module for working with local script directory"""

from os import path as oslibpath
from PySide2.QtCore import QUrl

def get_qml_qurl(qml_filename, qml_subdir = "QML"):
    """Function returns QUrl from given filename and QML subdirectory name"""
    dirname = oslibpath.dirname(oslibpath.realpath(__file__))
    return QUrl.fromLocalFile(oslibpath.join(dirname, qml_subdir, qml_filename))

if __name__ == "__main__":
    print(get_qml_qurl("main.qml"))
