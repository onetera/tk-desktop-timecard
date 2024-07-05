# -*- coding: utf-8 -*-

from sgtk.platform.qt import QtCore, QtGui
from .dump_constant import *

class ComboBoxDelegate(QtGui.QItemDelegate):
    def __init__(self, parent=None):
        super(ComboBoxDelegate, self).__init__(parent)

    def createEditor(self, parent, option=None, index=None):
        if index.data() in [u'Work', u'Management']:
            combo = QtGui.QComboBox(parent)
            combo.addItems(["Work", "Management"])
            return combo
        return super(ComboBoxDelegate, self).createEditor(parent, option, index)

    def setEditorData(self, editor, index):
        value = index.model().data(index, QtCore.Qt.EditRole)
        if isinstance(editor, QtGui.QComboBox):
            editor.setCurrentIndex(editor.findText(value))
        else:
            super(ComboBoxDelegate, self).setEditorData(editor, index)


    def setModelData(self, editor, model, index):
        if isinstance(editor, QtGui.QComboBox):
            model.setData(index, editor.currentText(), QtCore.Qt.EditRole)
        else:
            super(ComboBoxDelegate, self).setModelData(editor, model, index)

    def updateEditorGeometry(self, editor, option, index=None):
        editor.setGeometry(option.rect)


class CalendarDelegate(QtGui.QItemDelegate):
    def __init__(self, parent=None):
        super(CalendarDelegate, self).__init__(parent)

    def createEditor(self, parent, option=None, index=None):
        date_edit = QtGui.QDateEdit(parent)
        date_edit.setCalendarPopup(True)
        date_edit.setDisplayFormat("yyyy-MM-dd")

        # 날짜 범위 설정
        date_edit.setMinimumDate(QtCore.QDate(2024, 1, 1))
        date_edit.setMaximumDate(QtCore.QDate(2024, 4, 30))

        return date_edit

    def setEditorData(self, editor, index):
        value = index.model().data(index, QtCore.Qt.EditRole)
        editor.setDate(QtCore.QDate.fromString(value, "yyyy-MM-dd"))

    def setModelData(self, editor, model, index):
        date_value = editor.date().toString("yyyy-MM-dd")
        model.setData(index, date_value, QtCore.Qt.EditRole)

    def updateEditorGeometry(self, editor, option, index=None):
        editor.setGeometry(option.rect)