# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'musPlayer.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_musPlayer(object):
    def setupUi(self, musPlayer):
        musPlayer.setObjectName("musPlayer")
        musPlayer.resize(1017, 501)
        musPlayer.setAcceptDrops(True)
        musPlayer.setAutoFillBackground(False)
        musPlayer.setStyleSheet("QWidget{background-color: #555555;}\n"
"QPushButton{\n"
"background-color: #CCCCCC;\n"
"font-size: 19px;\n"
"border: 2px solid black;    \n"
"}\n"
"QListWidget{\n"
"background-color: #CCCCCC;\n"
"font-size: 19px;    \n"
"border: 2px solid black;\n"
"}\n"
"QLabel{\n"
"background-color: #CCCCCC;\n"
"font-size: 19px;    \n"
"border: 2px solid black;\n"
"}\n"
"QCheckBox{\n"
"background-color: #CCCCCC;\n"
"font-size: 19px;    \n"
"border: 2px solid black;\n"
"}\n"
"QSlider{\n"
"background-color: #CCCCCC;\n"
"font-size: 19px;    \n"
"border: 2px solid black;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(musPlayer)
        self.centralwidget.setObjectName("centralwidget")
        self.playPauseButton = QtWidgets.QPushButton(self.centralwidget)
        self.playPauseButton.setGeometry(QtCore.QRect(150, 340, 101, 81))
        self.playPauseButton.setObjectName("playPauseButton")
        self.removeButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeButton.setGeometry(QtCore.QRect(860, 40, 111, 41))
        self.removeButton.setObjectName("removeButton")
        self.musicname = QtWidgets.QLabel(self.centralwidget)
        self.musicname.setGeometry(QtCore.QRect(40, 210, 411, 51))
        self.musicname.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.musicname.setAutoFillBackground(False)
        self.musicname.setText("")
        self.musicname.setAlignment(QtCore.Qt.AlignCenter)
        self.musicname.setObjectName("musicname")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(730, 40, 111, 41))
        self.addButton.setObjectName("addButton")
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(150, 430, 101, 51))
        self.stopButton.setObjectName("stopButton")
        self.prevButton = QtWidgets.QPushButton(self.centralwidget)
        self.prevButton.setGeometry(QtCore.QRect(80, 350, 61, 61))
        self.prevButton.setStyleSheet("font-size: 31px;")
        self.prevButton.setObjectName("prevButton")
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(260, 350, 61, 61))
        self.nextButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.nextButton.setStyleSheet("font-size: 31px;")
        self.nextButton.setFlat(False)
        self.nextButton.setObjectName("nextButton")
        self.muspikt = QtWidgets.QLabel(self.centralwidget)
        self.muspikt.setGeometry(QtCore.QRect(20, 10, 430, 190))
        self.muspikt.setText("")
        self.muspikt.setPixmap(QtGui.QPixmap("C:/Users/Viktor/Downloads/muspikt.jpg"))
        self.muspikt.setScaledContents(True)
        self.muspikt.setObjectName("muspikt")
        self.volumeSlider = QtWidgets.QSlider(self.centralwidget)
        self.volumeSlider.setGeometry(QtCore.QRect(490, 60, 41, 181))
        self.volumeSlider.setOrientation(QtCore.Qt.Vertical)
        self.volumeSlider.setObjectName("volumeSlider")
        self.repeatBox = QtWidgets.QCheckBox(self.centralwidget)
        self.repeatBox.setGeometry(QtCore.QRect(380, 380, 141, 31))
        self.repeatBox.setObjectName("repeatBox")
        self.repeatallBox = QtWidgets.QCheckBox(self.centralwidget)
        self.repeatallBox.setGeometry(QtCore.QRect(380, 420, 141, 31))
        self.repeatallBox.setObjectName("repeatallBox")
        self.musiclist = QtWidgets.QListWidget(self.centralwidget)
        self.musiclist.setGeometry(QtCore.QRect(555, 90, 431, 361))
        self.musiclist.setObjectName("musiclist")
        self.timerLabel = QtWidgets.QLabel(self.centralwidget)
        self.timerLabel.setGeometry(QtCore.QRect(360, 270, 111, 41))
        self.timerLabel.setText("")
        self.timerLabel.setObjectName("timerLabel")
        self.songSlider = QtWidgets.QSlider(self.centralwidget)
        self.songSlider.setGeometry(QtCore.QRect(40, 270, 301, 41))
        self.songSlider.setOrientation(QtCore.Qt.Horizontal)
        self.songSlider.setObjectName("songSlider")
        musPlayer.setCentralWidget(self.centralwidget)

        self.retranslateUi(musPlayer)
        QtCore.QMetaObject.connectSlotsByName(musPlayer)

    def retranslateUi(self, musPlayer):
        _translate = QtCore.QCoreApplication.translate
        musPlayer.setWindowTitle(_translate("musPlayer", "musPlayer"))
        self.playPauseButton.setText(_translate("musPlayer", "Play/Pause"))
        self.removeButton.setText(_translate("musPlayer", "Remove"))
        self.addButton.setText(_translate("musPlayer", "Add"))
        self.stopButton.setText(_translate("musPlayer", "Stop"))
        self.prevButton.setText(_translate("musPlayer", "◄"))
        self.nextButton.setText(_translate("musPlayer", "►"))
        self.repeatBox.setText(_translate("musPlayer", "Repeat"))
        self.repeatallBox.setText(_translate("musPlayer", "Repeat All"))
