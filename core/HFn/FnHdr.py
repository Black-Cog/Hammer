
import Forge.core
import Hammer.core

import FnBaseEntity

class FnHdr( FnBaseEntity.FnBaseEntity ):
	def __init__( self, entity, arg, ui ):
		self.initFn()

		self.__interreter = Forge.core.System().interpreter()

		if self.__interreter == 'Nuke8.0':
			self._fn.append( self.publish )

		elif self.__interreter == 'maya':
			self._fn.append( self.get )

		self._fn.append( self.openSourceScene )

	def publish( self, entity, arg, ui ):
		self.publish = Hammer.core.Actions.HdrPublish( window=True, entity=entity, arg=arg, ui=ui )

	def get( self, entity, arg, ui ):
		print 'get : %s' %( str(entity) )

	def openSourceScene( self, entity, arg, ui ):
		if self.__interreter == 'Nuke8.0':
			arg['newSession'] = {
									'type' : 'bool',
									'value' : True,
								}

		self.openSourceScene = Hammer.core.Actions.BaseEntityOpenSourceScene( window=True, entity=entity, arg=arg, ui=ui )
