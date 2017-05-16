from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.utils import iface
from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry
from qgis.core import *
from qgis.gui import *
from NDVIdialog import NDVIDialog
import os

class NDVI:
    def __init__(self, iface):
	# Save reference to the interface OK
	self.iface = iface
	# initialize plugin  OK
	# Watch __file__: that is a property of a pre-
	# specified thing that can be received through the
	# dir command
	self.plugin_dir = os.path.dirname(__file__)	
	# Saving the file name in GeoTIFF format.

        #mapcanvas = iface.mapCanvas() 

        #layers = mapcanvas.layers()

        #self.NDVI_calc(layers)

        self.dlg = NDVIDialog()


        #Connect browse buttons
	QObject.connect(self.dlg.ui.pb_name_ndvi, SIGNAL("clicked()"), self.select_ndvi)
	QObject.connect(self.dlg.ui.pb_path_mtl, SIGNAL("clicked()"), self.select_mtl)

    def select_mtl(self):
		archivo_mtl = QFileDialog.getOpenFileName(None, "Select MTL file", "", "MTL text File (*.txt)")
		if archivo_mtl != None: self.dlg.ui.ln_path_mtl.setText(archivo_mtl)
		
    def select_ndvi(self):
		archivo_ndvi = QFileDialog.getSaveFileName(None, "Save output GeoTIFF file", "", "GeoTIFF (*.tif)")
		if archivo_ndvi != None: self.dlg.ui.ln_name_ndvi.setText(archivo_ndvi)
                
    def initGui(self):
		# Create action that will start plugin configuration
		self.action = QAction(QIcon("C:/Users/fumibol/.qgis2/python/plugins/NDVI/icon.png"),u"NDVI", self.iface.mainWindow())
		# connect the action to the run method
		self.action.triggered.connect(self.run)

		# Add toolbar button and menu item
		self.iface.addToolBarIcon(self.action)
		self.iface.addPluginToMenu(u"NDVI", self.action)

    def unload(self):
                # Remove the plugin menu item and icon
                self.iface.removePluginMenu(u"&Digital Number 2 NDVI", self.action)
		self.iface.removeToolBarIcon(self.action)




    def NDVI_calc(self , layers):

        entries = []
        
        for l in layers:
            layer = QgsRasterCalculatorEntry()
            layer = QgsRasterCalculatorEntry()
            layer.ref = l.name() +'@1'
            layer.raster = l
            layer.bandNumber = 1
            entries.append(layer)
            
# Original path: C:/Users/fumibol/Documents/Wetlands/Python/QGIS arcPython/NDVI plugin/Output/NDVI.tif

#        for entry in entries:

        raster_salida = ""
# First it was raster_salida = ruta + os.path.sep + raster_salida + '.tif'
        raster_salida = unicode(self.dlg.ui.ln_name_ndvi.text())
            
        expression = '(' + entries[1].ref + ' + ' + entries[0].ref + ')/(' + entries[1].ref + ' - ' + entries[0].ref + '+ 1)'
        calc = QgsRasterCalculator(expression, raster_salida, 'GTiff', layers[0].extent(), layers[0].width(), layers[0].height(), entries)

        calc.processCalculation()
        
#        QgsMapLayerRegistry.instance().addMapLayer('C:/Users/fumibol/Documents/Wetlands/Python/QGIS arcPython/NDVI plugin/Output/NDVI.tif' , 'NDVI result')

        rl = self.iface.addRasterLayer(raster_salida , 'NDVI result')
			
        QMessageBox.information(self.iface.mainWindow(),"Success!" , "Raster image " + entries[0].ref + " created successfully ")

    def run(self):
		# We connect to the map canvas to obtain the list of layers. Capa means layer
		# Hier zijn er layers! Insertie van data gebeurt hier... maar ik kan er niet bij.
		canvas = self.iface.mapCanvas()
                allLayers = canvas.layers()
		# It connects to the map canvas to determine the selectable options.
				
		self.dlg.ui.cb_raster_red.clear()
		self.dlg.ui.cb_raster_nir.clear()
		
		for i in allLayers:
			self.dlg.ui.cb_raster_red.addItem(i.name())
			self.dlg.ui.cb_raster_nir.addItem(i.name())
##		# show the dialog
		self.dlg.show()
##		# Run the dialog event loop
		result = self.dlg.exec_()
##		# See if OK was pressed
		if result == 1:
                    self.NDVI_calc(allLayers)
##			# We get the values of the dialog for processing
##			raster_red = layer_search(unicode(self.dlg.ui.cb_raster_red.currentText()))
##			raster_nir = layer_search(unicode(self.dlg.ui.cb_raster_nir.currentText()))
##			nombre_NDVI = unicode(self.dlg.ui.ln_name_NDVI.text())
##
##									
##			# Prepare data for NBR. Create empty list to be filled by the NBR output.
##			er_NDVI = []			
##			
##			# then add more data/specifications to it.
##			raster_calc_red = QgsRasterCalculatorEntry()
##			raster_calc_red.ref = Redband.rasterRefNombre + '@1'
##
##			raster_calc_red.raster = Redband.rasterRef
##			raster_calc_red.bandNumber = 1
##
##			# Add the modified data to the output; the calculated NBR.
##			raster_NDVI.append(raster_calc_red)
##			
##			# Same for band 7
##			raster_calc_nir = RasterCalculatorEntry()
##			raster_calc_nir.ref = Nirband.rasterRefNombre + '@1'
##			raster_calc_nir.raster = Nirband.rasterRef
##			# rasterRef likely transforms the output into a raster.
##			raster_calc_nir.bandNumber = 1
##			raster_NDVI.append(raster_calc_nir)
##
##
##			# Load newly created layer.
##			infoRaster = QFileInfo(nombre_NDVI)
##			nombreBase = infoRaster.baseName()
##			rasterNDVI = QgsRasterLayer(nombre_NDVI, nombreBase)
##			
##			# And add it to the registry to be reflected in the list of layers
