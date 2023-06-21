# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\login_tab.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(399, 228)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_3)
        self.lineEdit_username = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_username)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit_password = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_password)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.pushButton_login = QtWidgets.QPushButton(self.widget)
        self.pushButton_login.setObjectName("pushButton_login")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.pushButton_login)
        self.label_username_error = QtWidgets.QLabel(self.widget)
        self.label_username_error.setText("")
        self.label_username_error.setObjectName("label_username_error")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_username_error)
        self.label_password_error = QtWidgets.QLabel(self.widget)
        self.label_password_error.setText("")
        self.label_password_error.setObjectName("label_password_error")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.label_password_error)
        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Login Page"))
        self.lineEdit_username.setPlaceholderText(_translate("Form", "Enter your username"))
        self.label.setText(_translate("Form", "Username"))
        self.lineEdit_password.setPlaceholderText(_translate("Form", "Enter your password"))
        self.label_2.setText(_translate("Form", "Password"))
        self.pushButton_login.setText(_translate("Form", "Login"))
        self.pushButton_login.setShortcut(_translate("Form", "Ctrl+S, Ctrl+S, Ctrl+S, Ctrl+S"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
