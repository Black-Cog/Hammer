import sys
import Forge.core

class FnProject(object):
	"""docstring for FnProject"""
	
	def upFolder( self, arg ):
		path = arg.textfield_urlPath.text()

		print path
		# feedback text
		# arg.login.text_feedback.setText( message )
