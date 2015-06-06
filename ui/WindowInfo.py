
import Anvil.core

import WindowPopup

class WindowInfo( WindowPopup.WindowPopup ):
	def __init__( self, title='Ask', size=[ 500, 100 ], info='Infomation.' ):
		self.init( title=title, size=size )

		# layout init
		layout_main = Anvil.core.Layout( parent=self.window )

		# texts init
		text_ask = Anvil.core.Text( text=info , w=size[0], h=size[1]-50 )

		# buttons init
		button_ok = Anvil.core.Button( name='Ok', cmd=self.window.close, w=size[0]-15, h=25 )

		# defind layouts content
		layout_main.add( text_ask )
		layout_main.add( button_ok )
