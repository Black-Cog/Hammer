
import Hammer.core

import FnBaseEntity

class FnTemplate( FnBaseEntity.FnBaseEntity ):
	def __init__( self, entity, arg, ui ):
		self.initFn()
		self._fn.append( self.publish )
		self._fn.append( self.get )
		self._fn.append( self.openSourceScene )

	def publish( self, entity, arg, ui ):
		print 'publish : %s' %( str(entity) )

	def get( self, entity, arg, ui ):
		print 'get : %s' %( str(entity) )

	def openSourceScene( self, entity, arg, ui ):
		self.openSourceScene = Hammer.core.Actions.BaseEntityOpenSourceScene( window=True, entity=entity, arg=arg, ui=ui )
