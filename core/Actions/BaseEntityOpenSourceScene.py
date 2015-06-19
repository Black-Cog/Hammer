
import Forge.core.Process
import BaseAction

class BaseEntityOpenSourceScene( BaseAction.BaseAction ):

	def _doUi( self, entity, arg ):
		import Hammer.ui

		self.popup = Hammer.ui.WindowOpen(
			entity=entity,
			cmd=Forge.core.Process.partial( self._doAction, entity ),
			arg=arg,
		 )

		self.popup.show()

	def _doAction( self, entity, arg ):
		path = entity['source'][entity['version']]

		if path and Forge.core.System.exists( path ):
			extension = Forge.core.System.getExtension( path )

			newSession = True
			if 'newSession' in arg:
				newSession = arg['newSession']['value']

			if extension == 'nk':
				if newSession:
					Forge.core.Process.launchSoftware( 'c:/Program Files/Nuke8.0v3/Nuke8.0.exe', arg=path )
				else:
					import nuke
					nuke.scriptOpen( path )

			elif extension == 'ma':
				if newSession:
					Forge.core.Process.launchSoftware( 'c:/Program Files/Autodesk/Maya2015/bin/maya.exe', arg=path )
				else:
					import maya.cmds
					maya.cmds.file( path, f=True, o=True )

			else :
				import Hammer.ui
				self.popup = Hammer.ui.WindowInfo( title='Warning', info='The extension "%s" is unknow.' %(extension) )
				self.popup.show()

		else:
			import Hammer.ui
			self.popup = Hammer.ui.WindowInfo( title='Warning', info='No file found at this location : %s.' %(path) )
			self.popup.show()
