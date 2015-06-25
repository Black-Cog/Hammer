
import Forge.core

import BaseAction

class BasePublishAction( BaseAction.BaseAction ):

	def _doUi( self, entity, arg ):
		import Hammer.ui
		self.popup = Hammer.ui.WindowPublish(
			entity=entity,
			cmd=Forge.core.Process.partial( self._doAction, entity ),
		 )

		self.popup.show()

	def _doAction( self, entity, arg ):
		import Hammer.ui

		if arg['description']['value']:
			if self._verification( entity, arg ):
				self._doPublish( entity=entity, arg=arg )
			else:
				self.popupVerification = Hammer.ui.WindowWarning( title='Verification', info="Can't SaveInc, because can't find any entityInfo in this scene." )
				self.popupVerification.show()
				return

		else:
			self.ask = Hammer.ui.WindowAsk(
				title='Need description.',
				issue='You need to write a description to Publish. Retry?',
				cmdYes=Forge.core.Process.partial( self._doUi, entity, None ),
				)
			self.ask.show()

	def _doPublish( self, entity, arg ):
		pass

	def _verification( self, entity, arg ):
		return True
