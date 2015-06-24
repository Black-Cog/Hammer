
import Forge.core
import Hammer.core

import FnBaseEntity

class FnAnimationGeo( FnBaseEntity.FnBaseEntity ):
	def __init__( self, entity ):
		self.initFn()

		self.__interpreter = Forge.core.System().interpreter()

		if self.__interpreter == 'maya':
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
		args = {}
		if self.__interreter == 'maya':
			args['newSession'] = {
									'type' : 'bool',
									'value' : True,
								}

		self.openSourceScene = Hammer.core.Actions.BaseEntityOpenSourceScene( ui=True, entity=entity, arg=args )
