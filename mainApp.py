# -*- coding: utf-8 -*-
import sys
import threading
 
# QT IMPORTS
from PyQt4.QtGui import QApplication
import signal
from PyQt4.Qt import Qt, SIGNAL
from gui.mainWindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    win = MainWindow()
    win.show()
    
    app.connect(app, SIGNAL("aboutToQuit()"), win.onCloseAccept)
    signal.signal(signal.SIGINT, lambda *args, **kwargs: win.close())
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    
    app.exec_()