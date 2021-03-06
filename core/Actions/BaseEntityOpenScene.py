
import Forge.core
import BaseAction

class BaseEntityOpenScene( BaseAction.BaseAction ):

	def _doUi( self, entity, arg, ui ):
		import Hammer.ui

		self.popup = Hammer.ui.WindowOpen(
			entity=entity,
			cmd=Forge.core.Process.partial( self._doAction, entity ),
			arg=arg,
			ui=ui,
		 )

		self.popup.show()

	def _doAction( self, entity, arg, ui ):

		extension = 'unknow'
		if entity['entityType'] == 'MayaScene':
			extension = 'ma'
		elif entity['entityType'] == 'NukeScene':
			extension = 'nk'

		path = '%s/%s/scene.%s' %( entity['path'], str(entity['version']*10).zfill(4), extension )

		pathExist = Forge.core.System.exists( path )

		newSession = True
		if 'newSession' in arg:
			newSession = arg['newSession']['value']

		if pathExist or entity['version'] == 0:
			if extension == 'nk':
				if entity['version'] > 0:
					if newSession:
						Forge.core.Process.launchSoftware( Forge.core.Env().nuke, arg=path )
					else:
						import nuke
						nuke.scriptOpen( path )
				else:
					if newSession:
							Forge.core.Process().launchNukePython(
							cmd='Hammer.Hnuke.Actions.CreateEntityInfo',
							arg='entity=Hammer.getEntity(%i)' %( entity['entityId'] ),
						)
					else:
						import Hammer.Hnuke.Actions
						# todo : clean scene
						Hammer.Hnuke.Actions.CreateEntityInfo( entity=entity )

			elif extension == 'ma':
				if entity['version'] > 0:
					if newSession:
						Forge.core.Process.launchSoftware( Forge.core.Env().maya, arg=path )
					else:
						import maya.cmds
						maya.cmds.file( path, f=True, o=True )
				else:
					if newSession:
						Forge.core.Process().launchMayaPython(
							cmd='Hammer.Hmaya.Actions.CreateEntityInfo',
							arg='entity=Hammer.getEntity(%i)' %( entity['entityId'] ),
						)
					else:
						import maya.cmds
						import Hammer.Hmaya.Actions
						maya.cmds.file( f=True, new=True )
						self.createEntityInfo = Hammer.Hmaya.Actions.CreateEntityInfo( entity=entity )

			else :
				import Hammer.ui
				self.popup = Hammer.ui.WindowWarning( info='The entity "%s" is not supported yet.' %(entity['entityType']) )
				self.popup.show()

		else :
			import Hammer.ui
			self.popup = Hammer.ui.WindowWarning( info='No file found at this location : %s.' %(path) )
 			self.popup.show()