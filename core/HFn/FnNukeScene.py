
import Forge.core
import Hammer.core

import FnBaseEntity

class FnNukeScene( FnBaseEntity.FnBaseEntity ):
	def __init__( self, entity ):
		self.initFn()

		self.__interreter = Forge.core.System().interpreter()

		self._fn.append( self.openScene )

		if self.__interreter == 'Nuke8.0':
			entitiesLoad = Hammer.Hnuke.Actions.getEntitiesFromScene( arg={'entityId':entity['entityId']} ).returnValue
			if entitiesLoad and entitiesLoad[0]['entityId'] == entity['entityId']:
				self._fn.append( self.saveInc )

	def openScene( self, entity ):
		args = {}
		if self.__interreter == 'Nuke8.0':
			args['newSession'] = {
									'type' : 'bool',
									'value' : True,
								}

		self.openScene = Hammer.core.Actions.BaseEntityOpenScene( ui=True, entity=entity, arg=args )

	def saveInc( self, entity ):
		print 'saveInc : %s' %( str(entity) )
