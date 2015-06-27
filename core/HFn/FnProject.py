import sys
import Forge.core

class FnProject():
	"""docstring for FnProject"""
	
	@staticmethod
	def upFolder( arg ):
		import Hammer

		if arg._currentEntityId != 1:
			# set current entityId to parentId
			entity = Hammer.getEntity( arg._currentEntityId )
			arg._currentEntityId = entity.getParentId()


			# remove last folder in the urlPath field
			folders = arg.textfield_urlPath.getValue().split( '/' )
			for i in [0,-2,-1]:
				del folders[i]

			path = '/'
			for folder in folders:
				path += '%s/' %(folder)

			arg.textfield_urlPath.setValue( path )

			# rebuild tree
			arg._buildTreeEntity( entityIdOverride=True )
