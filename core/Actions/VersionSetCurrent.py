
import BaseAction
import Forge.core.Process

class VersionSetCurrent( BaseAction.BaseAction ):

	def _doAction( self, entity, arg ):

		import Hammer
		Hammer.Database().editEntity( entity, version=entity['version'] )
