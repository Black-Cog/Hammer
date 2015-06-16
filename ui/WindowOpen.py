
import Anvil.core

import WindowExecute

class WindowOpen( WindowExecute.WindowExecute ):
	def __init__( self, title=None, iconPath=None, size=[ 400, 100 ], entity=None, cmd=None, arg=None ):

		if not title:
			title = 'Open entity : %i' %( entity['entityId'] )

		self.init( title=title, iconPath=iconPath, size=size )

		self._cmd = cmd

		# defind class
		Abutton = Anvil.core.Button

		# layout init
		self.layout_main = Anvil.core.Layout( parent=self.window )

		# customUI init
		self._buildCustom( arg=arg )

		# buttons init
		button_open = Abutton( name='Open', cmd=self.execute, w=size[0]/2 - 15, h=25 )
		button_abort = Abutton( name='Abort', cmd=self.window.close, w=size[0]/2 - 15, h=25 )

		# defind layouts content
		self.layout_main.add( [ button_open, button_abort ] )
