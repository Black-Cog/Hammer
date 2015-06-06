
import Anvil.core

import WindowPopup

class WindowAsk( WindowPopup.WindowPopup ):
	def __init__( self, title='Ask', size=[ 500, 100 ],iconPath=None, issue='Are you sure?', cmdYes=None, cmdNo=None ):
		self.init( title=title, iconPath=iconPath, size=size )

		self.__cmdYes = cmdYes
		self.__cmdNo = cmdNo

		# defind class
		Abutton = Anvil.core.Button

		# layout init
		layout_main = Anvil.core.Layout( parent=self.window )

		# texts init
		text_ask = Anvil.core.Text( text=issue , w=size[0], h=size[1]-50 )

		# buttons init
		button_yes = Abutton( name='Yes', cmd=self.cmdYes, w=size[0]/2 - 15, h=25 )
		button_no = Abutton( name='No', cmd=self.cmdNo, w=size[0]/2 - 15, h=25 )

		# defind layouts content
		layout_main.add( text_ask )
		layout_main.add( [ button_yes, button_no ] )

	def cmdYes( self ):
		self.window.close()

		if self.__cmdYes:
			self.__cmdYes()

	def cmdNo( self ):
		self.window.close()

		if self.__cmdNo:
			self.__cmdNo()
