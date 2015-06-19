
import Forge.core.Process
import Anvil.core

import WindowPopup

class WindowExecute( WindowPopup.WindowPopup ):
	def __init__( self, title=None, iconPath=None, size=[ 400, 100 ], entity=None, cmd=None, arg=None ):

		if not title:
			title = 'Execute'

		self.init( title=title, iconPath=iconPath, size=size )

		self._cmd = cmd

		# defind class
		Abutton = Anvil.core.Button

		# layout init
		self.layout_main = Anvil.core.Layout( parent=self.window )

		# customUI init
		self._buildCustom( arg=arg )

		# buttons init
		button_open = Abutton( name='Execute', cmd=self.execute, w=size[0]/2 - 15, h=25 )
		button_abort = Abutton( name='Abort', cmd=self.window.close, w=size[0]/2 - 15, h=25 )

		# defind layouts content
		self.layout_main.add( [ button_open, button_abort ] )

	def execute( self ):
		self.window.close()

		if self._cmd:
			cmd = Forge.core.Process.partial( self._cmd, self._queryCustom() )
			cmd()

	def _buildCustom( self, arg ):
		if not arg:
			return

		for key, value in arg.iteritems():
			field = None

			if value['type'] == 'string':
				field = Anvil.core.Textfield( text=value['value'], name=key )

			elif value['type'] == 'int':
				field = Anvil.core.Intfield( value=value['value'], name=key )

			elif value['type'] == 'float':
				field = Anvil.core.Floatfield( value=value['value'], name=key )

			elif value['type'] == 'bool':
				field = Anvil.core.Checkbox( value=value['value'], name=key )

			elif value['type'] == 'color':
				field = Anvil.core.Colorpicker( color=value['value'], name=key )

			elif value['type'] == 'enum':
				field = Anvil.core.Dropmenu( items=value['value'], name=key, w=150 )

			self.layout_main.add([
					Anvil.core.Text( text='%s :' %(key), w=100 ),
					field,
						])

	def _queryCustom( self ):

		arg = {}
		for item in self.layout_main.children():

			if isinstance( item, Anvil.core.Textfield ):
				arg[item.name] = {
									'type'  : 'string',
									'value' : item.getValue(),
								}

			elif isinstance( item, Anvil.core.Intfield ):
				arg[item.name] = {
									'type'  : 'int',
									'value' : item.getValue(),
								}

			elif isinstance( item, Anvil.core.Floatfield ):
				arg[item.name] = {
									'type'  : 'float',
									'value' : item.getValue(),
								}

			elif isinstance( item, Anvil.core.Checkbox ):
				arg[item.name] = {
									'type'  : 'bool',
									'value' : item.getValue(),
								}

			elif isinstance( item, Anvil.core.Colorpicker ):
				arg[item.name] = {
									'type'  : 'color',
									'value' : item.getValue(),
								}

			elif isinstance( item, Anvil.core.Dropmenu ):
				arg[item.name] = {
									'type'  : 'enum',
									'value' : item.getValue(),
								}

		return arg
