
import FnBaseEntity

class FnShot( FnBaseEntity.FnBaseEntity ):
	def __init__( self ):
		self.initFn()
		self._fn.append( self.createEntity )

	def createEntity( self ):
		print 'createEntity'
