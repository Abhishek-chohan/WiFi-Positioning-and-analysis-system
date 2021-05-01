from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QWidget, QFileDialog, QTextEdit, QPushButton, QLabel, QVBoxLayout)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QDir
import sys

from Script import Centroid_K_means as ckm
from Script import Hinderance_modified as hm
from Script import Predict as p

class DialogApp(QWidget):
    def get_image_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open Image File', r"<Default dir>", "*.jpg *.jpeg *.png")
        return file_name
    
    def get_int(self, msg):
        n,done = QtWidgets.QInputDialog.getInt(self, 'Input Dialog', msg)
        return n,done

    def getHinderenceType(self,n):
        arr = []
        for i in range(n):
            hinderence_type,done = QtWidgets.QInputDialog.getInt(self, 'Input Dialog', 
            'Type of hinderance \n1)Metal Door \n2)Concrete Wall \n3)Brick Wall \n4)Wood window \n5)Glass window\n Enter your hinderence choice')
            arr.append(hinderence_type)
        return arr,done


class Ui_MainWindow(object):

    def upload(self):
        up = DialogApp()
        self.filepath = up.get_image_file()
        self.label.setPixmap(QPixmap(self.filepath))

    def userCentered(self):
        uc = DialogApp()
        n, done2 = uc.get_int('Enter the number of centroids')
        ckm.updateVar(self.filepath, n)
        ckm.main()
        self.label_2.setPixmap(QtGui.QPixmap("image.jpg"))
    
    def idealMap(self):
        p.updateVar(self.filepath)
        p.main()
        self.label_2.setPixmap(QtGui.QPixmap("image.jpg"))
    
    def hinderence(self):
        hind = DialogApp()
        n, done = hind.get_int('Enter the number of hinderances')
        hinderence_type, done2 = hind.getHinderenceType(n)
        hm.updateVar(self.filepath, n, hinderence_type)
        hm.main()
        self.label_2.setPixmap(QtGui.QPixmap("image.jpg"))


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(949, 717)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)

        self.pushButton_3.clicked.connect(self.upload)

        self.pushButton_3.setGeometry(QtCore.QRect(80, 480, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"background-color:#e6e6fa\n"
"}\n"
"\n")
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 951, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel{\n"
"background-color:white\n"
"}")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 160, 300, 300))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/wpfg.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(600, 160, 300, 300))
        self.label_2.setMouseTracking(False)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/wpfg.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)

        self.pushButton.clicked.connect(self.userCentered)

        self.pushButton.setGeometry(QtCore.QRect(370, 200, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color:#e6e6fa\n"
"}\n"
"\n")
        self.pushButton.setCheckable(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.clicked.connect(self.idealMap)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 280, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-color:#e6e6fa\n"
"}\n"
"\n")
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.clicked.connect(self.hinderence)
        self.pushButton_4.setGeometry(QtCore.QRect(370, 360, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"background-color:#e6e6fa\n"
"}\n"
"\n")
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(24, 120, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{\n"
"color:black\n"
"}")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(604, 120, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel{\n"
"color:black\n"
"}")
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 50, 961, 661))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("Images/wifi.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_6.raise_()
        self.label_3.raise_()
        self.pushButton_3.raise_()
        self.label_4.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_4.raise_()
        self.label_5.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "UPLOAD LOCATION MAP"))
        self.label_4.setText(_translate("MainWindow", "OPTIMAL WI-FI POSITIONING"))
        self.pushButton.setText(_translate("MainWindow", "USER CENTERED"))
        self.pushButton_2.setText(_translate("MainWindow", "EMPTY LOCATION MAP"))
        self.pushButton_4.setText(_translate("MainWindow", "MAP WITH HINDERENCE"))
        self.label_3.setText(_translate("MainWindow", "INPUT"))
        self.label_5.setText(_translate("MainWindow", "OUTPUT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
