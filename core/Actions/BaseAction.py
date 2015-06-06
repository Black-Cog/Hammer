

class BaseAction():
	def __init__( self, ui=False, entity=None ):

		if ui:
			self._doUi( entity=entity )
		else:
			self._doAction( entity=entity )

	def _doUi( self, entity ):
		pass

	def _doAction( self, entity ):
		pass
