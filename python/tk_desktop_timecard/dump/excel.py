# -*- coding: utf-8 -*-

import openpyxl

from sgtk.platform.qt import QtGui, QtCore


class ExcelLoad:
    def __init__(self, excel_file):
        self.row_infos = []
        self.excel_file = excel_file

        self.read_excel()

    def read_excel(self):
        wb = openpyxl.load_workbook(self.excel_file)
        sheet = wb.active

        for row in sheet.iter_rows(min_row=2, values_only=True):
            row_data = [cell for cell in row]
            if row_data[0]:
                check = True
            else:
                check = False
            row_data[0] = QtGui.QCheckBox()
            row_data[0].setChecked(check)

            self.row_infos.append(row_data)
        wb.close()