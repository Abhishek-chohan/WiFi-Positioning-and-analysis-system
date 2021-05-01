# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import strength,speed, zone
import connectedUser as cu
import networkMonitor as nm
import wifiPosition as wp
import RouterInfo as ri
from Script import GetWiFiReport as gwr


class Ui_MainWindow(object):
    def __init__(self):
        self.form = None

    def signal_test(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = strength.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.init()

    def speed_test(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = speed.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.init()

    def getWiFiReport(self):
        gwr.run()

    def connected_users(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = cu.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.init()

    def zones(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = zone.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def wifi_position(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = wp.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def network_monitering(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = nm.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def router_info(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = ri.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(949, 719)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.monitorUser = QtWidgets.QPushButton(self.centralwidget)
        self.monitorUser.setGeometry(QtCore.QRect(20, 360, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.monitorUser.setFont(font)
        self.monitorUser.setAutoFillBackground(False)
        self.monitorUser.setStyleSheet("QPushButton{\n"
"background-color:#e6e6fA\n"
"}\n"
"\n"
"QPushButton : pressed{\n"
"background-color:#696969\n"
"}")
        self.monitorUser.setCheckable(True)
        self.monitorUser.setObjectName("monitorUser")
        self.monitorUser.clicked.connect(self.network_monitering)
        self.routerInfo = QtWidgets.QPushButton(self.centralwidget)
        self.routerInfo.setGeometry(QtCore.QRect(20, 290, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.routerInfo.setFont(font)
        self.routerInfo.setAutoFillBackground(False)
        self.routerInfo.setStyleSheet("QPushButton{\n"
"background-color:#e6e6fA\n"
"}\n"
"\n"
"QPushButton : pressed{\n"
"background-color:#696969\n"
"}")
        self.routerInfo.setCheckable(True)
        self.routerInfo.setObjectName("routerInfo")
        self.routerInfo.clicked.connect(self.router_info)
        self.speedTest = QtWidgets.QPushButton(self.centralwidget)
        self.speedTest.setGeometry(QtCore.QRect(20, 570, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.speedTest.setFont(font)
        self.speedTest.setAutoFillBackground(False)
        self.speedTest.setStyleSheet("QPushButton{\n"
"background-color:#e6e6fA\n"
"}\n"
"\n"
"QPushButton : pressed{\n"
"background-color:#696969\n"
"}")
        self.speedTest.setCheckable(True)
        self.speedTest.setObjectName("speedTest")
        self.speedTest.clicked.connect(self.speed_test)

        self.signalTest = QtWidgets.QPushButton(self.centralwidget)
        self.signalTest.setGeometry(QtCore.QRect(20, 500, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.signalTest.setFont(font)
        self.signalTest.setAutoFillBackground(False)
        self.signalTest.setStyleSheet("QPushButton{\n"
"background-color:#e6e6fA\n"
"}\n"
"\n"
"QPushButton : pressed{\n"
"background-color:#696969\n"
"}")
        self.signalTest.setCheckable(True)
        self.signalTest.setObjectName("signalTest")
        self.signalTest.clicked.connect(self.signal_test)

        self.wifiPos = QtWidgets.QPushButton(self.centralwidget)
        self.wifiPos.setGeometry(QtCore.QRect(20, 150, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.wifiPos.setFont(font)
        self.wifiPos.setAcceptDrops(False)
        self.wifiPos.setAutoFillBackground(False)
        self.wifiPos.setStyleSheet("QPushButton{\n"
"background-color:#e6e6fA\n"
"}\n"
"\n"
"QPushButton : pressed{\n"
"background-color:#696969\n"
"}")
        self.wifiPos.setCheckable(True)
        self.wifiPos.setChecked(False)
        self.wifiPos.setDefault(False)
        self.wifiPos.setFlat(False)
        self.wifiPos.setObjectName("wifiPos")
        self.wifiPos.clicked.connect(self.wifi_position)
        self.zone = QtWidgets.QPushButton(self.centralwidget)
        self.zone.setGeometry(QtCore.QRect(20, 220, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.zone.setFont(font)
        self.zone.setAutoFillBackground(False)
        self.zone.setStyleSheet("QPushButton{\n"
"background-color:#e6e6fA\n"
"}\n"
"\n"
"QPushButton : pressed{\n"
"background-color:#696969\n"
"}")
        self.zone.setCheckable(True)
        self.zone.setObjectName("zone")
        self.zone.clicked.connect(self.zones)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 951, 731))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/roteador-e-wifi-casa-notahs-750x450.jpg"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 10, 791, 61))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("QLabel{\n"
"color:#444444\n"
"}\n"
"")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 640, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color:#e6e6fA\n"
"}\n"
"\n"
"QPushButton : pressed{\n"
"background-color:#696969\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.getWiFiReport)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 430, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-color:#e6e6fA\n"
"}\n"
"\n"
"QPushButton : pressed{\n"
"background-color:#696969\n"
"}")
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.connected_users)
        self.label.raise_()
        self.monitorUser.raise_()
        self.routerInfo.raise_()
        self.speedTest.raise_()
        self.signalTest.raise_()
        self.wifiPos.raise_()
        self.zone.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.monitorUser.setText(_translate("MainWindow", "Network Monitoring"))
        self.routerInfo.setText(_translate("MainWindow", "Router\'s Information"))
        self.speedTest.setText(_translate("MainWindow", "Speed Test"))
        self.signalTest.setText(_translate("MainWindow", "Signal Strength Test"))
        self.wifiPos.setText(_translate("MainWindow", "Wi-Fi\'s Position"))
        self.zone.setText(_translate("MainWindow", "Zones Recommendation"))
        self.label_2.setText(_translate("MainWindow", "WI-FI POSITIONING AND ANALYSIS SYSTEM"))
        self.pushButton.setText(_translate("MainWindow", "Get Wi-Fi Report"))
        self.pushButton_2.setText(_translate("MainWindow", "Connected Users"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
