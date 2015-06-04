
import FnBaseEntity

class FnCamera( FnBaseEntity.FnBaseEntity ):
	def __init__( self ):
		self.initFn()
		self._fn.append( self.publish )
		self._fn.append( self.get )
		self._fn.append( self.importEntity )
		self._fn.append( self.openSourceScene )

	def publish( self ):
		print 'publish'

	def get( self ):
		print 'get'

	def importEntity( self ):
		print 'importEntity'

	def openSourceScene( self ):
		print 'openSourceScene'
