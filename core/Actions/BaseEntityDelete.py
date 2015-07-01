
import BaseAction
import Forge.core.Process

class BaseEntityDelete( BaseAction.BaseAction ):

	def _doUi( self, entity, arg, ui ):
		import Hammer.ui
		self.popup = Hammer.ui.WindowAsk(
			title='Delete the entity : %i' %( entity['entityId'] ),
			issue='Are you want to delete this entity? This action is definitive.',
			cmdYes=Forge.core.Process.partial( self._doAction, entity, arg, ui ),
			)

		self.popup.show()

	def _doAction( self, entity, arg, ui ):
		import Hammer

		entityId = entity.getEntityId()
		childrenList = [ entityId ]

		def listAllChildren( parentId ):
			childrens = Hammer.getEntity( parentId ).getChildrenId()
			if childrens:
				for children in childrens:
					childrenList.append( children )
					listAllChildren( children )

		listAllChildren( entityId )

		for children in childrenList:
			Hammer.Database().removeEntity( children )
