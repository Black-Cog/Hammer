
import BaseAction
import Forge.core.Process

class CreateEntity( BaseAction.BaseAction ):

	def _doUi( self, entity, arg ):
		import Hammer.ui
		self.popup = Hammer.ui.WindowCreateEntity(
			cmd=Forge.core.Process.partial( self._doAction, entity ),
			)

		self.popup.show()

	def _doAction( self, entity, arg ):

		import Hammer

		Hammer.Database().addEntity( name=arg['name']['value'], type=arg['type']['value'], parentId=entity.getEntityId() )
