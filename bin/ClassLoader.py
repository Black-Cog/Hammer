
import sys, os
sys.path.append( '/'.join( os.path.dirname(__file__).split('\\')[:-2] ) )
from PySide import QtCore, QtGui
import Anvil.core
import Hammer.ui


class ClassLoader():
	"""docstring for ClassLoader"""
	def __init__(self):
		Awindow = Anvil.core.Window
		Alayout = Anvil.core.Layout
		Abutton = Anvil.core.Button

		self.hammerLog = Hammer.ui.Login().create()

	def create(self):
		return self.hammerLog

app = QtGui.QApplication(sys.argv)
test = ClassLoader()
sys.exit( test.create().exec_() )
