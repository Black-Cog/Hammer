
import Forge.core.Process
import BaseAction

class BaseEntityOpenSourceScene( BaseAction.BaseAction ):

	def _doUi( self, entity ):
		import Hammer.ui
		self.popup = Hammer.ui.WindowOpen(
			entity=entity,
			cmd=Forge.core.Process.partial( self._doAction, entity ),
		 )

		self.popup.show()

	def _doAction( self, entity ):
		path = entity['source']

		if path and Forge.core.System.exists( path ):
			extension = Forge.core.System.getExtension( path )

			if extension == 'nk':
				Forge.core.Process.launchSoftware( 'c:/Program Files/Nuke8.0v3/Nuke8.0.exe', arg=path )

			elif extension == 'ma':
				Forge.core.Process.launchSoftware( 'c:/Program Files/Autodesk/Maya2015/bin/maya.exe', arg=path )

			else :
				import Hammer.ui
				self.popup = Hammer.ui.WindowInfo( title='Warning', info='The extension "%s" is unknow.' %(extension) )
				self.popup.show()

		else :
			import Hammer.ui
			self.popup = Hammer.ui.WindowInfo( title='Warning', info='No file found at this location : %s.' %(path) )
			self.popup.show()
