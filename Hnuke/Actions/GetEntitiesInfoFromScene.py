
import Hammer.core.Actions.BaseAction

class GetEntitiesInfoFromScene( Hammer.core.Actions.BaseAction ):

	def _doAction( self, entity, arg, ui ):

		import nuke
		import Hammer

		self.returnValue = []

		entitiesInfo = []
		for node in nuke.allNodes():
			if node.Class() == 'StickyNote' and node['name'].value() == 'entityInfo':
				entitiesInfo.append( node )

		entityId = None
		if arg and 'entityId' in arg.keys():
			entityId = arg['entityId']

		entityType = None
		if arg and 'entityType' in arg.keys():
			entityType = arg['entityType']


		for entityInfo in entitiesInfo:
			if arg:
				currentEntityId = entityInfo.knob('entityId').value()

				if entityId and entityId == currentEntityId:
					self.returnValue.append( entityInfo )

				if entityType and entityType == entityInfo.knob('entityType').value():
					self.returnValue.append( entityInfo )

			else:
				self.returnValue.append( entityInfo )
