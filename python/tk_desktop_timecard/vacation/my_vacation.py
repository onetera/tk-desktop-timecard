import traceback
import datetime 

import sgtk
from sgtk.platform.qt import QtCore, QtGui
from ..ui.vacation import CalendarApp

import os
import sys

if sys.version_info.major == 2:
    import cPickle as pick
else:
    import pickle as pick

logger = sgtk.platform.get_logger(__name__)

PYSIDE_VER = repr(QtGui.QWidget)
if 'PySide2' in PYSIDE_VER:
    PYSIDE_VER = 2
else:
    PYSIDE_VER = 1


class MyVacation( CalendarApp ):
    '''
    '''
    def __init__(self, parent=None):
        CalendarApp.__init__(self, parent)
        self.parent = parent
        self.ok_btn.clicked.connect( self.register )

    def register( self ):
        sg = self.parent._app.context.tank.shotgun

        vacation_type = 'Dayoff' if self.day_rd.isChecked() else 'H_Dayoff'
        sel_dates     = self.calendar.get_selected_dates()

        #project = self.parent._app.context.project
        
        project = sg.find_one( 'Project', [['name' , 'is' , '_Timelog']] , [] )

        user = self.parent._app.context.user
        
        mana = sg.find_one( 
                    'CustomNonProjectEntity04', 
                    [['code','is',vacation_type]], 
                    ['code'] 
                    )

        desc = 'Half off' if vacation_type == 'H_Dayoff' else 'Dayoff'

        for sel_date in sel_dates:
            vacation_date = datetime.date( sel_date.year(), sel_date.month() , sel_date.day() )

            data = {
                'user':user, 'entity' : mana , 'date' : vacation_date , 'description' : desc, 'project' : project
                }
            result = sg.create( 
                'TimeLog', data    
                )
            print( result )

        notice = QtGui.QMessageBox.information( 
                            self, 'Registered' , 
                            desc + ' was registered.',
                            QtGui.QMessageBox.Yes 
        )

        self.parent.parent.my_timelog_table._model._refresh_data()
        self.close()



