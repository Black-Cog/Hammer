
import Forge.core

import Hammer.core.Actions.BasePublishAction

class NukeSceneSaveInc( Hammer.core.Actions.BasePublishAction ):

	def _doPublish( self, entity, arg ):

		import Hammer

		# add new version
		Hammer.Database().addNewVersion( entity, arg['description']['value'], False )

		newVersion = len( entity['approved'] )

		# set current version
		Hammer.Database().editEntity( entity, version=newVersion )

		folder = '%s/%s/' %( entity['path'], str(newVersion*10).zfill(4) )
		path = '%s/scene.nk' %( folder )

		Forge.core.System.mkdir( folder )

		import nuke
		entityInfo = Hammer.Hnuke.Actions.GetEntitiesInfoFromScene( entity=entity, arg={'entityId':entity['entityId']} ).returnValue[0]
		entityInfo.knob('entityVersion').setValue( newVersion )

		nuke.scriptSaveAs( filename=path )

		# publish done
		self.popup = Hammer.ui.WindowInfo( info='SaveInc done. New version : %i' %(newVersion) )
		self.popup.show()
