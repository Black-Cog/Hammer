
import BaseAction

class BaseEntityProperty( BaseAction.BaseAction ):

	def _doUi( self, entity, arg, ui ):
		import Hammer.ui
		self.popup = Hammer.ui.WindowProperty( entity=entity )
		self.popup.show()
