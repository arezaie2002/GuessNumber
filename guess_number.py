# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guess-number.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 500)
        MainWindow.setMaximumSize(QtCore.QSize(900, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 900, 500))
        self.label.setMaximumSize(QtCore.QSize(900, 500))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("back.png"))
        self.label.setObjectName("label")
        self.label_num = QtWidgets.QLabel(self.centralwidget)
        self.label_num.setGeometry(QtCore.QRect(170, 110, 100, 200))
        self.label_num.setMaximumSize(QtCore.QSize(100, 200))
        self.label_num.setText("")
        self.label_num.setPixmap(QtGui.QPixmap("../Python/dice-project/00.png"))
        self.label_num.setObjectName("label_num")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(870, 20, 16, 16))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("background-color: rgb(138, 12, 19);\n"
"border-radius:6px;")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(850, 20, 16, 16))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("border-radius:6px;\n"
"background-color: rgb(220, 71, 3);")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(300, 320, 601, 171))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Typewriter")
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Typewriter")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(510, 160, 181, 44))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-radius : 6px ;\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(540, 240, 121, 41))
        self.pushButton.setStyleSheet("QPushButton {\n"
"  background: #3498db;\n"
"  background-image: -webkit-linear-gradient(top, #3498db, #2980b9);\n"
"  background-image: -moz-linear-gradient(top, #3498db, #2980b9);\n"
"  background-image: -ms-linear-gradient(top, #3498db, #2980b9);\n"
"  background-image: -o-linear-gradient(top, #3498db, #2980b9);\n"
"  background-image: linear-gradient(to bottom, #3498db, #2980b9);\n"
"  border-radius: 28 px;\n"
"  -moz-border-radius: 28;\n"
"  border-radius: 28px;\n"
"  -webkit-box-shadow: 0px 1px 3px #666666;\n"
"  -moz-box-shadow: 0px 1px 3px #666666;\n"
"  box-shadow: 0px 1px 3px #666666;\n"
"  font-family: Georgia;\n"
"  color: #ffffff;\n"
"  font-size: 20px;\n"
"  background: #3498db;\n"
"  padding: 10px 20px 10px 20px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #000c14;\n"
"  background-image: -webkit-linear-gradient(top, #000c14, #3498db);\n"
"  background-image: -moz-linear-gradient(top, #000c14, #3498db);\n"
"  background-image: -ms-linear-gradient(top, #000c14, #3498db);\n"
"  background-image: -o-linear-gradient(top, #000c14, #3498db);\n"
"  background-image: linear-gradient(to bottom, #000c14, #3498db);\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_3.clicked.connect(MainWindow.showMinimized)
        self.pushButton_2.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Arezaie2002"))
        self.label_4.setText(_translate("MainWindow", "1-100"))
        self.label_3.setText(_translate("MainWindow", "Good Luck"))
        self.lineEdit.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Click Me"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
