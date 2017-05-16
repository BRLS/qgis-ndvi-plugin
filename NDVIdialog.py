from PyQt4 import QtCore, QtGui
from ui_NDVI import Ui_NDVI

class NDVIDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
	# Set up the user interface from Designer.
	self.ui = Ui_NDVI()
	self.ui.setupUi(self)
