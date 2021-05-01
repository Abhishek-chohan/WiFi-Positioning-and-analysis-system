from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QWidget, QFileDialog, QTextEdit, QPushButton, QLabel, QVBoxLayout)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QDir
import sys
import zonedemo as zd



class DialogApp(QWidget):
    def get_image_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open Image File', r"<Default dir>", "*.jpg *.jpeg *.png")
        return file_name
    def get_int(self, msg):
        n,done = QtWidgets.QInputDialog.getInt(self, 'Input Dialog', msg)
        return n

class Ui_MainWindow(object):

    def upload(self):
        up = DialogApp()
        self.filepath = up.get_image_file()
        self.label_2.setPixmap(QPixmap(self.filepath))

    def generateMap(self):
        obj = DialogApp()
        x = obj.get_int('Enter X-coordinate:')
        y = obj.get_int('Enter Y-coordinate:')
        zd.updateVar(self.filepath,x,y)
        zd.main()
        self.label_2.setPixmap(QPixmap('heatmap2.png'))


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(948, 718)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 951, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"background-color:white\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 751, 521))
        self.label_2.setStyleSheet("QLabel{\n"
"background-color:white\n"
"}")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(''))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(470, 620, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setCheckable(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.generateMap)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 620, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.upload)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "NETWORK ZONE RECOMMENDATION"))
        self.pushButton.setText(_translate("MainWindow", "Generate Heat Map"))
        self.pushButton_2.setText(_translate("MainWindow", "Upload Image"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
