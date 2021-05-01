from PyQt5 import QtWidgets, uic, QtCore, QtGui
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys, os, time
from Script import speedt


class Ui_MainWindow(object):
    def init(self):

        self.server_info = speedt.getServer()
        #graph plotting
        self.download = [] 
        self.timed = []  

        self.graphWidget.setLabel(axis="left",text='Download Speed (Mbps)')
        self.graphWidget.setLabel(axis="bottom",text='Time')
        pen1 = pg.mkPen(color=(255, 0, 0))
        self.data_lined =  self.graphWidget.plot(self.timed, self.download, name='downloadSpeed', pen=pen1)

        self.timer1 = QtCore.QTimer()
        self.timer1.setInterval(500)
        self.timer1.timeout.connect(self.update_plot_data1)
        self.timer1.start()

    
    def update_plot_data1(self):
        if len(self.download)>20:
            self.download = self.download[1:] #remove the first element
        
        if len(self.timed)>20:
            self.timed = self.timed[1:]  # Remove the first element

        self.string = 'Ping = '+str(speedt.getPing())
        self.string1 = self.string + '\n===Server Info===\n'
        self.string1 += 'IP : ' + str(self.server_info['ip']) + '\nLATTITUDE : ' + str(self.server_info['lat'])
        self.string1 += '\nLONGITUDE : ' + str(self.server_info['lon']) + '\nISP : ' + str(self.server_info['isp'])
        self.string1 += '\nISP-RATING : ' + str(self.server_info['isprating']) + '\nCOUNTRY : ' + str(self.server_info['country'])
        self.label_5.setText(self.string1)

        res_d = speedt.getDownloadSpeed()
        self.download.append(res_d[0])  # Add a new value
        self.timed.append(res_d[1])  # Add a new random value.
        self.data_lined.setData(self.timed, self.download)  # Update the data.

        res_u = speedt.getUploadSpeed()
        self.progressBar.setProperty("value", res_u[0]*5)
        self.progressBar_2.setProperty("value", res_d[0]*5)

        s = 'Upload Speed = ' + str(res_u[0])
        self.label_2.setText(s)

        s = 'Download Speed = ' + str(res_d[0])
        self.label_3.setText(s)





    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(947, 718)
        MainWindow.setStyleSheet("QMainWindow{\n"
"background-color : black\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphWidget = PlotWidget(self.centralwidget)
        self.graphWidget.setGeometry(QtCore.QRect(50, 320, 841, 331))
        self.graphWidget.setStyleSheet("PlotWidget{\n"
"background-color:black\n"
"}")
        self.graphWidget.setObjectName("graphWidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 941, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"background-color:white\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(50, 120, 251, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("QProgressBar{\n"
"color:black\n"
"}")
        self.progressBar.setProperty("value", 78)
        self.progressBar.setObjectName("progressBar")
        self.progressBar_2 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_2.setGeometry(QtCore.QRect(630, 120, 241, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.progressBar_2.setFont(font)
        self.progressBar_2.setStyleSheet("QProgressBar{\n"
"color:black\n"
"}")
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
"color:white\n"
"}")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(630, 80, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{\n"
"color:white\n"
"}")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(320, 110, 241, 131))
        self.label_5.setStyleSheet("QLabel{\n"
"color:white\n"
"}")
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "SPEED TESTING"))
        self.label_2.setText(_translate("MainWindow", "Upload Speed = x"))
        self.label_3.setText(_translate("MainWindow", "Download Speed = x"))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.init()
    sys.exit(app.exec_())
