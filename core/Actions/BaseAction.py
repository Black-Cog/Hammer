

class BaseAction():
	def __init__( self, ui=False, entity=None, arg=None ):

		if ui:
			self._doUi( entity=entity, arg=arg )
		else:
			self._doAction( entity=entity, arg=arg )

	def _doUi( self, entity, arg ):
		pass

	def _doAction( self, entity, arg ):
		pass
