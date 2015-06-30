
import FnBaseEntity

class FnReference( FnBaseEntity.FnBaseEntity ):
	def __init__( self, entity, arg, ui ):
		self.initFn()
		self._fn.append( self.get )
		self._fn.append( self.importEntity )

	def get( self, entity, arg, ui ):
		print 'get : %s' %( str(entity) )

	def importEntity( self, entity, arg, ui ):
		print 'importEntity : %s' %( str(entity) )
