
import Forge.core.Process

import BaseAction

class HdrPublish( BaseAction.BaseAction ):

	def _doUi( self, entity, arg ):
		import Hammer.ui
		self.popup = Hammer.ui.WindowPublish(
			entity=entity,
			cmd=Forge.core.Process.partial( self._doAction, entity ),
		 )

		self.popup.show()

	def _doAction( self, entity, arg ):
		print 'Hdr Publish'

