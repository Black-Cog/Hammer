
def __getEntityType( dbEntityInfo ):

	import EntityType

	for entityType in dir( EntityType ):
		if entityType == dbEntityInfo['type']:
			entityClass = eval( 'EntityType.%s' %(entityType) )

			entity = entityClass(
								entityId = dbEntityInfo['entityId'],
								name = dbEntityInfo['name'],
								path = dbEntityInfo['path'],
								version = dbEntityInfo['version'],
								parentId = dbEntityInfo['parentId'],
								childrenId = dbEntityInfo['childrenId'],
								copyId = dbEntityInfo['copyId'],
								referenceId = dbEntityInfo['referenceId'],
								assetId = dbEntityInfo['assetId'],
								masterAssetId = dbEntityInfo['masterAssetId'],
								dependencyId = dbEntityInfo['dependencyId'],
								bundleId = dbEntityInfo['bundleId'],
								sources = dbEntityInfo['sources'],
								)
			return entity

def getEntity( entityId ):
	'''
	Return the entity based on the id.
	'''

	import os
	currentPath = os.path.dirname( os.path.realpath(__file__) )

	for i in open( currentPath + "/db", "r"):
		dbEntityInfo = eval(i)
		if dbEntityInfo['entityId'] == entityId:
			return __getEntityType( dbEntityInfo )

	return None




# todo : Refactor and move into python/Hammer/Actions
class HammerActions():
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
