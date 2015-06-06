
import functools

import BaseAction

class BaseEntityOpenSourceScene( BaseAction.BaseAction ):

	def _doUi( self, entity ):
		import Hammer.ui
		self.popup = Hammer.ui.WindowOpen(
			entity=entity,
			cmd=functools.partial( self._doAction, entity ),
		 )

		self.popup.show()

	def _doAction( self, entity ):
		print 'Open Source Scene'
		print entity['source']

