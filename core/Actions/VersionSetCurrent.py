
import BaseAction
import Forge.core.Process

class VersionSetCurrent( BaseAction.BaseAction ):

	def _doAction( self, entity, arg, ui ):

		import Hammer
		Hammer.Database().editEntity( entity['entityId'], version=entity['version'] )

		ui._buildTreeEntity( entity['entityId'] )
