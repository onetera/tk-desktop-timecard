# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created: Thu Dec 07 18:06:16 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(596, 694)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.CIBtn = QtGui.QPushButton(Dialog)
        self.CIBtn.setObjectName("CIBtn")
        self.gridLayout.addWidget(self.CIBtn, 4, 0, 1, 1)
        self.textBrowser = QtGui.QTextBrowser(Dialog)
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 40))
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 3, 0, 1, 4)
        self.COBtn = QtGui.QPushButton(Dialog)
        self.COBtn.setObjectName("COBtn")
        self.gridLayout.addWidget(self.COBtn, 4, 3, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.taskTabWidget = QtGui.QTabWidget(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.taskTabWidget.sizePolicy().hasHeightForWidth())
        self.taskTabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.taskTabWidget.setFont(font)
        self.taskTabWidget.setObjectName("taskTabWidget")
        self.horizontalLayout.addWidget(self.taskTabWidget)
        self.TimeGroupBox = QtGui.QGroupBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TimeGroupBox.sizePolicy().hasHeightForWidth())
        self.TimeGroupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.TimeGroupBox.setFont(font)
        self.TimeGroupBox.setObjectName("TimeGroupBox")
        self.listWidget = QtGui.QListWidget(self.TimeGroupBox)
        self.listWidget.setGeometry(QtCore.QRect(20, 20, 256, 521))
        self.listWidget.setObjectName("listWidget")
        self.addTimeBtn = QtGui.QPushButton(self.TimeGroupBox)
        self.addTimeBtn.setGeometry(QtCore.QRect(80, 550, 145, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(50)
        font.setBold(False)
        self.addTimeBtn.setFont(font)
        self.addTimeBtn.setObjectName("addTimeBtn")
        self.horizontalLayout.addWidget(self.TimeGroupBox)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 4)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "The Current Sgtk Environment", None, QtGui.QApplication.UnicodeUTF8))
        self.CIBtn.setText(QtGui.QApplication.translate("Dialog", "Check In", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser.setHtml(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.COBtn.setText(QtGui.QApplication.translate("Dialog", "Check Out", None, QtGui.QApplication.UnicodeUTF8))
        self.TimeGroupBox.setTitle(QtGui.QApplication.translate("Dialog", "Your Time", None, QtGui.QApplication.UnicodeUTF8))
        self.addTimeBtn.setText(QtGui.QApplication.translate("Dialog", "Add Time", None, QtGui.QApplication.UnicodeUTF8))

from . import resources_rc
