
import Forge.core

import Hammer.core.Actions.BasePublishAction

class MayaSceneSaveInc( Hammer.core.Actions.BasePublishAction ):

	def _doPublish( self, entity, arg ):

		import Hammer

		# add new version
		Hammer.Database().addNewVersion( entity, arg['description']['value'], False )

		newVersion = len( entity['approved'] )

		# set current version
		Hammer.Database().editEntity( entity, version=newVersion )

		folder = '%s/%s/' %( entity['path'], str(newVersion*10).zfill(4) )
		path = '%s/scene.ma' %( folder )

		Forge.core.System.mkdir( folder )

		import maya.cmds
		entityInfo = Hammer.Hmaya.Actions.GetEntitiesInfoFromScene( entity=entity, arg={'entityId':entity['entityId']} ).returnValue[0]
		maya.cmds.setAttr( "%s.entityVersion" %(entityInfo), lock=False )
		maya.cmds.setAttr( '%s.entityVersion' %(entityInfo), newVersion )
		maya.cmds.setAttr( "%s.entityVersion" %(entityInfo), lock=True )

		maya.cmds.file( rename=path )
		maya.cmds.file( save=True, type='mayaAscii' )

		# publish done
		self.popup = Hammer.ui.WindowInfo( info='SaveInc done. New version : %i' %(newVersion) )
		self.popup.show()
