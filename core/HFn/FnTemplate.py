
import Hammer.core

import FnBaseEntity

class FnTemplate( FnBaseEntity.FnBaseEntity ):
	def __init__( self, entity ):
		self.initFn()
		self._fn.append( self.publish )
		self._fn.append( self.get )
		self._fn.append( self.openSourceScene )

	def publish( self, entity ):
		print 'publish : %s' %( str(entity) )

	def get( self, entity ):
		print 'get : %s' %( str(entity) )

	def openSourceScene( self, entity ):
		self.openSourceScene = Hammer.core.Actions.BaseEntityOpenSourceScene( ui=True, entity=entity )
