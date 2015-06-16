
import Anvil.core

import WindowExecute

class WindowPublish( WindowExecute.WindowExecute ):
	def __init__( self, title='Publish', iconPath=None, size=[ 400, 100 ], entity=None, cmd=None, arg=None ):

		if not title:
			title = 'Publish entity : %i' %( entity['entityId'] )

		self.init( title=title, iconPath=iconPath, size=size )

		self._cmd = cmd

		# defind class
		Abutton = Anvil.core.Button

		# layout init
		self.layout_main = Anvil.core.Layout( parent=self.window )

		# customUI init
		self._buildCustom( arg=arg )

		# buttons init
		button_launch = Abutton( name='Launch Publish', cmd=self.execute, w=size[0]/2 - 15, h=25 )
		button_abort = Abutton( name='Abort', cmd=self.window.close, w=size[0]/2 - 15, h=25 )

		# defind layouts content
		self.layout_main.add( [ button_launch, button_abort ] )
