# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'equalizer.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ecualizer(object):
    def setupUi(self, Ecualizer):
        Ecualizer.setObjectName("Ecualizer")
        Ecualizer.resize(300, 400)
        Ecualizer.setStyleSheet("background:qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41,61,132,235),stop:1 rgba(155,79,165,255));")
        self.label = QtWidgets.QLabel(Ecualizer)
        self.label.setGeometry(QtCore.QRect(25, 220, 20, 29))
        self.label.setStyleSheet("background-color:none;\n"
"color:white;\n"
"font-size:10px;")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Ecualizer)
        self.label_3.setGeometry(QtCore.QRect(50, 220, 20, 29))
        self.label_3.setStyleSheet("background-color:none;\n"
"color:white;\n"
"font-size:10px;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Ecualizer)
        self.label_4.setGeometry(QtCore.QRect(75, 220, 20, 29))
        self.label_4.setStyleSheet("background-color:none;\n"
"color:white;\n"
"font-size:10px;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Ecualizer)
        self.label_5.setGeometry(QtCore.QRect(100, 220, 20, 29))
        self.label_5.setStyleSheet("background-color:none;\n"
"color:white;\n"
"font-size:10px;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Ecualizer)
        self.label_6.setGeometry(QtCore.QRect(125, 220, 20, 29))
        self.label_6.setStyleSheet("background-color:none;\n"
"color:white;\n"
"font-size:10px;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Ecualizer)
        self.label_7.setGeometry(QtCore.QRect(155, 220, 20, 29))
        self.label_7.setStyleSheet("background-color:none;\n"
"color:white;\n"
"font-size:10px;")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Ecualizer)
        self.label_8.setGeometry(QtCore.QRect(183, 220, 20, 29))
        self.label_8.setStyleSheet("background-color:none;\n"
"color:white;\n"
"font-size:10px;")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Ecualizer)
        self.label_9.setGeometry(QtCore.QRect(208, 220, 20, 29))
        self.label_9.setStyleSheet("background-color:none;\n"
"color:white;\n"
"font-size:10px;")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Ecualizer)
        self.label_10.setGeometry(QtCore.QRect(235, 220, 20, 29))
        self.label_10.setStyleSheet("background-color:none;\n"
"color:white;\n"
"font-size:10px;")
        self.label_10.setObjectName("label_10")
        self.label_19 = QtWidgets.QLabel(Ecualizer)
        self.label_19.setGeometry(QtCore.QRect(260, 220, 20, 29))
        self.label_19.setStyleSheet("background-color:none;\n"
"color:white;\n"
"font-size:10px;")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(Ecualizer)
        self.label_20.setGeometry(QtCore.QRect(90, 20, 120, 81))
        self.label_20.setStyleSheet("background-color:none;\n"
"color:white;\n"
"font-size:30px;")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.frame = QtWidgets.QFrame(Ecualizer)
        self.frame.setGeometry(QtCore.QRect(10, 250, 276, 86))
        self.frame.setStyleSheet("background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);    \n"
"border-radius: 7px;")
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalSlider_1 = QtWidgets.QSlider(self.frame)
        self.verticalSlider_1.setStyleSheet("background-color:none;")
        self.verticalSlider_1.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_1.setObjectName("verticalSlider_1")
        self.horizontalLayout.addWidget(self.verticalSlider_1)
        self.verticalSlider_2 = QtWidgets.QSlider(self.frame)
        self.verticalSlider_2.setStyleSheet("background-color:none;")
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.horizontalLayout.addWidget(self.verticalSlider_2)
        self.verticalSlider_3 = QtWidgets.QSlider(self.frame)
        self.verticalSlider_3.setStyleSheet("background-color:none;")
        self.verticalSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_3.setObjectName("verticalSlider_3")
        self.horizontalLayout.addWidget(self.verticalSlider_3)
        self.verticalSlider_5 = QtWidgets.QSlider(self.frame)
        self.verticalSlider_5.setStyleSheet("background-color:none;")
        self.verticalSlider_5.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_5.setObjectName("verticalSlider_5")
        self.horizontalLayout.addWidget(self.verticalSlider_5)
        self.verticalSlider_4 = QtWidgets.QSlider(self.frame)
        self.verticalSlider_4.setStyleSheet("background-color:none;")
        self.verticalSlider_4.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_4.setObjectName("verticalSlider_4")
        self.horizontalLayout.addWidget(self.verticalSlider_4)
        self.verticalSlider_7 = QtWidgets.QSlider(self.frame)
        self.verticalSlider_7.setStyleSheet("background-color:none;")
        self.verticalSlider_7.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_7.setObjectName("verticalSlider_7")
        self.horizontalLayout.addWidget(self.verticalSlider_7)
        self.verticalSlider_6 = QtWidgets.QSlider(self.frame)
        self.verticalSlider_6.setStyleSheet("background-color:none;")
        self.verticalSlider_6.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_6.setObjectName("verticalSlider_6")
        self.horizontalLayout.addWidget(self.verticalSlider_6)
        self.verticalSlider_8 = QtWidgets.QSlider(self.frame)
        self.verticalSlider_8.setStyleSheet("background-color:none;")
        self.verticalSlider_8.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_8.setObjectName("verticalSlider_8")
        self.horizontalLayout.addWidget(self.verticalSlider_8)
        self.verticalSlider_10 = QtWidgets.QSlider(self.frame)
        self.verticalSlider_10.setStyleSheet("background-color:none;")
        self.verticalSlider_10.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_10.setObjectName("verticalSlider_10")
        self.horizontalLayout.addWidget(self.verticalSlider_10)
        self.verticalSlider_9 = QtWidgets.QSlider(self.frame)
        self.verticalSlider_9.setStyleSheet("background-color:none;")
        self.verticalSlider_9.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_9.setObjectName("verticalSlider_9")
        self.horizontalLayout.addWidget(self.verticalSlider_9)

        self.retranslateUi(Ecualizer)
        QtCore.QMetaObject.connectSlotsByName(Ecualizer)

        default_value = 50
        self.verticalSlider_1.setValue(default_value)
        self.verticalSlider_2.setValue(default_value)
        self.verticalSlider_3.setValue(default_value)
        self.verticalSlider_4.setValue(default_value)
        self.verticalSlider_5.setValue(default_value)
        self.verticalSlider_6.setValue(default_value)
        self.verticalSlider_7.setValue(default_value)
        self.verticalSlider_8.setValue(default_value)
        self.verticalSlider_9.setValue(default_value)
        self.verticalSlider_10.setValue(default_value)



    def retranslateUi(self, Ecualizer):
        _translate = QtCore.QCoreApplication.translate
        Ecualizer.setWindowTitle(_translate("Ecualizer", "Dialog"))
        self.label.setText(_translate("Ecualizer", "32"))
        self.label_3.setText(_translate("Ecualizer", "64"))
        self.label_4.setText(_translate("Ecualizer", "125"))
        self.label_5.setText(_translate("Ecualizer", "250"))
        self.label_6.setText(_translate("Ecualizer", "500"))
        self.label_7.setText(_translate("Ecualizer", "1K"))
        self.label_8.setText(_translate("Ecualizer", "2K"))
        self.label_9.setText(_translate("Ecualizer", "4K"))
        self.label_10.setText(_translate("Ecualizer", "8K"))
        self.label_19.setText(_translate("Ecualizer", "16K"))
        self.label_20.setText(_translate("Ecualizer", "Equalizer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ecualizer = QtWidgets.QDialog()
    ui = Ui_Ecualizer()
    ui.setupUi(Ecualizer)
    Ecualizer.show()
    sys.exit(app.exec_())
