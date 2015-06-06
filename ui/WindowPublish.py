
import Anvil.core

import WindowPopup

class WindowPublish( WindowPopup.WindowPopup ):
	def __init__( self, title='Publish', iconPath=None, size=[ 400, 100 ], entity=None, cmd=None ):

		if not title:
			title = 'Publish entity : %i' %( entity['entityId'] )

		self.init( title=title, iconPath=iconPath, size=size )

		self.__cmd = cmd

		# defind class
		Abutton = Anvil.core.Button

		# layout init
		layout_main = Anvil.core.Layout( parent=self.window )

		# buttons init
		button_launch = Abutton( name='Launch Publish', cmd=self.launchPublish, w=size[0]/2 - 15, h=25 )
		button_abort = Abutton( name='Abort', cmd=self.window.close, w=size[0]/2 - 15, h=25 )

		# defind layouts content
		layout_main.add( [ button_launch, button_abort ] )

	def launchPublish( self ):
		self.window.close()

		if self.__cmd:
			self.__cmd()
