
import Hammer.core.Actions.BaseAction

class GetEntitiesFromScene( Hammer.core.Actions.BaseAction ):

	def _doAction( self, entity, arg ):

		import maya.cmds
		import Hammer

		self.returnValue = []
		entitiesInfo = Hammer.Hmaya.Actions.GetEntitiesInfoFromScene( entity=entity, arg=arg ).returnValue

		for entityInfo in entitiesInfo:
			currentEntityId = maya.cmds.getAttr('%s.entityId' %(entityInfo))

			self.returnValue.append( Hammer.getEntity(currentEntityId) )
