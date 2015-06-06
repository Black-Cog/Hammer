
import Anvil.core

class WindowPopup():
	def __init__( self, title='Popup',iconPath=None, size=[ 500, 200 ] ):
		self.init( title=title, iconPath=iconPath,size=size )

	def init( self, title, iconPath, size ):
		if not iconPath:
			iconPath = '../core/icon/hammer.png'
		self.window = Anvil.core.Window( title=title, iconPath=iconPath, size=size, menuBar=False )

	def show( self ):
		self.window.show()
