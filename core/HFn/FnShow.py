
import FnBaseEntity
import Hammer

class FnShow( FnBaseEntity.FnBaseEntity ):
	def __init__( self, entity, arg, ui ):
		self.initFn()
		self._fn.append( self.createEntity )

	def createEntity( self, entity, arg, ui ):

		self.openSourceScene = Hammer.core.Actions.CreateEntity( window=True, entity=entity, arg=arg, ui=ui )
