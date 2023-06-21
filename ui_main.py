# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\ui\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(741, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_login = LoginTab()
        self.tab_login.setObjectName("tab_login")
        self.tabWidget.addTab(self.tab_login, "")
        self.tab_home = HomeTab()
        self.tab_home.setObjectName("tab_home")
        self.tabWidget.addTab(self.tab_home, "")
        self.tab_data = DataTab()
        self.tab_data.setObjectName("tab_data")
        self.tabWidget.addTab(self.tab_data, "")
        self.tab_last_page = LastTab()
        self.tab_last_page.setObjectName("tab_last_page")
        self.tabWidget.addTab(self.tab_last_page, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 741, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_login), _translate("MainWindow", "Login"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_home), _translate("MainWindow", "Home"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_data), _translate("MainWindow", "Data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_last_page), _translate("MainWindow", "Last Page"))
from pages.data_tab import DataTab
from pages.home_tab import HomeTab
from pages.last_tab import LastTab
from pages.login_tab import LoginTab


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
