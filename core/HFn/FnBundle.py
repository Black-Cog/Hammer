
import FnBaseEntity

class FnBundle( FnBaseEntity.FnBaseEntity ):
	def __init__( self ):
		self.initFn()
		self._fn.append( self.publish )
		self._fn.append( self.get )

	def publish( self ):
		print 'publish'

	def get( self ):
		print 'get'
