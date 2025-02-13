# :coding: utf-8

#from tank.platform.qt.QtCore import *
#from tank.platform.qt.QtGui  import *

from sgtk.platform.qt import QtCore
from sgtk.platform.qt import QtGui  


import sys
#from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QCalendarWidget, QLabel
#from PyQt5.QtCore import QDate



class CalendarWidget( QtGui.QCalendarWidget ):
    def __init__(self, parent=None):
        super( CalendarWidget , self).__init__(parent)
        self.selected_dates = set()
        self.setGridVisible(True)
        self.clicked.connect(self.toggle_date_selection)

    def toggle_date_selection(self, date):
        if QtGui.QApplication.keyboardModifiers() == QtCore.Qt.ControlModifier:
            if date in self.selected_dates:
                self.selected_dates.remove(date)
            else:
                self.selected_dates.add(date)
        else:
            self.selected_dates = {date}
        print( self.selected_dates )
        self.updateCells()

    def paintCell(self, painter, rect, date):
        super( CalendarWidget , self ).paintCell(painter, rect, date)
        if date in self.selected_dates:
            painter.save()
            painter.setBrush( QtCore.Qt.blue )
            painter.setOpacity(0.5)
            painter.drawRect(rect)
            painter.restore()
            #painter.fillRect(rect, QtCore.Qt.blue )
            #painter.fillRect(rect, painter.brush())

    def get_selected_dates(self):
        return sorted(self.selected_dates)




class CalendarApp( QtGui.QDialog ):
    def __init__( self , parent = None ):
        QtGui.QDialog.__init__( self, parent )


        vlay = QtGui.QVBoxLayout()

        #self.calendar = QtGui.QCalendarWidget()
        self.calendar = CalendarWidget()
        self.calendar.setGridVisible(True)  # 격자 보이기 설정
        self.calendar.clicked.connect(self.show_date)

        self.day_rd  = QtGui.QRadioButton( 'Day off' )
        self.half_rd = QtGui.QRadioButton( 'Half off' )
        self.ok_btn  = QtGui.QPushButton( 'OK' )
        self.cancel_btn = QtGui.QPushButton( 'Cancel' )
        hlay = QtGui.QHBoxLayout()
        hlay.addWidget( self.day_rd )
        hlay.addWidget( self.half_rd )
        hlay.addWidget( self.ok_btn )
        hlay.addWidget( self.cancel_btn )

        self.label = QtGui.QLabel()
        self.label.setText(self.calendar.selectedDate().toString("yyyy-MM-dd"))

        vlay.addWidget(self.calendar)
        vlay.addWidget(self.label)
        vlay.addLayout( hlay )

        self.setLayout( vlay )
        self.setWindowTitle( 'Day off / Half off' )
        self.setGeometry(300, 300, 400, 300)

        self.day_rd.setChecked( True )
        self.cancel_btn.clicked.connect( self.close )

    def show_date(self, date):
        #self.label.setText(date.toString("yyyy-MM-dd"))

        selected_dates = self.calendar.get_selected_dates()
        if selected_dates:
            date_strings = [d.toString("yyyy-MM-dd") for d in selected_dates]
            self.label.setText(  u", ".join(date_strings))
        else:
            self.label.setText("선택된 날짜 없음")




#from . import resources_rc

#if __name__ == '__main__':
#    app = QtCore.QApplication(sys.argv)
#    ex = CalendarApp()
#    ex.show()
#    sys.exit(app.exec_())
