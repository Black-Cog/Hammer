
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

		interpreter = Forge.core.System().interpreter()
		if interpreter == 'python' :
			tabs = {
					'User':0,
					'Project':1,
					'Applications':2,
					'Farm':3,
					'Wiki':4,
					'Administration':5,
					'Paperwork':6,
					'Budjet':7,
					'Hiring':8,
					}
		else:
			tabs = {
					'User':0,
					'Project':1,
					'SceneContent':2,
					'Applications':3,
					'Farm':4,
					'Wiki':5,
					'Administration':6,
					'Paperwork':7,
					'Budjet':8,
					'Hiring':9,
					}

		# convertuild tab list
		self.__tabList = []
		self.__tabCount = 0
		def buildTabList( self, tabs ):
		    for key, value in tabs.iteritems():
		        if value == self.__tabCount:
		            self.__tabCount += 1
		            self.__tabList.append( key )
		            buildTabList( self, tabs )
		buildTabList( self, tabs )

		# tabs init
		tab_main = Anvil.core.Tab(
						parent=self.window,
						tabs=self.__tabList,
						)

		# set 'Project' as current tab
		tab_main.setCurrentWidget( tab_main.widget(tabs['Project']) )

		# setup Tabs
		Hammer.ui.User( parent=tab_main.widget(tabs['User']) )
		Hammer.ui.Project( parent=tab_main.widget(tabs['Project']) )
		Hammer.ui.Applications( parent=tab_main.widget(tabs['Applications']) )

		if 'SceneContent' in tabs.keys():
			Hammer.ui.SceneContent( parent=tab_main.widget(tabs['SceneContent']) )

		self.window.show()
