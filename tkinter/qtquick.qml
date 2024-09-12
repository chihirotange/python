import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 400
    height: 300
    title: "Styled Button Example"


    Column {
        focus: true
        Keys.onPressed: {
            if (event.key === Qt.Key_Escape) {
                Qt.quit();
            }
        }
        // anchors.fill: parent
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: parent.top
        
        Button {
            id: hoverableButton
            contentItem: Text {
                text: "Click me"
                font.pointSize: 20
                color: "#f2faef"
                font.family: "Tahoma"
                font.capitalization: Font.AllUppercase
            }
            background: Rectangle {
                color: hoverableButton.hovered ? "#5a9ac0" : "#447a9c"
                Behavior on color {
                    ColorAnimation { duration: 200 }
                }
            }
            hoverEnabled: true
        }
        Button {
            text: "click me"
        }
    }

    // Button {
    //     text: "Styled Button"
    //     anchors.centerIn: parent

    //     background: Rectangle {
    //         color: "#4CAF50"
    //         border.color: "black"
    //         radius: 10
    //         padding: 10
    //     }

    //     contentItem: Text {
    //         text: "Styled Button"
    //         color: "white"
    //         font.bold: true
    //         font.pointSize: 18
    //     }
    // }
}