# -*- coding: utf-8 -*-

import sys

from sgtk.platform.qt import QtCore, QtGui
from .dump_constant import *

class DumpTableModel(QtCore.QAbstractTableModel):
    def __init__(self, project_name, excel_array, parent=None, *args):

        QtCore.QAbstractTableModel.__init__(self, parent, *args)
        self.header = list(MODEL_KEYS.keys())
        # self.header = MODEL_KEYS.keys()
        self.project_name = project_name
        self.arraydata = excel_array


    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.arraydata)


    def columnCount(self, parent=QtCore.QModelIndex()):
        return len(self.header)


    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.DisplayRole:
            return None

        if orientation == QtCore.Qt.Horizontal:
            return self.header[section]
        return None


    def data(self, index, role):
        if not index.isValid():
            return None
        
        if role == QtCore.Qt.DisplayRole:
            if index.column() == 0:
                return None
            elif index.column() == 4:
                return self.arraydata[index.row()][index.column()]
            elif index.column() == 5:
                value = self.arraydata[index.row()][index.column()]
                if sys.version_info.major == 2 and value is not None:
                    value = float(value)
                try:
                    if value is None:
                        return "0 hrs"
                    if '.0' in str(value):
                        return "{} hrs".format(int(value))
                    else:
                        return "{} hrs".format(value)
                    
                except ValueError:
                    return "0 hrs"
            else:
                return self.arraydata[index.row()][index.column()]
        elif role == QtCore.Qt.EditRole:
            return self.arraydata[index.row()][index.column()]
        elif role == QtCore.Qt.CheckStateRole and index.column() == 0:
            checkbox = self.arraydata[index.row()][index.column()]
            if isinstance(checkbox, QtGui.QCheckBox):
                return QtCore.Qt.Checked if checkbox.isChecked() else QtCore.Qt.Unchecked
        return None


    def flags(self, index):
        if index.column() == 0:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsUserCheckable
        if index.column() == 6:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable
        else:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable


    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if not index.isValid():
            return False
        
        if role == QtCore.Qt.CheckStateRole and index.column() == 0:
            checkbox = self.arraydata[index.row()][index.column()]
            if isinstance(checkbox, QtGui.QCheckBox):
                checkbox.setChecked(value == QtCore.Qt.Checked)
                self.dataChanged.emit(index, index)
                return True
        elif role == QtCore.Qt.EditRole and index.column() == 4:
            self.arraydata[index.row()][index.column()] = value
            self.dataChanged.emit(index, index)
            return True
        else:
            self.arraydata[index.row()][index.column()] = value
            self.dataChanged.emit(index, index)
            return True
        return False


    def add_Item(self):
        self.beginInsertRows(QtCore.QModelIndex(), self.rowCount(), self.rowCount())
        self.arraydata.append([QtGui.QCheckBox(), '', '', '', QtCore.QDate(2024, 4, 30).toString("yyyy-MM-dd"), '0', self.project_name, ''])
        self.endInsertRows()


    def del_Item(self):
        for row in reversed(range(len(self.arraydata))):
            if self.arraydata[row][0].isChecked():
                self.beginRemoveRows(QtCore.QModelIndex(), row, row)
                self.arraydata.pop(row)
                self.endRemoveRows()

    
    def get_checked_rows(self):
        checked_rows = []
        for row in range(self.rowCount()):
            if self.arraydata[row][0].isChecked():
                checked_rows.append(row)
        return checked_rows

