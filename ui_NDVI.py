
from PyQt4 import QtCore, QtGui
import qgis.core

try:
	_fromUtf8 = QtCore.QtString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s
# A pre-programmed Qt package. Reference to Qt.


try:
	_encoding = QtGui.QApplication.UnicodeUTF8
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig, _encoding)		
except AttributeError:
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig)

class Ui_NDVI(object):
	def setupUi(self, NDVI):
		NDVI.setObjectName(_fromUtf8("NDVI"))

		NDVI.resize(400, 500)
		
		# We connect to the map canvas to get the Layer listing
		canvas = qgis.utils.iface.mapCanvas()
		allLayers = canvas.layers()
		
		# Button OK/Cancel
		self.buttonBox = QtGui.QDialogButtonBox(NDVI)
		self.buttonBox.setGeometry(QtCore.QRect(40, 455, 341, 32))
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
		
		# Header with plugin description
		self.Description = QtGui.QLabel(NDVI)
		self.Description.setGeometry(QtCore.QRect(10, 10, 371, 41))
		self.Description.setAcceptDrops(False)
		self.Description.setFrameShape(QtGui.QFrame.NoFrame)
		self.Description.setTextFormat(QtCore.Qt.AutoText)
		self.Description.setScaledContents(False)
		self.Description.setWordWrap(True)
		self.Description.setObjectName(_fromUtf8("Description"))
		
		# Tag and combobox red
		self.lbl_raster_red = QtGui.QLabel(NDVI)
		self.lbl_raster_red.setGeometry(QtCore.QRect(10, 60, 371, 20))
		self.lbl_raster_red.setObjectName(_fromUtf8("lbl_raster_red"))
		self.cb_raster_red = QtGui.QComboBox(NDVI)
		self.cb_raster_red.setGeometry(QtCore.QRect(10, 80, 371, 22))
		self.cb_raster_red.setObjectName(_fromUtf8("cb_raster_red"))

		# Tag and combobox near_red
		self.lbl_raster_nir = QtGui.QLabel(NDVI)
		self.lbl_raster_nir.setGeometry(QtCore.QRect(10, 100, 371, 20))
		self.lbl_raster_nir.setObjectName(_fromUtf8("lbl_raster_nir"))
		self.cb_raster_nir = QtGui.QComboBox(NDVI)
		self.cb_raster_nir.setGeometry(QtCore.QRect(10, 120, 371, 22))
		self.cb_raster_nir.setObjectName(_fromUtf8("cb_raster_nir"))
		
		# NDVI output name
		self.lbl_name_ndvi = QtGui.QLabel(NDVI)
		self.lbl_name_ndvi.setGeometry(QtCore.QRect(10, 340, 371, 16))
		self.lbl_name_ndvi.setObjectName(_fromUtf8("lbl_name_ndvi"))
		self.ln_name_ndvi = QtGui.QLineEdit(NDVI)
		self.ln_name_ndvi.setGeometry(QtCore.QRect(10, 360, 300, 20))
		self.ln_name_ndvi.setObjectName(_fromUtf8("ln_name_ndvi"))
		self.pb_name_ndvi = QtGui.QPushButton(NDVI)
		self.pb_name_ndvi.setGeometry(QtCore.QRect(320, 358, 61, 24))
		self.pb_name_ndvi.setObjectName(_fromUtf8("pb_name_ndvi"))
		
		# MTL directory
		self.lbl_path_mtl = QtGui.QLabel(NDVI)
		# Setting a rectangle. What Lammert said. The numbers are sizes. For more info: https://srinikom.github.io/pyside-docs/PySide/QtCore/QRect.html
		self.lbl_path_mtl.setGeometry(QtCore.QRect(10, 395, 371, 16))
		# Set the object name.
		self.lbl_path_mtl.setObjectName(_fromUtf8("lbl_path_mtl"))
		# A line edit allows the user to enter and edit a single line of plain text.
		self.ln_path_mtl = QtGui.QLineEdit(NDVI)
		
		# Same methods are repeated for different properties of the MTL: its length and the Push Button
		self.ln_path_mtl.setGeometry(QtCore.QRect(10, 415, 300, 20))
		self.ln_path_mtl.setObjectName(_fromUtf8("ln_path_mtl"))
		self.pb_path_mtl = QtGui.QPushButton(NDVI)
		self.pb_path_mtl.setGeometry(QtCore.QRect(320, 413, 61, 24))
		self.pb_path_mtl.setObjectName(_fromUtf8("pb_path_mtl"))

		self.retranslateUi(NDVI)
                QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), NDVI.accept)
                QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), NDVI.reject)
                QtCore.QMetaObject.connectSlotsByName(NDVI)

	def retranslateUi(self, NDVI):
			NDVI.setWindowTitle(_translate("NDVI", "NDVI", None))
			self.Description.setText(_translate("NDVI", "Convert Landsat 8 images to NDVI GEoTIFF images", None))#"<DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\"\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
#"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
#"p, li { white-space: pre-wrap; }\n"
#"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
#"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Calculate the NBR from a Landsat 7 image with Digital Numbers values. 2 new images will be created with the radiance and reflectance values. Each output will have the same name along with the &quot;_RAD&quot; and &quot;_REF&quot; suffix respectively.</p></body></html>", None))
			self.lbl_raster_red.setText(_translate("NDVI", "The red raster, necessary to obtain the NDVI", None))
			self.lbl_raster_nir.setText(_translate("NDVI", "The near - red raster, necessary to obtain the NDVI", None))
			self.lbl_name_ndvi.setText(_translate("NDVI", "Path and filename of the NDVI output", None))
			self.pb_name_ndvi.setText(_translate("NDVI", "Browse...", None))
			self.lbl_path_mtl.setText(_translate("NDVI", "Path and filename of the MTL text file with the metadata", None))
			self.pb_path_mtl.setText(_translate("NDVI", "Browse...", None))
			
                
