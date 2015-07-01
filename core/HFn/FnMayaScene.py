
import Forge.core
import Hammer.core

import FnBaseEntity

class FnMayaScene( FnBaseEntity.FnBaseEntity ):
	def __init__( self, entity, arg, ui ):
		self.initFn()

		self.__interreter = Forge.core.System().interpreter()

		self._fn.append( self.openScene )

		if self.__interreter == 'maya':
			entitiesLoad = Hammer.Hmaya.Actions.GetEntitiesFromScene( arg={'entityId':entity['entityId']} ).returnValue
			if entitiesLoad and entitiesLoad[0]['entityId'] == entity['entityId']:
				self._fn.append( self.saveInc )

	def openScene( self, entity, arg, ui ):
		if self.__interreter == 'maya':
			arg['newSession'] = {
									'type' : 'bool',
									'value' : True,
								}

		self.openScene = Hammer.core.Actions.BaseEntityOpenScene( window=True, entity=entity, arg=arg, ui=ui )

	def saveInc( self, entity, arg, ui ):

		self.saveInc = Hammer.Hmaya.Actions.MayaSceneSaveInc( window=True, entity=entity, arg=arg, ui=ui )
