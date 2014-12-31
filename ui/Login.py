
import sys, os
sys.path.append( '/'.join( os.path.dirname(__file__).split('\\')[:-2] ) )
from PySide import QtCore, QtGui
import Anvil.core


class Login():
	"""docstring for Login"""
	def __init__(self):
		# defind class
		Awindow    = Anvil.core.Window
		Abutton    = Anvil.core.Button
		Atextfield = Anvil.core.Textfield
		Atext      = Anvil.core.Text 

		# defin UI elements
		self.window        = Awindow( title='Hammer Login' )
		button_stat        = Abutton( name='Sign in', cmd=self.toto )
		text_login         = Atext( text='login : ' )
		text_password      = Atext( text='Password : ' )
		textfield_login    = Atextfield()
		textfield_password = Atextfield()

		# defind layout
		self.window.addChild( text_login )
		self.window.addChild( textfield_login )
		self.window.addChild( text_password )
		self.window.addChild( textfield_password )
		self.window.addChild( button_stat )

	def toto( self ):
		print 'login'

	def create(self):
		return self.window
