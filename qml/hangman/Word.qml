import QtQuick 2.2
import QtQuick.Controls 2.5

Item {
    id: word
    property string text: ""

    Row {
        id: row
        spacing: topLevel.width / 100
        anchors.fill: parent

        Rectangle { width: 10; height: word.height; color: "red" }

        Repeater {
            id: repeater
            model: text.length

            Item {
                width: (word.text.length) > 0 ? (((word.width-20) / word.text.length) - (word.width/100)) : 10
                height: word.height
                Letter {
                    id: letter
                    //width: (word.text.length) > 0 ? (word.width / word.text.length) - row.spacing : 10
                    //height: word.height
                    text: word.text.charAt(index)
                    anchors.fill:parent
                    z:100
                }
            }
        }

        Rectangle { width: 10; height: word.height; color: "blue" }
    }
}
