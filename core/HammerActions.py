
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

	for i in open( "../core/db", "r"):
		dbEntityInfo = eval(i)
		if dbEntityInfo['entityId'] == entityId:
			return __getEntityType( dbEntityInfo )

	return None

def getActions( entity ):
	'''
	Return the list of action for the entity.
	'''

	import HFn

	entityType = entity.getType()

	for fnMethod in dir( HFn ):
		if fnMethod == 'Fn%s' %( entityType ):
			classFn = eval( 'HFn.%s' %(fnMethod) )
			return classFn()._fn
