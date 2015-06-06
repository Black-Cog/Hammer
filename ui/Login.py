
import Anvil.core

class Login():
	"""docstring for Login"""
	def __init__( self, cmd=None ):

		# defind class
		Awindow    = Anvil.core.Window
		Alayout    = Anvil.core.Layout
		Atext      = Anvil.core.Text
		Atextfield = Anvil.core.Textfield
		Abutton    = Anvil.core.Button

		# window init
		self.window = Awindow( title='Hammer Login', size=[ 640, 480 ], menuBar=False )
		layout_main = Alayout( parent=self.window, x=self.window.geometry().width()/2-130, y=self.window.geometry().height()/2-50 )

		# texts init
		text_login         = Atext( text='Login        :', w=55 )
		text_password      = Atext( text='Password :'    , w=55 )
		self.text_feedback = Atext( text='', w=260 )

		# textfields init
		self.textfield_login    = Atextfield( text='', w=195 )
		self.textfield_password = Atextfield( text='', w=195 )

		# buttons init
		button_log = Abutton( name='Sign in', cmd=cmd, w=260, h=35 )

		# defind layouts content
		layout_main.add( [text_login,    self.textfield_login] )
		layout_main.add( [text_password, self.textfield_password] )
		layout_main.add( button_log )
		layout_main.add( self.text_feedback )
