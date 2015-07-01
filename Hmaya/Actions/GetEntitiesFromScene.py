
import Hammer.core.Actions.BaseAction

class GetEntitiesFromScene( Hammer.core.Actions.BaseAction ):

	def _doAction( self, entity, arg, ui ):

		import maya.cmds
		import Hammer

		self.returnValue = []
		entitiesInfo = Hammer.Hmaya.Actions.GetEntitiesInfoFromScene( entity=entity, arg=arg, ui=ui ).returnValue

		for entityInfo in entitiesInfo:
			currentEntityId = maya.cmds.getAttr('%s.entityId' %(entityInfo))

			self.returnValue.append( Hammer.getEntity(currentEntityId) )
