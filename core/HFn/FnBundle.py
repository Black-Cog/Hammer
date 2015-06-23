
import FnBaseEntity

class FnBundle( FnBaseEntity.FnBaseEntity ):
	def __init__( self, entity ):
		self.initFn()
		self._fn.append( self.publish )
		self._fn.append( self.get )

	def publish( self, entity ):
		print 'publish : %s' %( str(entity) )

	def get( self, entity ):
		print 'get : %s' %( str(entity) )
