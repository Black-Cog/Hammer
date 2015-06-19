
import Anvil.core
import Hammer

import WindowExecute

class WindowCreateEntity( WindowExecute.WindowExecute ):
	def __init__( self, title='Create Entity', iconPath=None, size=[ 400, 100 ], entity=None, cmd=None, arg={} ):

		self.init( title=title, iconPath=iconPath, size=size )

		self._cmd = cmd

		# defind class
		Abutton = Anvil.core.Button

		# layout init
		self.layout_main = Anvil.core.Layout( parent=self.window )

		entityType = []
		for item in dir( Hammer.core.EntityType ):
			if not '__' in item and not item == 'BaseEntity':
				entityType.append( {item:item} )

		# define arguments
		args = {}
		args['type'] = {
							'type' : 'enum',
							'value' : entityType
						}

		args['name'] = 	{
							'type' : 'string',
							'value' : '',
						}

		args.update( arg )

		# customUI init
		self._buildCustom( arg=args )

		# buttons init
		button_launch = Abutton( name='Create Entity', cmd=self.execute, w=size[0]/2 - 15, h=25 )
		button_abort = Abutton( name='Abort', cmd=self.window.close, w=size[0]/2 - 15, h=25 )

		# defind layouts content
		self.layout_main.add( [ button_launch, button_abort ] )
