
import Forge.core
import Hammer.core

class FnVersion():
	def __init__( self, entity, arg, ui ):
		self._fn = 	[
					self.approved,
					self.setCurrent,
					]

	def approved( self, entity, arg, ui ):

		self.approved = Hammer.core.Actions.VersionApproved( entity=entity, arg=arg, ui=ui )

	def setCurrent( self, entity, arg, ui ):

		self.setCurrent = Hammer.core.Actions.VersionSetCurrent( entity=entity, arg=arg, ui=ui )
