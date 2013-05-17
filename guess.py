# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guess.ui'
#
# Created: Thu May 16 04:45:51 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import functools

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
i = 0
shown = []
class Ui_MainWindow(object):

    def check(self,imgName):
        global i
        global shown
        if(i<=1):
            if(imgName == "img1"):
                self.img1.setStyleSheet(_fromUtf8("background-image: url(\':/nums/images/8.png\');"))
                i +=1
                shown.append(self.img1)
                shown.append(8)
            if(imgName == "img2"):
                self.img2.setStyleSheet(_fromUtf8("background-image: url(\':/nums/images/5.png\');"))
                i +=1
                shown.append(self.img2)
                shown.append(5)
            if(imgName == "img3"):
                self.img3.setStyleSheet(_fromUtf8("background-image: url(\':/nums/images/3.png\');"))
                i +=1
                shown.append(self.img3)
                shown.append(3)
            if(imgName == "img4"):
                self.img4.setStyleSheet(_fromUtf8("background-image: url(\':/nums/images/4.png\');"))
                i +=1
                shown.append(self.img4)
                shown.append(4)
            if(imgName == "img5"):
                self.img5.setStyleSheet(_fromUtf8("background-image: url(\':/nums/images/2.png\');"))
                i +=1
                shown.append(self.img5)
                shown.append(2)
            if(imgName == "img6"):
                self.img6.setStyleSheet(_fromUtf8("background-image: url(\':/nums/images/6.png\');"))
                i +=1
                shown.append(self.img6)
                shown.append(6)
            if(imgName == "img7"):
                self.img7.setStyleSheet(_fromUtf8("background-image: url(\':/nums/images/7.png\');"))
                i +=1
                shown.append(self.img7)
                shown.append(7)
            if(imgName == "img8"):
                self.img8.setStyleSheet(_fromUtf8("background-image: url(\':/nums/images/1.png\');"))
                i +=1
                shown.append(self.img8)
                shown.append(1)
            if(imgName == "img9"):
                self.img9.setStyleSheet(_fromUtf8("background-image: url(\':/nums/images/4.png\');"))
                i +=1
                shown.append(self.img9)
                shown.append(4)
            if(imgName == "img10"):
                self.img10.setStyleSheet(_fromUtf8("background-image: url(\':/nums/images/2.png\');"))
                i +=1
                shown.append(self.img10)
                shown.append(2)
            if(imgName == "img11"):
                self.img11.setStyleSheet(_fromUtf8("background-image: url(\':/nums/images/8.png\');"))
                i +=1
                shown.append(self.img11)
                shown.append(8)
            if(imgName == "img12"):
                self.img12.setStyleSheet(_fromUtf8("background-image: url(\':/nums/images/3.png\');"))
                i +=1
                shown.append(self.img12)
                shown.append(3)
            if(imgName == "img13"):
                self.img13.setStyleSheet(_fromUtf8("background-image: url(\':/nums/images/7.png\');"))
                i +=1
                shown.append(self.img13)
                shown.append(7)
            if(imgName == "img14"):
                self.img14.setStyleSheet(_fromUtf8("background-image: url(\':/nums/images/5.png\');"))
                i +=1
                shown.append(self.img14)
                shown.append(5)
            if(imgName == "img15"):
                self.img15.setStyleSheet(_fromUtf8("background-image: url(\':/nums/images/1.png\');"))
                i +=1
                shown.append(self.img15)
                shown.append(1)
            if(imgName == "img16"):
                self.img16.setStyleSheet(_fromUtf8("background-image: url(\':/nums/images/6.png\');"))
                i +=1
                shown.append(self.img16)
                shown.append(6)

        elif(i == 2):
            if(shown[1] == shown[3]):
                i = 0
                shown = []
                print "Correct"
            else:
                i = 0
                shown[0].setStyleSheet(_fromUtf8("background-image: url(\':/qMark/images/?.png\');"))
                shown[2].setStyleSheet(_fromUtf8("background-image: url(\':/qMark/images/?.png\');"))
                shown = []
                
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("Guess & check game"))
        MainWindow.resize(699, 689)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.img1 = QtGui.QPushButton(self.centralwidget)
        self.img1.setGeometry(QtCore.QRect(30, 20, 150, 150))
        self.img1.setStyleSheet(_fromUtf8("background-image: url(\':/qMark/images/?.png\');"))
        self.img1.setText(_fromUtf8(""))
        self.img1.setObjectName(_fromUtf8("img1"))
        self.img5 = QtGui.QPushButton(self.centralwidget)
        self.img5.setGeometry(QtCore.QRect(30, 170, 150, 150))
        self.img5.setStyleSheet(_fromUtf8("background-image: url(\':/qMark/images/?.png\');"))
        self.img5.setText(_fromUtf8(""))
        self.img5.setObjectName(_fromUtf8("img5"))
        self.img9 = QtGui.QPushButton(self.centralwidget)
        self.img9.setGeometry(QtCore.QRect(30, 320, 150, 150))
        self.img9.setStyleSheet(_fromUtf8("background-image: url(\':/qMark/images/?.png\');"))
        self.img9.setText(_fromUtf8(""))
        self.img9.setObjectName(_fromUtf8("img9"))
        self.img13 = QtGui.QPushButton(self.centralwidget)
        self.img13.setGeometry(QtCore.QRect(30, 470, 150, 150))
        self.img13.setStyleSheet(_fromUtf8("background-image: url(\':/qMark/images/?.png\');"))
        self.img13.setText(_fromUtf8(""))
        self.img13.setObjectName(_fromUtf8("img13"))
        self.img14 = QtGui.QPushButton(self.centralwidget)
        self.img14.setGeometry(QtCore.QRect(190, 470, 150, 150))
        self.img14.setStyleSheet(_fromUtf8("background-image: url(\':/qMark/images/?.png\');"))
        self.img14.setText(_fromUtf8(""))
        self.img14.setObjectName(_fromUtf8("img14"))
        self.img10 = QtGui.QPushButton(self.centralwidget)
        self.img10.setGeometry(QtCore.QRect(190, 320, 150, 150))
        self.img10.setStyleSheet(_fromUtf8("background-image: url(\':/qMark/images/?.png\');"))
        self.img10.setText(_fromUtf8(""))
        self.img10.setObjectName(_fromUtf8("img10"))
        self.img2 = QtGui.QPushButton(self.centralwidget)
        self.img2.setGeometry(QtCore.QRect(190, 20, 150, 150))
        self.img2.setStyleSheet(_fromUtf8("background-image: url(\':/qMark/images/?.png\');"))
        self.img2.setText(_fromUtf8(""))
        self.img2.setObjectName(_fromUtf8("img2"))
        self.img6 = QtGui.QPushButton(self.centralwidget)
        self.img6.setGeometry(QtCore.QRect(190, 170, 150, 150))
        self.img6.setStyleSheet(_fromUtf8("background-image: url(\':/qMark/images/?.png\');"))
        self.img6.setText(_fromUtf8(""))
        self.img6.setObjectName(_fromUtf8("img6"))
        self.img15 = QtGui.QPushButton(self.centralwidget)
        self.img15.setGeometry(QtCore.QRect(350, 470, 150, 150))
        self.img15.setStyleSheet(_fromUtf8("background-image: url(\':/qMark/images/?.png\');"))
        self.img15.setText(_fromUtf8(""))
        self.img15.setObjectName(_fromUtf8("img15"))
        self.img11 = QtGui.QPushButton(self.centralwidget)
        self.img11.setGeometry(QtCore.QRect(350, 320, 150, 150))
        self.img11.setStyleSheet(_fromUtf8("background-image: url(\':/qMark/images/?.png\');"))
        self.img11.setText(_fromUtf8(""))
        self.img11.setObjectName(_fromUtf8("img11"))
        self.img3 = QtGui.QPushButton(self.centralwidget)
        self.img3.setGeometry(QtCore.QRect(350, 20, 150, 150))
        self.img3.setStyleSheet(_fromUtf8("background-image: url(\':/qMark/images/?.png\');"))
        self.img3.setText(_fromUtf8(""))
        self.img3.setObjectName(_fromUtf8("img3"))
        self.img7 = QtGui.QPushButton(self.centralwidget)
        self.img7.setGeometry(QtCore.QRect(350, 170, 150, 150))
        self.img7.setStyleSheet(_fromUtf8("background-image: url(\':/qMark/images/?.png\');"))
        self.img7.setText(_fromUtf8(""))
        self.img7.setObjectName(_fromUtf8("img7"))
        self.img16 = QtGui.QPushButton(self.centralwidget)
        self.img16.setGeometry(QtCore.QRect(510, 470, 150, 150))
        self.img16.setStyleSheet(_fromUtf8("background-image: url(\':/qMark/images/?.png\');"))
        self.img16.setText(_fromUtf8(""))
        self.img16.setObjectName(_fromUtf8("img16"))
        self.img12 = QtGui.QPushButton(self.centralwidget)
        self.img12.setGeometry(QtCore.QRect(510, 320, 150, 150))
        self.img12.setStyleSheet(_fromUtf8("background-image: url(\':/qMark/images/?.png\');"))
        self.img12.setText(_fromUtf8(""))
        self.img12.setObjectName(_fromUtf8("img12"))
        self.img4 = QtGui.QPushButton(self.centralwidget)
        self.img4.setGeometry(QtCore.QRect(510, 20, 150, 150))
        self.img4.setStyleSheet(_fromUtf8("background-image: url(\':/qMark/images/?.png\');"))
        self.img4.setText(_fromUtf8(""))
        self.img4.setObjectName(_fromUtf8("img4"))
        self.img8 = QtGui.QPushButton(self.centralwidget)
        self.img8.setGeometry(QtCore.QRect(510, 170, 150, 150))
        self.img8.setStyleSheet(_fromUtf8("background-image: url(\':/qMark/images/?.png\');"))
        self.img8.setText(_fromUtf8(""))
        self.img8.setObjectName(_fromUtf8("img8"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 699, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.img1, QtCore.SIGNAL(_fromUtf8("clicked()")), functools.partial(self.check,"img1"))
        QtCore.QObject.connect(self.img2, QtCore.SIGNAL(_fromUtf8("clicked()")), functools.partial(self.check,"img2"))
        QtCore.QObject.connect(self.img3, QtCore.SIGNAL(_fromUtf8("clicked()")), functools.partial(self.check,"img3"))
        QtCore.QObject.connect(self.img4, QtCore.SIGNAL(_fromUtf8("clicked()")), functools.partial(self.check,"img4"))
        QtCore.QObject.connect(self.img5, QtCore.SIGNAL(_fromUtf8("clicked()")), functools.partial(self.check,"img5"))
        QtCore.QObject.connect(self.img6, QtCore.SIGNAL(_fromUtf8("clicked()")), functools.partial(self.check,"img6"))
        QtCore.QObject.connect(self.img7, QtCore.SIGNAL(_fromUtf8("clicked()")), functools.partial(self.check,"img7"))
        QtCore.QObject.connect(self.img8, QtCore.SIGNAL(_fromUtf8("clicked()")), functools.partial(self.check,"img8"))
        QtCore.QObject.connect(self.img9, QtCore.SIGNAL(_fromUtf8("clicked()")), functools.partial(self.check,"img9"))
        QtCore.QObject.connect(self.img10, QtCore.SIGNAL(_fromUtf8("clicked()")), functools.partial(self.check,"img10"))
        QtCore.QObject.connect(self.img11, QtCore.SIGNAL(_fromUtf8("clicked()")), functools.partial(self.check,"img11"))
        QtCore.QObject.connect(self.img12, QtCore.SIGNAL(_fromUtf8("clicked()")), functools.partial(self.check,"img12"))
        QtCore.QObject.connect(self.img13, QtCore.SIGNAL(_fromUtf8("clicked()")), functools.partial(self.check,"img13"))
        QtCore.QObject.connect(self.img14, QtCore.SIGNAL(_fromUtf8("clicked()")), functools.partial(self.check,"img14"))
        QtCore.QObject.connect(self.img15, QtCore.SIGNAL(_fromUtf8("clicked()")), functools.partial(self.check,"img15"))
        QtCore.QObject.connect(self.img16, QtCore.SIGNAL(_fromUtf8("clicked()")), functools.partial(self.check,"img16"))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("Guess & check game", "Guess & check game", None, QtGui.QApplication.UnicodeUTF8))

import resources

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

