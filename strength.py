import sys, os, time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets, uic
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import subprocess


SEARCH = b"system:"
TERM_LINE = "Name"

def copynet(netint):
    li=[]
    for i in range(len(netint)):
        if SEARCH in netint[i]:
            break
    for i in range(i+2,20):
        li.append(netint[i].decode('UTF-8'))
    return(li)

def get_item2(i):
    st=li[i]
    a=st.split(":")
    ans=a[-1]
    if i==3 or i==6:
        ans=a[1]+":"+a[2]+":"+a[3]+":"+a[4]+":"+a[5]+":"+a[6]
    #print(ans)
    return (ans.strip())

COMMAND = "netsh wlan show interface"
netint = subprocess.check_output(COMMAND).split(b"\n")
li=copynet(netint)


class Ui_MainWindow(object):
    def init(self, *args, **kwargs):
        
        self.t=[1,2,3,4,5,6,7,8,9,10]
        self.signalStrength=[0,0,0,0,0,0,0,0,0,0]
            
        self.graphWidget.setLabel(axis="left",text='Signal Strength(%)')
        self.graphWidget.setLabel(axis="bottom",text='Time')
        pen1 = pg.mkPen(color=(255, 0, 0))
        self.data_lined =  self.graphWidget.plot(self.t, self.signalStrength, pen=pen1)

        self.timer1 = QtCore.QTimer()
        self.timer1.setInterval(500)
        self.timer1.timeout.connect(self.update_plot_data1)
        self.timer1.start()

    
    def update_plot_data1(self):
        if len(self.signalStrength)>0:
            self.signalStrength = self.signalStrength[1:] #remove the first element

        netint = subprocess.check_output(COMMAND).split(b"\n")
        li=copynet(netint)

        var = int(get_item2(15).strip("%"))
        self.signalStrength.append(var)
        self.data_lined.setData(self.t, self.signalStrength) 

        self.progressBar.setProperty("value", var)
        

    def plot(self, t, signalStrength):
        self.graphWidget.setLabel(axis="left",text='Y-axis')
        self.graphWidget.setLabel(axis="bottom",text='X-axis')
        self.graphWidget.plot(t, signalStrength)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(947, 719)
        MainWindow.setStyleSheet("QMainWindow{\n"
"background-color : black\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphWidget = PlotWidget(self.centralwidget)
        self.graphWidget.setGeometry(QtCore.QRect(50, 380, 851, 281))
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
        self.progressBar.setGeometry(QtCore.QRect(600, 130, 251, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("QProgressBar{\n"
"color:white\n"
"}")
        self.progressBar.setProperty("value", 78)
        self.progressBar.setObjectName("progressBar")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(600, 240, 211, 31))
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
        self.label_3.setGeometry(QtCore.QRect(30, 80, 471, 191))
        self.label_3.setStyleSheet("QLabel{\n"
"color:white\n"
"}")
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "SIGNAL STRENGTH TESTING"))
        self.label_2.setText(_translate("MainWindow", "AVG SIGNAL STRENGTH"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
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
