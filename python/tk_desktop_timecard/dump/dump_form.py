# -*- coding: utf-8 -*-

import os
from math import ceil
from datetime import datetime, timedelta
import sgtk
from sgtk.platform.qt import QtGui, QtCore
from .dump_model import DumpTableModel
from .dump_delegate import ComboBoxDelegate, CalendarDelegate
from .dump_constant import *
from ..ui.dump import Ui_DumpDialog
from .excel import ExcelLoad

logger = sgtk.platform.get_logger(__name__)


class DumpForm(QtGui.QDialog):

    def __init__(self, project_name, parent=None):
        super(DumpForm, self).__init__(parent)

        self._app = sgtk.platform.current_bundle()
        self._sg = self._app.context.tank.shotgun

        today = datetime.now()
        self.tomorrow = today + timedelta(days=1)
        self.tomorrow = self.tomorrow.strftime("%Y-%m-%dT%H:%M:%SZ")

        self._ui = Ui_DumpDialog()
        self._ui.setupUi(self)

        self.project_name = project_name

        self._ui.upload.setEnabled(False)
        self._ui.add_btn.setEnabled(False)
        self._ui.del_btn.setEnabled(False)
        self._ui.task_check.setEnabled(False)

        self.load_flag = False

        self._ui.select_dir.clicked.connect(self._set_path)
        self._ui.load_excel.clicked.connect(self._load_excel)
        self._ui.check_all_btn.clicked.connect(self._check_all)
        self._ui.uncheck_all_btn.clicked.connect(self._uncheck_all)
        self._ui.add_btn.clicked.connect(self._add_log)
        self._ui.del_btn.clicked.connect(self._del_log)
        self._ui.task_check.clicked.connect(self._task_check)
        self._ui.upload.clicked.connect(self._upload)


    def _set_path(self):
        self._ui.add_btn.setEnabled(False)
        self._ui.del_btn.setEnabled(False)
        self._ui.task_check.setEnabled(False)
        self._ui.upload.setEnabled(False)

        home_path = os.path.expanduser('~')
        filename, _ = QtGui.QFileDialog().getOpenFileName(None,
                                                               'Import ExcelFile directory',
                                                               home_path,
                                                               filter="Excel Files (*.xlsx *.xls)")
        if os.path.splitext(filename)[-1] == '.xls':
            os.rename(filename,
                      os.path.splitext(filename)[0] + '.xlsx')
            
            filename = os.path.splitext(filename)[0] + '.xlsx'
        self._ui.lineEdit.setText(filename)
    

    def _load_excel(self):
        path = self._ui.lineEdit.text()
        if path:
            excel_load = ExcelLoad(path)
            self._model = DumpTableModel(self.project_name, excel_load.row_infos)

            self._ui.seq_model_view.setModel(None)

            if excel_load.confirm_sync:
                self._ui.seq_model_view.setModel(self._model)
            self._ui.seq_model_view.horizontalHeader().setStretchLastSection(True)

            self._ui.add_btn.setEnabled(True)
            self._ui.del_btn.setEnabled(True)
            self._ui.task_check.setEnabled(True)

            combo_delegate = ComboBoxDelegate(self)
            self._ui.seq_model_view.setItemDelegateForColumn(2, combo_delegate)

            calen_delegate = CalendarDelegate(self)
            self._ui.seq_model_view.setItemDelegateForColumn(4, calen_delegate)
        else:
            return QtGui.QMessageBox.critical(self, "Error", "Please select an '.xlsx' or '.xls' file.")


    def _check_all(self):
        for row in range(0, self._model.rowCount(None)):
                index = self._model.createIndex(row, 0)
                self._model.setData(index, QtCore.Qt.Checked, QtCore.Qt.CheckStateRole)


    def _uncheck_all(self):
        for row in range(0, self._model.rowCount(None)):
                index = self._model.createIndex(row, 0)
                self._model.setData(index, QtCore.Qt.Unchecked, QtCore.Qt.CheckStateRole)


    def _add_log(self):
        self._model.add_Item()
        self._ui.del_btn.setEnabled(True)
        self._ui.upload.setEnabled(False)


    def _del_log(self):
        self._model.del_Item()


    def _task_check(self):
        checked_rows = self._model.get_checked_rows()
        self.result_list = []

        project = str(self._model.data(self._model.index(0, 6), QtCore.Qt.DisplayRole))
        project_id = self._sg.find_one("Project", [['name', 'is', project]])
        
        if project == "_Timelog":
            for row in checked_rows:
                if project != str(self._model.data(self._model.index(row, 6), QtCore.Qt.DisplayRole)):
                    return QtGui.QMessageBox.critical(self, "Error", "The row '{0}' is not '{1}'".format(row+1, project))
                
                user = str(self._model.data(self._model.index(row, 1), QtCore.Qt.DisplayRole))
                user_id = self._sg.find_one("HumanUser",[['name', 'is', user]])
                task = str(self._model.data(self._model.index(row, 2), QtCore.Qt.DisplayRole))
                if task.lower() in ["work", "management"]:
                    task_id = self._sg.find_one("CustomNonProjectEntity04", [['code', 'is', task]])
                    date = str(self._model.data(self._model.index(row, 4), QtCore.Qt.DisplayRole))
                    hour = str(self._model.data(self._model.index(row, 5), QtCore.Qt.DisplayRole))
                    duration = float(hour.split(" ")[0]) * 60
                    description = str(self._model.data(self._model.index(row, 7), QtCore.Qt.DisplayRole))
                    if description == 'None':
                        description = ''

                    result = {
                            MODEL_KEYS["project"]: project_id,
                            MODEL_KEYS["user"]: user_id,
                            MODEL_KEYS["task"]: task_id,
                            MODEL_KEYS["date"]: date,
                            MODEL_KEYS["hour"]: duration,
                            MODEL_KEYS["description"]: description,
                            "sg_update_type": "User"
                            }
                                
                    self.result_list.append(result)
                else:
                    return QtGui.QMessageBox.critical(self, "Error", "Only 'Work' and 'Management' are allowed.")

        else:
            for row in checked_rows:
                if project != str(self._model.data(self._model.index(row, 6), QtCore.Qt.DisplayRole)):
                    return QtGui.QMessageBox.critical(self, "Error", "The row '{0}' is not '{1}'".format(row+1, project))
                
                shot = str(self._model.data(self._model.index(row, 3), QtCore.Qt.DisplayRole))
                user = str(self._model.data(self._model.index(row, 1), QtCore.Qt.DisplayRole))
                user_id = self._sg.find_one("HumanUser",[['name', 'is', user]])
                if shot == 'None':
                    task = str(self._model.data(self._model.index(row, 2), QtCore.Qt.DisplayRole))
                    if task.lower() in ["work", "management"]:                    
                        task_id = self._sg.find_one("CustomNonProjectEntity04", [['code', 'is', task]])
                        date = str(self._model.data(self._model.index(row, 4), QtCore.Qt.DisplayRole))
                        hour = str(self._model.data(self._model.index(row, 5), QtCore.Qt.DisplayRole))
                        duration = float(hour.split(" ")[0]) * 60
                        description = str(self._model.data(self._model.index(row, 7), QtCore.Qt.DisplayRole))
                        if description == 'None':
                            description = ''

                        result = {
                                MODEL_KEYS["project"]: project_id,
                                MODEL_KEYS["user"]: user_id,
                                MODEL_KEYS["task"]: task_id,
                                MODEL_KEYS["date"]: date,
                                MODEL_KEYS["hour"]: duration,
                                MODEL_KEYS["description"]: description,
                                "sg_update_type": "User"
                                }
                        
                        self.result_list.append(result)

                    else:
                        return QtGui.QMessageBox.critical(self, "Error", "Only 'Work' and 'Management' are allowed.")

                else: 
                    shot_asset = str(self._model.data(self._model.index(row, 3), QtCore.Qt.DisplayRole))

                    for entity_type in ["Shot", "Asset"]:
                        shot_asset_id = self._sg.find_one(entity_type, [['project', 'is', project_id], ['code', 'is', shot_asset]])
                        if shot_asset_id:
                            break

                    if not shot_asset_id:
                        return QtGui.QMessageBox.critical(self, "Error", "'{}' is not an existing Shot/Asset.".format(shot_asset))
                    else:
                        task = str(self._model.data(self._model.index(row, 2), QtCore.Qt.DisplayRole))
                        task_id = self._sg.find_one("Task", [["entity", "is", shot_asset_id],["content", "is", task], 
                                                             ["task_assignees", "is", user_id]])

                        if not task_id:
                            return QtGui.QMessageBox.critical(self, "Error", "'{0}' has not been assigned to the '{1}' task.".format(user, task))
                        else:
                            date = str(self._model.data(self._model.index(row, 4), QtCore.Qt.DisplayRole))
                            hour = str(self._model.data(self._model.index(row, 5), QtCore.Qt.DisplayRole))
                            duration = float(hour.split(" ")[0]) * 60
                            description = str(self._model.data(self._model.index(row, 7), QtCore.Qt.DisplayRole))
                            if description == 'None':
                                description = ''

                            result = {
                                    MODEL_KEYS["project"]: project_id,
                                    MODEL_KEYS["user"]: user_id,
                                    MODEL_KEYS["task"]: task_id,
                                    MODEL_KEYS["date"]: date,
                                    MODEL_KEYS["hour"]: duration,
                                    MODEL_KEYS["description"]: description,
                                    "sg_update_type": "User"
                                    }
                            
                            self.result_list.append(result)

            QtGui.QMessageBox.information(self, "Info", "Check Clear. You can UPLOAD timelog")
            self._ui.upload.setEnabled(True)
            # self._ui.task_check.setEnabled(False)

            logger.debug("check result: {}".format(self.result_list))


    def _upload(self):
        error = 0
        for ressult in self.result_list:
            try:
                exist_log = self._sg.find_one("TimeLog", 
                                              [
                                                ['created_at', 'less_than', self.tomorrow],
                                                ["project", "is", ressult["project"]],
                                                ["entity", "is", ressult["entity"]],
                                                ["user", "is", ressult["user"]],
                                                ["date", "is", ressult["date"]],
                                                ["duration", "is", ressult["duration"]],
                                                ["description", "is", ressult["description"]]
                                              ])
                logger.debug("exist log result : {}".format(exist_log))

                if exist_log is None:
                    upload = self._sg.create("TimeLog", ressult)

                    logger.debug("create result : {}".format(upload))
            except Exception as e:
                logger.error(e)
                error += 1

        if error == 0:
            QtGui.QMessageBox.information(self, "Info", "Upload Complete")
            self._ui.upload.setEnabled(False)
            self.result_list = []
        else:
            QtGui.QMessageBox.warning(self, "Warning", "Upload Error : Try again")


    def closeEvent(self, event):
        self._ui.seq_model_view.setModel(None)
        self.deleteLater()
        event.accept()
        logger.debug("CloseEvent Received. Begin shutting down UI.")