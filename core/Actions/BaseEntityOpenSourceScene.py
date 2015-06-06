
import functools
import subprocess
import os

import BaseAction

class BaseEntityOpenSourceScene( BaseAction.BaseAction ):

	def _doUi( self, entity ):
		import Hammer.ui
		self.popup = Hammer.ui.WindowOpen(
			entity=entity,
			cmd=functools.partial( self._doAction, entity ),
		 )

		self.popup.show()

	def _doAction( self, entity ):
		path = entity['source']

		if path and os.path.exists( path ):
			extension = path.split( '.' )[-1]

			if extension == 'nk':
				subprocess.call( ['c:/Program Files/Nuke8.0v3/Nuke8.0.exe', path] )

			elif extension == 'ma':
				subprocess.call( ['c:/Program Files/Autodesk/Maya2015/bin/maya.exe', path] )

			else :
				import Hammer.ui
				self.popup = Hammer.ui.WindowInfo( title='Warning', info='The extension %s is unknow.' %(extension) )
				self.popup.show()

		else :
			import Hammer.ui
			self.popup = Hammer.ui.WindowInfo( title='Warning', info='No file found at this location : %s.' %(path) )
			self.popup.show()
