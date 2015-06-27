
import BaseAction
import Forge.core

class CreateEntity( BaseAction.BaseAction ):

	def _doUi( self, entity, arg ):
		import Hammer.ui
		self.popup = Hammer.ui.WindowCreateEntity(
			cmd=Forge.core.Process.partial( self._doAction, entity ),
			)

		self.popup.show()

	def _doAction( self, entity, arg ):

		self.path = [
			arg['name']['value'] + '/',
			entity['name'] + '/',
			]
		import Hammer

		def listParentName( entity ):
			parent = Hammer.getEntity( entity['parentId'] )
			self.path.append( parent['name'] + '/' )

			if parent['entityType'] in ['Show', 'BaseEntity']:
				return
			listParentName( parent )
		listParentName( entity )

		self.path.append( Forge.core.Env().data )
		self.path.reverse()
		path = ''.join( self.path )

		if Forge.core.System().exists( path ):
			import Hammer.ui
			self.ask = Hammer.ui.WindowAsk(
				title='Entity already exist.',
				issue='This entity already exist. You need to change the name. Retry?',
				cmdYes=Forge.core.Process.partial( self._doUi, entity, None ),
				)
			self.ask.show()

		else:
			Hammer.Database().addEntity(
				name=arg['name']['value'],
				type=arg['type']['value'],
				parentId=entity.getEntityId(),
				path=path,
				)
