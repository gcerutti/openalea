# -*- python -*-
#
#       spatial_image.visu : spatial nd images
#
#       Copyright 2006 INRIA - CIRAD - INRA  
#
#       File author(s): Jerome Chopard <jerome.chopard@sophia.inria.fr>
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
# 
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#
"""
This module provide a simple viewer to display 3D stacks
"""

__license__= "Cecill-C"
__revision__=" $Id: $ "

__all__ = ["display","SlideViewer"]

from ..spatial_image import SpatialImage

from PyQt4.QtCore import Qt,QObject,SIGNAL
from PyQt4.QtGui import (QApplication,QLabel,QMainWindow,QComboBox,
                        QSlider,QToolBar)
from palette import palette_names,palette_factory
from pixmap_view import PixmapStackView,ScalableLabel

from slide_viewer_ui import Ui_MainWindow

class SlideViewer (QMainWindow) :
	"""Display each image in a stack using a slider
	"""
	def __init__ (self, order='C') :
		QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.order=order
		#central label
		self._im_view = PixmapStackView(order=self.order)
		self._label = ScalableLabel()
		self.setCentralWidget(self._label)
		
		#mouse handling
		self._label.setMouseTracking(True)
		self._last_mouse_x = 0
		self._last_mouse_y = 0
		
		QObject.connect(self._label,
		                SIGNAL("mouse_press"),
		                self.mouse_pressed)
		
		QObject.connect(self._label,
		                SIGNAL("mouse_move"),
		                self.mouse_pressed)
		
		#toolbar
		QObject.connect(self.ui.action_close,
		                SIGNAL("triggered(bool)"),
		                self.close)
		
		QObject.connect(self.ui.action_snapshot,
		                SIGNAL("triggered(bool)"),
		                self.snapshot)
		
		QObject.connect(self.ui.action_rotate_left,
		                SIGNAL("triggered(bool)"),
		                self.rotate_left)
		
		QObject.connect(self.ui.action_rotate_right,
		                SIGNAL("triggered(bool)"),
		                self.rotate_right)
		
		#palette
		self._palette_select = QComboBox()
		self.ui.toolbar.addWidget(self._palette_select)
		for palname in palette_names :
			self._palette_select.addItem(palname)
		
		QObject.connect(self._palette_select,
		                SIGNAL("currentIndexChanged(int)"),
		                self.palette_name_changed)
		
		#slider
		self._bot_toolbar = QToolBar("slider")
		
		self._img_slider = QSlider(Qt.Horizontal)
		self._img_slider.setEnabled(False)
		QObject.connect(self._img_slider,
		                SIGNAL("valueChanged(int)"),
		                self.slice_changed)
		
		self._bot_toolbar.addWidget(self._img_slider)
		self.addToolBar(Qt.BottomToolBarArea,self._bot_toolbar)
		
		
		#statusbar
		self._lab_coord = QLabel("coords:")
		self._lab_xcoord = QLabel("% 4d" % 0)
		self._lab_ycoord = QLabel("% 4d" % 0)
		self._lab_zcoord = QLabel("% 4d" % 0)
		self._lab_intens = QLabel("intens: None")
		
		self.ui.statusbar.addPermanentWidget(self._lab_coord)
		self.ui.statusbar.addPermanentWidget(self._lab_xcoord)
		self.ui.statusbar.addPermanentWidget(self._lab_ycoord)
		self.ui.statusbar.addPermanentWidget(self._lab_zcoord)
		self.ui.statusbar.addPermanentWidget(self._lab_intens)
	
	##############################################
	#
	#		update GUI
	#
	##############################################
	def update_pix (self) :
		pix = self._im_view.pixmap()
		if pix is not None :
			self._label.setPixmap(pix)
	
	def fill_infos (self) :
		x,y = self._label.pixmap_coordinates(self._last_mouse_x,
		                                     self._last_mouse_y)
		
		img = self._im_view.image()
		if img is not None :
			i,j,k = self._im_view.data_coordinates(x,y)
			self._lab_xcoord.setText("% 4d" % i)
			self._lab_ycoord.setText("% 4d" % j)
			self._lab_zcoord.setText("% 4d" % k)
			
			imax,jmax,kmax = img.shape
			if 0 <= i < imax and 0 <= j < jmax and 0 <= k < kmax :
				self._lab_intens.setText("intens: % 3d" % img[i,j,k])
			else :
				self._lab_intens.setText("intens: None")
	
	##############################################
	#
	#		accessors
	#
	##############################################
	def set_image (self, img) :
		self._im_view.set_image(img)
		
		try :
			res = img.resolution[:2]
			self._label.set_resolution(*res)
		except AttributeError :
			pass
		
		self._img_slider.setRange(0,self._im_view.nb_slices() - 1)
		self._img_slider.setEnabled(True)
		self.slice_changed(self._img_slider.value() )
	
	def set_palette (self, palette, palette_name = None) :
		if palette_name is not None :
			ind = self._palette_select.findText(palette_name)
			self._palette_select.setCurrentIndex(ind)
		
		self._im_view.set_palette(palette)
		self.update_pix()
	
	##############################################
	#
	#		slots
	#
	##############################################
	def palette_name_changed (self, palette_index) :
		palname = str(self._palette_select.currentText() )
		img = self._im_view.image()
		if img is not None :
			self.set_palette(palette_factory(str(palname),img.max() ) )
	
	def slice_changed (self, ind) :
		self._im_view.set_current_slice(ind)
		self.update_pix()
		self.fill_infos()
	
	def snapshot (self) :
		"""write the current image
		"""
		pix = self._im_view.pixmap()
		if pix is not None :
			pix.save("slice%.4d.png" % self._img_slider.value() )
	
	def wheelEvent (self, event) :
		inc = event.delta() / 8 / 15
		self._img_slider.setValue(self._img_slider.value() + inc)
	
	def rotate_left (self) :
		self._im_view.rotate(-1)
		self.update_pix()
	
	def rotate_right (self) :
		self._im_view.rotate(1)
		self.update_pix()
	
	def mouse_pressed (self, event) :
		self._last_mouse_x = event.x()
		self._last_mouse_y = event.y()
		self.fill_infos()

def display (image, palette_name = "grayscale", color_index_max = None,order="C") :
    """
    """	
    w = SlideViewer(order)
		
    if not isinstance(image,SpatialImage):
        image = SpatialImage(image)

    if color_index_max is None :
	cmax = image.max()
    else :
	cmax = color_index_max
		
    palette = palette_factory(palette_name,cmax)
		
    w.set_palette(palette,palette_name)
    w.set_image(image)
		
    w.show()
    return w