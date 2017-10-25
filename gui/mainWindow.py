from __future__ import print_function, division

from PyQt4.Qt import QFileDialog, QMainWindow, pyqtSignal, pyqtSlot
import os
from PyQt4.QtGui import QApplication
from gui.templates.mainWindow import Ui_MainWindow
import pyqtgraph as pg
from PIL import Image
import numpy as np

class MainWindow(Ui_MainWindow, QMainWindow):
    
    refreshFrame = pyqtSignal(np.ndarray)
    
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        img = Image.open("./lena_std.tif")
        img.load()
        self.frameData = np.asarray( img.convert('L'), dtype="int32" )
        self.setupUi(self)
        
        # This is call to update new frame
        self.refreshFrame.emit(self.frameData)
    
    def setupUi(self, MainWindow):
        Ui_MainWindow.setupUi(self, MainWindow)
        
        self.cameraView = pg.ImageView()
        self.cameraView.ui.roiBtn.hide()
        self.cameraView.ui.menuBtn.hide()
        self.cameraViewFrame.layout().addWidget(self.cameraView)
        
        self.graphDialog = pg.PlotWidget(title="My nice title")
        self.graphDialog.setLabel("bottom", "Point")
        self.graphDialog.showGrid(x=True, y=True, alpha=0.1)
        
        self.graphViewFrame.layout().addWidget(self.graphDialog)
        
        # Connecting pyqtSignal to it's pyqtSlot
        self.refreshFrame.connect(self.frameUpdate)
        
    def onCloseAccept(self):
        pass
    
    @pyqtSlot(np.ndarray)
    def frameUpdate(self, frameData):
        self.frameData = frameData
        self.cameraView.setImage(self.frameData)       
    
    def resetRoi(self):
        print("reset ROI button clicked")
    
    def setRoi(self):
        roiX, roiY = self.roiXInput.value(), self.roiYInput.value()
        roiXOffset, roiYOffset = self.roiXOffsetInput.value(), self.roiYOffsetInput.value()
        
        print("Roi X,Y: %i, %i" % (roiX, roiY))
        print("Roi offset X,Y: %i, %i" % (roiXOffset, roiYOffset))
    
    def clearModeChanged(self, clearMode):
        print("Clear mode changed", clearMode)
        
    def triggerModeChanged(self, triggerMode):
        print("Trigger mode changed", triggerMode)
        
    def readoutRateChanged(self, readoutRate):
        print("Readout rate changed", readoutRate)
        
    def exposureTimeChanged(self, exposureTime):
        print("Exposure time changed: ", exposureTime)
        
    def liveModeClicked(self):
        print("Live mode button clicked")
    
    def snapClicked(self):
        saveFilePath = QFileDialog.getSaveFileName(self, 'Set save file')
        if saveFilePath == "": 
            return
        
        print("Snap button clicked, save it in the file %s" % saveFilePath)
        
    def start(self):
        print("Start rd clicked")
        
    def refreshClicked(self):
        print("Refresh clicked")
    
    def cameraRecordClicked(self):
        saveFilePath = QFileDialog.getSaveFileName(self, 'Set save file')
        if saveFilePath == "": 
            return
        
        numOfFrames = self.cameraFramesInput.value()
        print("Record %i frames" % numOfFrames)
    
    def bgSubstracionClicked(self):
        numOfFrames = self.bgSubstracionFramesInput.value()
        print("Substract %i frames" % numOfFrames)
    
    def graphSaveClicked(self):
        saveFilePath = QFileDialog.getSaveFileName(self, 'Set save file')
        if saveFilePath == "": 
            return
        
        saveImages = self.saveImagesCheckbox.isChecked()
        print("Save graph clicked, save images: %i" % saveImages)
        
    def recordGraphClicked(self):
        saveFilePath = QFileDialog.getSaveFileName(self, 'Set save file')
        if saveFilePath == "": 
            return
        
        numOfFrames = self.graphFramesRecordInput.value()
        saveImages = self.saveImagesCheckbox.isChecked()
        print("Record %i graph frames, save images: %i" % (numOfFrames, saveImages))
