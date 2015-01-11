
import sys
import Anvil.core
import Login
import Hammer.core

class ClassLoader():

	def __init__(self):
		# load login ui
		self.login = Login.Login( cmd=self.log )

	def app( self ):
		return self.login.window


	def log( self ):

		login    = self.login.textfield_login.text()
		password = self.login.textfield_password.text()

		if login and password:
			if self.checkLogin( login=login, password=password ) :
				message  = 'login success'
				self.ui()
			else : message = 'login failed'
		else : message = 'Login or/and password are empty.'

		# feedback text
		self.login.text_feedback.setText( message )

	@staticmethod
	def checkLogin( login, password ):
		# mysql call here
		# fake value
		loginArray    = ['toto', 'tata', 'clipo', 'cedric', 'sebastien']
		passwordArray = ['toto', 'tata', 'clipo', 'sebastien', 'cedric']
		check = False

		if login in loginArray:
			index = loginArray.index( login )
			if password == passwordArray[ index ] : check = True

		return check


	def ui( self ):
		from PySide import QtGui, QtCore
		# close login UI
		self.login.window.hide()

		# defind class
		Awindow       = Anvil.core.Window
		Alayout       = Anvil.core.Layout
		Atext         = Anvil.core.Text
		Atextfield    = Anvil.core.Textfield
		Abutton       = Anvil.core.Button
		Atab          = Anvil.core.Tab

		fnUser        = Hammer.core.FnUser()
		hammerActions = Hammer.core.HammerActions()

		# window init
		self.window = Awindow( title='Hammer', size=[ 640, 480 ] )

		# tabs init
		tab_main = Atab( parent=self.window, tabs=[ 'User', 'Project', 'Farm', 'Wiki', 'Administration', 'Paperwork', 'Budjet', 'Hiring' ] )

		# # layout init
		layout_user = Alayout( parent=tab_main.widget(0) )

		# texts init
		text_user          = Atext( text=fnUser.getUserName(),      w=200 )
		text_hours         = Atext( text=fnUser.getMonthlyHours(),  w=200 )
		text_timeOnProd    = Atext( text=fnUser.getTimeOnProd(),    w=200 )
		text_contractBegin = Atext( text=fnUser.getContractBegin(), w=200 )
		text_contractEnd   = Atext( text=fnUser.getContractEnd(),   w=200 )
		text_supervisor    = Atext( text=fnUser.getSupervisor(),    w=200 )

		# buttons init
		button_mail = Abutton( name='Mail', cmd=hammerActions.mail )

		# defind layouts content
		layout_user.add( text_user )
		layout_user.add( text_hours )
		layout_user.add( text_timeOnProd )
		layout_user.add( text_contractBegin )
		layout_user.add( text_contractEnd )
		layout_user.add( text_supervisor )

		layout_user.add( button_mail )

		self.window.showMaximized()
