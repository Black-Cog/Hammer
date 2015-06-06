
import Forge.core
import Hammer.core

import FnBaseEntity

class FnTexture( FnBaseEntity.FnBaseEntity ):
	def __init__( self ):
		self.initFn()

		interpreter = Forge.core.System().interpreter()

		if interpreter == 'Nuke8.0':
			self._fn.append( self.publish )

		elif interpreter == 'maya':
			self._fn.append( self.get )

		self._fn.append( self.openSourceScene )

	def publish( self, entity ):
		print 'publish : %s' %( str(entity) )

	def get( self, entity ):
		print 'get : %s' %( str(entity) )

	def openSourceScene( self, entity ):
		self.baseEntityProperty = Hammer.core.Actions.BaseEntityOpenSourceScene( ui=True, entity=entity )
