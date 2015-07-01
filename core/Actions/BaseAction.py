

class BaseAction():
	def __init__( self, window=False, entity=None, arg={}, ui=None ):

		self.returnValue = None

		if window:
			self._doUi( entity=entity, arg=arg, ui=ui )
		else:
			self._doAction( entity=entity, arg=arg, ui=ui )

	def _doUi( self, entity, arg, ui ):
		pass

	def _doAction( self, entity, arg, ui ):
		pass
