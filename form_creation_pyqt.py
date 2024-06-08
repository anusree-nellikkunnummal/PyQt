from PyQt5 import QtCore, QtGui, QtWidgets


class UiForm(object):
    """ Create a form """
    def setup_ui(self, form):
        form.setObjectName("Form")
        form.resize(1000, 840)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 20, 1000, 840))
        self.frame.setStyleSheet("background-color: rgb(252, 255, 240);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 1000, 181))
        self.frame_2.setStyleSheet("background-color: rgb(255, 235, 161);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        # label to display non-editable text
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(140, 40, 60, 14))
        self.label.setObjectName("label")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(350, 63, 350, 75))
        self.label_8.setStyleSheet("color: rgb(17, 28, 93); font: 75 22pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(240, 0, 251, 20))
        self.label_9.setStyleSheet("color: rgb(102, 102, 102); font: 7pt \"Times New Roman\";\n")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(440, 135, 501, 16))
        self.label_10.setStyleSheet("font: 8pt \"Trebuchet MS\"; color: rgb(64, 84, 154);\n")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(460, 63, 111, 75))
        self.label_11.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\"; color: rgb(99, 113, 135);")
        self.label_11.setObjectName("label_11")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(150, 300, 160, 19))
        self.label_2.setStyleSheet("font: 9pt MS Shell Dlg 2;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(395, 300, 160, 19))
        self.label_3.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(640, 300, 160, 19))
        self.label_4.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(150, 430, 160, 19))
        self.label_5.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(395, 430, 160, 19))
        self.label_6.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(640, 430, 160, 19))
        self.label_7.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        # clickable button
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(420, 650, 160, 39))
        self.pushButton.setObjectName("pushButton")
        # allows users to enter and edit a single line of plain text
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 340, 200, 40))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(390, 340, 200, 40))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_6.setGeometry(QtCore.QRect(640, 340, 200, 40))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_8.setGeometry(QtCore.QRect(150, 470, 200, 40))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_9.setGeometry(QtCore.QRect(390, 470, 200, 40))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.spinBox = QtWidgets.QSpinBox(self.frame)
        self.spinBox.setGeometry(QtCore.QRect(640, 470, 200, 40))
        self.spinBox.setObjectName("spinBox")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(500, 0, 501, 20))
        self.label_13.setStyleSheet("color: rgb(102, 102, 102); background-color: rgb(255, 235, 161); font: 7pt Times New Roman;")
        self.label_13.setObjectName("label_13")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_8.setText(_translate("Form", "Algo"))
        self.label_10.setText(_translate("Form", "Establish the in-houseUser"))
        self.label_11.setText(_translate("Form", "miz"))
        self.label_2.setText(_translate("Form", "First Name"))
        self.label_3.setText(_translate("Form", "Last Name"))
        self.label_4.setText(_translate("Form", "Project"))
        self.label_5.setText(_translate("Form", "Email Id"))
        self.label_6.setText(_translate("Form", "Role"))
        self.label_7.setText(_translate("Form", "Employee Id"))
        self.pushButton.setText(_translate("Form", "Create"))
        self.label_13.setText(_translate("Form", "Copyright (c) 2023, Anusree Narayan All rights reserved"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = UiForm()
    ui.setup_ui(Form)
    Form.show()
    sys.exit(app.exec_())
