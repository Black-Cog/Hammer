
import FnBaseEntity

class FnReference( FnBaseEntity.FnBaseEntity ):
	def __init__( self ):
		self.initFn()
		self._fn.append( self.get )
		self._fn.append( self.importEntity )

	def get( self, entity ):
		print 'get : %s' %( str(entity) )

	def importEntity( self, entity ):
		print 'importEntity : %s' %( str(entity) )
