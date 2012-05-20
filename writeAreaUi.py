# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'writeArea.ui'
#
# Created: Fri Apr  6 14:46:19 2012
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(786, 549)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Andika Basic")
        Form.setFont(font)
        Form.setStyleSheet("#topFrame {\n"
"border: none;\n"
"background:27281a;\n"
"} \n"
"#bottomFrame {\n"
"border: none;\n"
"background:27281a;\n"
"}\n"
"\n"
"#topFrame QPushButton {\n"
"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 11px;\n"
"padding: 5px;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #888);\n"
"min-width: 80px;\n"
"} \n"
"#topFrame QPushButton:hover {\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb);\n"
"}\n"
"#topFrame QPushButton:pressed {\n"
"background: qradialgradient(cx: 0.4, cy: -0.1,\n"
"fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
"}\n"
"#topFrame QComboBox {\n"
"color: #000;\n"
"border: 2px solid #555;\n"
"border-radius: 11px;\n"
"padding: 5px;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #888);\n"
"min-width: 120px;\n"
"} \n"
"#topFrame QComboBox:hover {\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb);\n"
"}\n"
"#topFrame QComboBox:pressed {\n"
"background: qradialgradient(cx: 0.4, cy: -0.1,\n"
"fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
"}\n"
"\n"
"")
        self.gridLayout_2 = QtGui.QGridLayout(Form)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.topFrame = QtGui.QFrame(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topFrame.sizePolicy().hasHeightForWidth())
        self.topFrame.setSizePolicy(sizePolicy)
        self.topFrame.setStyleSheet("background-color: rgb(39, 40, 26);")
        self.topFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.topFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.topFrame.setObjectName("topFrame")
        self.gridLayout = QtGui.QGridLayout(self.topFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.quitButton = QtGui.QPushButton(self.topFrame)
        self.quitButton.setStyleSheet("background-color: rgb(223,216,174);")
        self.quitButton.setObjectName("quitButton")
        self.gridLayout.addWidget(self.quitButton, 0, 9, 1, 1)
        self.clearButton = QtGui.QPushButton(self.topFrame)
        self.clearButton.setStyleSheet("background-color: rgb(223,216,174);")
        self.clearButton.setObjectName("clearButton")
        self.gridLayout.addWidget(self.clearButton, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 5, 1, 1)
        self.languageComboBox = QtGui.QComboBox(self.topFrame)
        self.languageComboBox.setStyleSheet("background-color: rgb(223,216,174);")
        self.languageComboBox.setObjectName("languageComboBox")
        self.gridLayout.addWidget(self.languageComboBox, 0, 3, 1, 1)
        self.setButton = QtGui.QPushButton(self.topFrame)
        self.setButton.setStyleSheet("background-color: rgb(223,216,174);")
        self.setButton.setObjectName("setButton")
        self.gridLayout.addWidget(self.setButton, 0, 8, 1, 1)
        self.charshowBut = QtGui.QPushButton(self.topFrame)
        self.charshowBut.setStyleSheet("background-color: rgb(223,216,174);")
        self.charshowBut.setCheckable(True)
        self.charshowBut.setChecked(True)
        self.charshowBut.setObjectName("charshowBut")
        self.gridLayout.addWidget(self.charshowBut, 0, 2, 1, 1)
        self.gridLayout_2.addWidget(self.topFrame, 0, 0, 1, 1)
        self.bottomFrame = QtGui.QFrame(Form)
        self.bottomFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.bottomFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.bottomFrame.setObjectName("bottomFrame")
        self.gridLayout_3 = QtGui.QGridLayout(self.bottomFrame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout2 = QtGui.QGridLayout()
        self.gridLayout2.setObjectName("gridLayout2")
        self.gridLayout_3.addLayout(self.gridLayout2, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.bottomFrame, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.quitButton.setText(QtGui.QApplication.translate("Form", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.clearButton.setText(QtGui.QApplication.translate("Form", "ClearPage", None, QtGui.QApplication.UnicodeUTF8))
        self.setButton.setText(QtGui.QApplication.translate("Form", "Monitor Caliberate", None, QtGui.QApplication.UnicodeUTF8))
        self.charshowBut.setText(QtGui.QApplication.translate("Form", "showCharacters", None, QtGui.QApplication.UnicodeUTF8))

