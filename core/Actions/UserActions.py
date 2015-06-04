
class UserActions():
	"""docstring for HammerActions"""
	
	@staticmethod
	def mail():
		print 'email forwarded'

	@staticmethod
	def launchPublish( filename2=None, classname2=None ):
		import sys
		sys.path.append( 'F:/dev/Hammer/maya/actions/' )

		filename  = 'FnPublishModelingPrint'
		classname = 'Modeling'
		importcmd   = 'from %s import %s' %( filename, classname )
		instancecmd = 'inst = %s()' %( classname )

		exec( importcmd )
		exec( instancecmd )

		instMethods = dir( inst )


		if 'verification' in instMethods:
			print 'verification'

		if 'publish' in instMethods:
			print 'publish'
