
import FnBaseEntity

class FnBundle( FnBaseEntity.FnBaseEntity ):
	def __init__( self, entity, arg, ui ):
		self.initFn()
		self._fn.append( self.publish )
		self._fn.append( self.get )

	def publish( self, entity, arg, ui ):
		print 'publish : %s' %( str(entity) )

	def get( self, entity, arg, ui ):
		print 'get : %s' %( str(entity) )
