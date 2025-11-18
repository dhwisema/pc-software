

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick
import QtQuick.Controls
import Senior_design_ui
import QtQuick.Layouts

Rectangle {
    id: rectangle
    width: Constants.width
    height: Constants.height

    color: Constants.backgroundColor

    Text {
        id: text1
        x: 781
        y: 110
        text: qsTr("Pager Software")
        font.pixelSize: 50
        font.bold: true
    }

    Text {
        id: text2
        x: 878
        y: 183
        text: qsTr("Welcome")
        font.pixelSize: 40
    }

    RowLayout {
        id: rowLayout
        width: 336
        height: 56
        anchors.top: parent.top
        anchors.topMargin: 470
        spacing: 20
        anchors.horizontalCenter: parent.horizontalCenter

        ComboBox {
            id: teamA
            width: 160
            clip: true
            flat: false
            editable: false
            currentIndex: -1
            textRole: "Team A"
            font.pointSize: 15
            displayText: "Team A"
            Layout.preferredWidth: 140
        }

        ComboBox {
            id: teamB
            width: 160
            spacing: 2
            clip: false
            textRole: "Team B"
            font.pointSize: 15
            displayText: "Team B"
            Layout.preferredWidth: 140
        }
    }

    Button {
        id: button
        width: 300
        text: qsTr("Send Message")
        anchors.top: rowLayout.bottom
        anchors.topMargin: 5
        font.pointSize: 20
        anchors.horizontalCenter: parent.horizontalCenter
    }

    Label {
        id: label
        text: qsTr("Manual Queue Mode")
        anchors.bottom: rowLayout.top
        anchors.bottomMargin: 38
        anchors.horizontalCenterOffset: 0
        anchors.horizontalCenter: rowLayout.horizontalCenter
        font.pointSize: 40
    }

    states: [
        State {
            name: "clicked"
        }
    ]
}
