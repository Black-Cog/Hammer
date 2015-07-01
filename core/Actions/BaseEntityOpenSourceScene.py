
import Forge.core
import BaseAction

class BaseEntityOpenSourceScene( BaseAction.BaseAction ):

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

		path = ''
		if entity['version'] > 0 :
			path = entity['source'][entity['version']]

		if path and Forge.core.System.exists( path ):
			extension = Forge.core.System.getExtension( path )

			newSession = True
			if 'newSession' in arg:
				newSession = arg['newSession']['value']

			if extension == 'nk':
				if newSession:
					Forge.core.Process.launchSoftware( Forge.core.Env().nuke, arg=path )
				else:
					import nuke
					nuke.scriptOpen( path )

			elif extension == 'ma':
				if newSession:
					Forge.core.Process.launchSoftware( Forge.core.Env().maya, arg=path )
				else:
					import maya.cmds
					maya.cmds.file( path, f=True, o=True )

			else :
				import Hammer.ui
				self.popup = Hammer.ui.WindowWarning( info='The extension "%s" is unknow.' %(extension) )
				self.popup.show()

		else:
			import Hammer.ui
			self.popup = Hammer.ui.WindowWarning( info='No file found at this location : %s.' %(path) )
			self.popup.show()
