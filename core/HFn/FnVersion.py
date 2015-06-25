
import Forge.core
import Hammer.core

class FnVersion():
	def __init__( self, entity ):
		self._fn = 	[
					self.approved,
					self.setCurrent,
					]

	def approved( self, entity ):

		self.approved = Hammer.core.Actions.VersionApproved( entity=entity )

	def setCurrent( self, entity ):

		self.setCurrent = Hammer.core.Actions.VersionSetCurrent( entity=entity )
