import sys
import Forge.core

class FnProject():
	"""docstring for FnProject"""
	
	@staticmethod
	def upFolder( arg ):
		path = arg.textfield_urlPath.text()

		print path
		# feedback text
		# arg.login.text_feedback.setText( message )

	@staticmethod
	def getActions( entity ):
		entityType = entity.getType()



