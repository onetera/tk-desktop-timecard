# -*- coding: utf-8 -*-

from math import ceil
# from datetime import timedelta
import sgtk
from sgtk.platform.qt import QtGui, QtCore
from .dump_model import DumpTableModel
from .dump_delegate import ComboBoxDelegate, CalendarDelegate
from .dump_constant import *
from ..ui.dump import Ui_DumpDialog

logger = sgtk.platform.get_logger(__name__)


class DumpForm(QtGui.QDialog):

    def __init__(self, project_name, parent=None):
        super(DumpForm, self).__init__(parent)

        self._app = sgtk.platform.current_bundle()

        self._ui = Ui_DumpDialog()
        self._ui.setupUi(self)

        self._model = DumpTableModel(project_name)
        self._ui.seq_model_view.setModel(self._model)
        self._ui.seq_model_view.horizontalHeader().setStretchLastSection(True)

        if project_name == '_Timelog':
            combo_delegate = ComboBoxDelegate(self)
            self._ui.seq_model_view.setItemDelegateForColumn(3, combo_delegate)
        calen_delegate = CalendarDelegate(self)
        self._ui.seq_model_view.setItemDelegateForColumn(4, calen_delegate)

        self._ui.upload.setEnabled(False)

        self._ui.check_all_btn.clicked.connect(self._check_all)
        self._ui.uncheck_all_btn.clicked.connect(self._uncheck_all)
        self._ui.add_btn.clicked.connect(self._add_log)
        self._ui.del_btn.clicked.connect(self._del_log)
        self._ui.task_check.clicked.connect(self._task_check)
        self._ui.upload.clicked.connect(self._upload)

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

    def _del_log(self):
        self._model.del_Item()

    def _task_check(self):
        checked_rows = self._model.get_checked_rows()
        sg = self._app.context.tank.shotgun
        err_msg = 0
        self.result_list = []

        project = str(self._model.data(self._model.index(0, 1), QtCore.Qt.DisplayRole))
        project_id = sg.find_one("Project", [['name', 'is', project]])
        
        if project == "_Timelog":
            for row in checked_rows:
                task = str(self._model.data(self._model.index(row, 3), QtCore.Qt.DisplayRole))
                task_id = sg.find_one("CustomNonProjectEntity04", [['code', 'is', task]])
                date = str(self._model.data(self._model.index(row, 4), QtCore.Qt.DisplayRole))
                hour = str(self._model.data(self._model.index(row, 5), QtCore.Qt.DisplayRole))
                duration = float(hour.split(" ")[0]) * 60
                description = str(self._model.data(self._model.index(row, 6), QtCore.Qt.DisplayRole))

                result = {MODEL_KEYS["project"]: project_id,
                        MODEL_KEYS["shot"]: task_id,
                        MODEL_KEYS["date"]: date,
                        MODEL_KEYS["hour"]: duration,
                        MODEL_KEYS["description"]: description,
                        "sg_update_type": "User"}
                            
                self.result_list.append(result)

        else:
            for row in checked_rows:
                shot = str(self._model.data(self._model.index(row, 2), QtCore.Qt.DisplayRole))
                if len(shot) == 0:
                    task = str(self._model.data(self._model.index(row, 3), QtCore.Qt.DisplayRole))
                    if task.lower() == "work":
                        task_id = sg.find_one("CustomNonProjectEntity04", [['code', 'is', task]])
                        date = str(self._model.data(self._model.index(row, 4), QtCore.Qt.DisplayRole))
                        hour = str(self._model.data(self._model.index(row, 5), QtCore.Qt.DisplayRole))
                        duration = float(hour.split(" ")[0]) * 60
                        description = str(self._model.data(self._model.index(row, 6), QtCore.Qt.DisplayRole))

                        result = {MODEL_KEYS["project"]: project_id,
                                MODEL_KEYS["shot"]: task_id,
                                MODEL_KEYS["date"]: date,
                                MODEL_KEYS["hour"]: duration,
                                MODEL_KEYS["description"]: description,
                                "sg_update_type": "User"}
                        
                        self.result_list.append(result)

                    else:
                        self._model.setData(self._model.index(row, 0), QtCore.Qt.Unchecked, QtCore.Qt.CheckStateRole)
                        err_msg += 1

                else: 
                    shot = str(self._model.data(self._model.index(row, 2), QtCore.Qt.DisplayRole))
                    shot_id = sg.find_one("Shot", [['project', 'is', project_id], ['code', 'is', shot]])
                    if not shot_id:
                        self._model.setData(self._model.index(row, 0), QtCore.Qt.Unchecked, QtCore.Qt.CheckStateRole)
                        err_msg += 1
                    else:
                        task = str(self._model.data(self._model.index(row, 3), QtCore.Qt.DisplayRole))
                        task_id = sg.find_one("Task", [["entity", "is", shot_id],["content", "is", task]])

                        if not task_id:
                            self._model.setData(self._model.index(row, 0), QtCore.Qt.Unchecked, QtCore.Qt.CheckStateRole)
                            err_msg += 1
                        else:
                            date = str(self._model.data(self._model.index(row, 4), QtCore.Qt.DisplayRole))
                            hour = str(self._model.data(self._model.index(row, 5), QtCore.Qt.DisplayRole))
                            duration = float(hour.split(" ")[0]) * 60
                            description = str(self._model.data(self._model.index(row, 6), QtCore.Qt.DisplayRole))

                            result = {MODEL_KEYS["project"]: project_id,
                                    MODEL_KEYS["task"]: task_id,
                                    MODEL_KEYS["date"]: date,
                                    MODEL_KEYS["hour"]: duration,
                                    MODEL_KEYS["description"]: description,
                                    "sg_update_type": "User"}
                            
                            self.result_list.append(result)

        if err_msg != 0:
            self.result_list = []
            QtGui.QMessageBox.warning(self, "Warning", "WRONG timelog change UNCHECKED")
        else:
            QtGui.QMessageBox.information(self, "Info", "Check Clear. You can UPLOAD timelog")
            self._ui.upload.setEnabled(True)
            # self._ui.task_check.setEnabled(False)

            logger.debug("check result: {}".format(self.result_list))
            
    def _upload(self):
        sg = self._app.context.tank.shotgun
        error = 0
        for ressult in self.result_list:
            try:
                upload = sg.create("TimeLog", ressult)

                logger.debug("create result : {}".format(upload))
            except Exception as e:
                logger.error(e)
                error += 1

        if error == 0:
            QtGui.QMessageBox.information(self, "Info", "Upload Complete")
            self._ui.upload.setEnabled(False)
            # self._ui.task_check.setEnabled(True)
            self.result_list = []
        else:
            QtGui.QMessageBox.warning(self, "Warning", "Upload Error : Try again")
    
    def closeEvent(self, event):
        self._ui.seq_model_view.setModel(None)
        self.deleteLater()
        event.accept()
        logger.debug("CloseEvent Received. Begin shutting down UI.")