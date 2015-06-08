
import BaseAction
import Forge.core.Process

class BaseEntityDelete( BaseAction.BaseAction ):

	def _doUi( self, entity ):
		import Hammer.ui
		self.popup = Hammer.ui.WindowAsk(
			title='Delete the entity : %i' %( entity['entityId'] ),
			issue='Are you want to delete this entity? This action is definitive.',
			cmdYes=Forge.core.Process.partial( self._doAction, entity ),
			)

		self.popup.show()

	def _doAction( self, entity ):
		print 'actionDelete'
