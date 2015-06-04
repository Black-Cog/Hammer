
import FnBaseEntity

class FnAnimationGeo( FnBaseEntity.FnBaseEntity ):
	def __init__( self ):
		self.initFn()
		self._fn.append( self.publish )
		self._fn.append( self.get )
		self._fn.append( self.importEntity )
		self._fn.append( self.openSourceScene )

	def publish( self, entity ):
		print 'publish : %s' %( str(entity) )

	def get( self, entity ):
		print 'get : %s' %( str(entity) )

	def importEntity( self, entity ):
		print 'importEntity : %s' %( str(entity) )

	def openSourceScene( self, entity ):
		print 'openSourceScene : %s' %( str(entity) )
