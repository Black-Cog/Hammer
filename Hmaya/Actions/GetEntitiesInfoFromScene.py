
import Hammer.core.Actions.BaseAction

class GetEntitiesInfoFromScene( Hammer.core.Actions.BaseAction ):

	def _doAction( self, entity, arg, ui ):

		import maya.cmds
		import Hammer

		self.returnValue = []
		entitiesInfo = maya.cmds.ls( 'entityInfo', type='transform' )

		entityId = None
		if arg and 'entityId' in arg.keys():
			entityId = arg['entityId']

		entityType = None
		if arg and 'entityType' in arg.keys():
			entityType = arg['entityType']


		for entityInfo in entitiesInfo:
			if arg:
				currentEntityId = maya.cmds.getAttr('%s.entityId' %(entityInfo))

				if entityId and entityId == currentEntityId:
					self.returnValue.append( entityInfo )

				if entityType and entityType == maya.cmds.getAttr('%s.entityType' %(entityInfo)):
					self.returnValue.append( entityInfo )

			else:
				self.returnValue.append( entityInfo )
