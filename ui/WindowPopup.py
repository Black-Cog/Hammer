
import Anvil.core

class WindowPopup():
	def __init__( self, title='Popup', size=[ 500, 200 ] ):
		self.init( title=title, size=size )

	def init( self, title, size ):
		self.window = Anvil.core.Window( title=title, size=size, menuBar=False )

	def show( self ):
		self.window.show()
