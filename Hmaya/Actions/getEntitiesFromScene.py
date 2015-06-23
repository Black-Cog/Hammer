
import Hammer.core.Actions.BaseAction

class getEntitiesFromScene( Hammer.core.Actions.BaseAction ):

	def _doAction( self, entity, arg ):

		import maya.cmds
		import Hammer

		self.returnValue = []
		entitiesInfo = maya.cmds.ls( 'entityInfo', type='transform' )

		entityId = None
		if 'entityId' in arg.keys():
			entityId = arg['entityId']

		entityType = None
		if 'entityType' in arg.keys():
			entityType = arg['entityType']


		for entityInfo in entitiesInfo:
			currentEntityId = maya.cmds.getAttr('%s.entityId' %(entityInfo))

			if entityId and entityId == currentEntityId:
				self.returnValue.append( Hammer.getEntity(currentEntityId) )

			if entityType and entityType == maya.cmds.getAttr('%s.entityType' %(entityInfo)):
				self.returnValue.append( Hammer.getEntity(currentEntityId) )
