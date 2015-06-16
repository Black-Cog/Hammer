
import sys
import Anvil.core
import Login
import Hammer.core
import Hammer.ui
import Forge.core.System

class ClassLoader():

	def __init__(self):

		# set env
		currentPath = Forge.core.System.getPath( __file__ )
		Forge.core.System.setEnv( currentPath )

		# todo : reimplement login : actions init
		# log = lambda: Hammer.core.HFn.FnUser().log( self )
		
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

		# window init
		self.window = Anvil.core.Window( title='Hammer', iconPath='../core/icon/hammer.png', size=[ 640, 480 ], menuBar=False )

		# tabs init
		tab_main = Anvil.core.Tab(
						parent=self.window,
						tabs=[
							'User',
							'Project',
							'Applications',
							'Farm',
							'Wiki',
							'Administration',
							'Paperwork',
							'Budjet',
							'Hiring',
							],
						)

		# set 'Project' as current tab
		tab_main.setCurrentWidget( tab_main.widget(1) )

		# setup Tabs
		Hammer.ui.User( parent=tab_main.widget(0) )
		Hammer.ui.Project( parent=tab_main.widget(1) )
		Hammer.ui.Applications( parent=tab_main.widget(2) )

		self.window.show()
