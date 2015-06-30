
import BaseAction
import Forge.core.Process

class VersionApproved( BaseAction.BaseAction ):

	def _doAction( self, entity, arg, ui ):

		import Hammer
		newApproved = entity['approved']

		value = newApproved[ entity['version'] ]

		if value:
			value = False
		else:
			value = True

		newApproved[ entity['version'] ] = value
		Hammer.Database().editEntity( entity['entityId'], approved=newApproved )

		ui._buildTreeEntity( entity['entityId'] )
