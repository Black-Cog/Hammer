
import FnBaseEntity

class FnLibrary( FnBaseEntity.FnBaseEntity ):
	def __init__( self ):
		self.initFn()
		self._fn.append( self.createEntity )

	def createEntity( self, entity ):
		print 'createEntity : %s' %( str(entity) )
