from PyQt4.Qt import QFileDialog, QMainWindow
import os
from PyQt4.QtGui import QApplication
from gui.templates.mainWindow import Ui_MainWindow

class MainWindow(Ui_MainWindow, QMainWindow):
    
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        
        self.setupUi(self)
    
    def onCloseAccept(self):
        pass
    
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
        
    def startRdClicked(self):
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
