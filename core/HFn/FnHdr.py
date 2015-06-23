
import Forge.core
import Hammer.core

import FnBaseEntity

class FnHdr( FnBaseEntity.FnBaseEntity ):
	def __init__( self, entity ):
		self.initFn()

		self.__interreter = Forge.core.System().interpreter()

		if self.__interreter == 'Nuke8.0':
			self._fn.append( self.publish )

		elif self.__interreter == 'maya':
			self._fn.append( self.get )

		self._fn.append( self.openSourceScene )

	def publish( self, entity ):
		self.publish = Hammer.core.Actions.HdrPublish( ui=True, entity=entity )

	def get( self, entity ):
		print 'get : %s' %( str(entity) )

	def openSourceScene( self, entity ):
		args = {}
		if self.__interreter == 'Nuke8.0':
			args['newSession'] = {
									'type' : 'bool',
									'value' : True,
								}

		self.openSourceScene = Hammer.core.Actions.BaseEntityOpenSourceScene( ui=True, entity=entity, arg=args )
