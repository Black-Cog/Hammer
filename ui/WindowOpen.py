
import Anvil.core

import WindowPopup

class WindowOpen( WindowPopup.WindowPopup ):
	def __init__( self, title=None, size=[ 400, 100 ], entity=None, cmd=None ):

		if not title:
			title = 'Open entity : %i' %( entity['entityId'] )

		self.init( title=title, size=size )

		self.__cmd = cmd

		# defind class
		Abutton = Anvil.core.Button
		Acheckbox   = Anvil.core.Checkbox

		# layout init
		layout_main = Anvil.core.Layout( parent=self.window )

		# checkboxs init
		checkbox_newSession = Anvil.core.Checkbox( value=True )

		# texts init
		text_newSession = Anvil.core.Text( text='Open in new Session :', w=100 )

		# buttons init
		button_open = Abutton( name='Open', cmd=self.open, w=size[0]/2 - 15, h=25 )
		button_abort = Abutton( name='Abort', cmd=self.window.close, w=size[0]/2 - 15, h=25 )

		# defind layouts content
		layout_main.add( [ checkbox_newSession, text_newSession ] )
		layout_main.add( [ button_open, button_abort ] )

	def open( self ):
		self.window.close()

		if self.__cmd:
			self.__cmd()
