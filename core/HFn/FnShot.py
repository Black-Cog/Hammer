
import FnBaseEntity
import Hammer

class FnShot( FnBaseEntity.FnBaseEntity ):
	def __init__( self ):
		self.initFn()
		self._fn.append( self.createEntity )

	def createEntity( self, entity ):

		self.openSourceScene = Hammer.core.Actions.CreateEntity( ui=True, entity=entity )
