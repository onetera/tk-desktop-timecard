# -*- coding: utf-8 -*-

from sgtk.platform.qt import QtCore, QtGui
from .dump_constant import *

class DumpTableModel(QtCore.QAbstractTableModel):
    def __init__(self, project_name, parent=None, *args):

        QtCore.QAbstractTableModel.__init__(self, parent, *args)
        self.header = list(MODEL_KEYS.keys())
        # self.header = MODEL_KEYS.keys()
        self.project_name = project_name
        if self.project_name != "_Timelog":
            self.arraydata = [[False, self.project_name, '', 'Work', QtCore.QDate.currentDate().toString("yyyy-MM-dd"), '0', '']]
        else:
            self.arraydata = [[False, self.project_name, '', 'Management', QtCore.QDate.currentDate().toString("yyyy-MM-dd"), '0', '']]

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
                try:
                    if '.' in value:
                        return "{} hrs".format(value)
                    elif isinstance(int(value), int):
                        if int(value) == 1:
                            return "1 hr" 
                        elif int(value) <= 16:
                            return "{} hrs".format(value)
                        else:
                            return "0 hrs"
                except ValueError:
                    return "0 hrs"
            else:
                return self.arraydata[index.row()][index.column()]
        elif role == QtCore.Qt.EditRole:
            return self.arraydata[index.row()][index.column()]
        elif role == QtCore.Qt.CheckStateRole and index.column() == 0:
            return QtCore.Qt.Checked if self.arraydata[index.row()][index.column()] else QtCore.Qt.Unchecked
        return None

    def flags(self, index):
        if index.column() == 0:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsUserCheckable
        if index.column() == 1:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable
        else:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if not index.isValid():
            return False
        
        if role == QtCore.Qt.CheckStateRole and index.column() == 0:
            self.arraydata[index.row()][index.column()] = value
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
        if self.project_name != "_Timelog":
            self.beginInsertRows(QtCore.QModelIndex(), self.rowCount(), self.rowCount())
            self.arraydata.append([False, self.project_name, '', 'Work', QtCore.QDate.currentDate().toString("yyyy-MM-dd"), '0', ''])
            self.endInsertRows()
        else:
            self.beginInsertRows(QtCore.QModelIndex(), self.rowCount(), self.rowCount())
            self.arraydata.append([False, self.project_name, '', 'Management', QtCore.QDate.currentDate().toString("yyyy-MM-dd"), '0', ''])
            self.endInsertRows()

    def del_Item(self):
        for row in reversed(range(len(self.arraydata))):
            if self.arraydata[row][0] == QtCore.Qt.Checked:
                self.beginRemoveRows(QtCore.QModelIndex(), row, row)
                self.arraydata.pop(row)
                self.endRemoveRows()
    
    def get_checked_rows(self):
        checked_rows = []
        for row in range(self.rowCount()):
            if self.arraydata[row][0]:
                checked_rows.append(row)
        return checked_rows


