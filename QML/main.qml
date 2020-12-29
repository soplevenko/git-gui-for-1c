//import related modules
import QtQuick 2.14
import QtQuick.Window 2.14
import QtQuick.Layouts 1.14
import QtQuick.Controls 2.14
import QtQuick.Controls.Material 2.14
import QtQuick.Controls.Universal 2.14

//window containing the application
Window {

    width: 320
    height: 240
    title: qsTr("1C Git")

    TextField {
        id: folderSelectText
        placeholderText: qsTr("Select folder")
        onEditingFinished: text = folderVerificator.verify_folder(text)
    
        Button {
            id: folderSelectButton
            anchors.left: parent.right
            text: "..."
        }
    }
}