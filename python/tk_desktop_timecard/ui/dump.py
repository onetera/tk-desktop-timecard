# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dump_re.ui'
#
# Created: Fri May 17 11:53:59 2024
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

# from PyQt4 import QtCore, QtGui

# try:
#     _fromUtf8 = QtCore.QString.fromUtf8
# except AttributeError:
#     def _fromUtf8(s):
#         return s

# try:
#     _encoding = QtGui.QApplication.UnicodeUTF8
#     def _translate(context, text, disambig):
#         return QtGui.QApplication.translate(context, text, disambig, _encoding)
# except AttributeError:
#     def _translate(context, text, disambig):
#         return QtGui.QApplication.translate(context, text, disambig)

from sgtk.platform.qt import QtCore, QtGui

class Ui_DumpDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1044, 675)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.check_all_btn = QtGui.QPushButton(Dialog)
        self.check_all_btn.setObjectName("check_all_btn")
        self.horizontalLayout_3.addWidget(self.check_all_btn)
        self.uncheck_all_btn = QtGui.QPushButton(Dialog)
        self.uncheck_all_btn.setObjectName("uncheck_all_btn")
        self.horizontalLayout_3.addWidget(self.uncheck_all_btn)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.seq_model_view = QtGui.QTableView(Dialog)
        self.seq_model_view.setObjectName("seq_model_view")
        self.verticalLayout.addWidget(self.seq_model_view)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_5.setSpacing(0)
        # self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.add_btn = QtGui.QPushButton(self.groupBox_2)
        self.add_btn.setObjectName("add_btn")
        self.horizontalLayout_5.addWidget(self.add_btn)
        self.del_btn = QtGui.QPushButton(self.groupBox_2)
        self.del_btn.setObjectName("del_btn")
        self.horizontalLayout_5.addWidget(self.del_btn)
        self.horizontalLayout_4.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_6.setSpacing(0)
        # self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.task_check = QtGui.QPushButton(self.groupBox_3)
        self.task_check.setObjectName("task_check")
        self.horizontalLayout_6.addWidget(self.task_check)
        self.upload = QtGui.QPushButton(self.groupBox_3)
        self.upload.setObjectName("upload")
        self.horizontalLayout_6.addWidget(self.upload)
        self.horizontalLayout_4.addWidget(self.groupBox_3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Past Timelog", None, QtGui.QApplication.UnicodeUTF8))
        self.check_all_btn.setText(QtGui.QApplication.translate("Dialog", "Check All", None, QtGui.QApplication.UnicodeUTF8))
        self.uncheck_all_btn.setText(QtGui.QApplication.translate("Dialog", "Uncheck All", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Dialog", "Control", None, QtGui.QApplication.UnicodeUTF8))
        self.add_btn.setText(QtGui.QApplication.translate("Dialog", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.del_btn.setText(QtGui.QApplication.translate("Dialog", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Dialog", "Action", None, QtGui.QApplication.UnicodeUTF8))
        self.task_check.setText(QtGui.QApplication.translate("Dialog", "Task Check", None, QtGui.QApplication.UnicodeUTF8))
        self.upload.setText(QtGui.QApplication.translate("Dialog", "Upload", None, QtGui.QApplication.UnicodeUTF8))

from . import resources_rc
