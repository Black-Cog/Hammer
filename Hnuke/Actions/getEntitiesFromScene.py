
import Hammer.core.Actions.BaseAction

class GetEntitiesFromScene( Hammer.core.Actions.BaseAction ):

	def _doAction( self, entity, arg ):

		import nuke
		import Hammer

		self.returnValue = []
		entitiesInfo = Hammer.Hnuke.Actions.GetEntitiesInfoFromScene( entity=entity, arg=arg ).returnValue

		for entityInfo in entitiesInfo:
			currentEntityId = entityInfo.knob('entityId').value()

			self.returnValue.append( Hammer.getEntity(currentEntityId) )
