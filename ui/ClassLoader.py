
import sys
import Anvil.core
import Login
import Hammer.core

class ClassLoader():

	def __init__(self):

		# todo : reimplement login : actions init
		# log = lambda: Hammer.core.FnUser().log( self )
		
		# todo : reimplement login : load login ui
		# self.login = Login.Login( cmd=log )
		self.ui()

	def app( self ):
		# todo : reimplement login : return login window to start
		# return self.login.window
		return self.window

	def ui( self ):
		from PySide import QtGui, QtCore

		# todo : reimplement login : close login UI
		# self.login.window.hide()

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

		# currentWidget()
		tab_main.setCurrentWidget( tab_main.widget(1) )

		############
		# User
		############

		# layout init
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


		############
		# Project
		############

		# layout init
		layout_project = Alayout( parent=tab_main.widget(1) )

		# textfields init
		self.textfield_urlPath = Atextfield( text='/', w=350 )

		# actions init
		upFolder = lambda: Hammer.core.FnProject().upFolder( self )

		# buttons init
		button_up = Abutton( name='UP', cmd=upFolder, w=25, h=25 )
		button_set = Abutton( name='>', cmd=upFolder, w=25, h=25 )

		# defind layouts content
		layout_project.add( [button_up, button_set, self.textfield_urlPath] )

		# build entity UI
		for entityUI in self._buildEntityUI():
			layout_project.add( entityUI )

		self.window.show()
		# self.window.showMaximized()

	def _buildEntityUI( self, entityId=1 ):
		entity = Hammer.core.getEntity( entityId )

		textList = []
		# texts init
		for childId in entity.getChildrenId():
			child = Hammer.core.getEntity( childId )
			textList.append( Anvil.core.Text(text=child.getName(), w=200) )

		return textList
