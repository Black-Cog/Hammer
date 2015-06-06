
import functools

import BaseAction

class HdrPublish( BaseAction.BaseAction ):

	def _doUi( self, entity ):
		import Hammer.ui
		self.popup = Hammer.ui.WindowPublish(
			entity=entity,
			cmd=functools.partial( self._doAction, entity ),
		 )

		self.popup.show()

	def _doAction( self, entity ):
		print 'Hdr Publish'

