
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


class Database():
	def __init__( self ):
		self.db = "../core/db"

	def getEntity( self, entityId ):
		'''
		Return the entity based on the id.
		'''

		for i in open( self.db, "r"):
			dbEntityInfo = eval(i)
			if dbEntityInfo['entityId'] == entityId:
				return self.__getEntityType( dbEntityInfo )

		return None

	@staticmethod
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
									descriptions=dbEntityInfo['descriptions'],
									approved=dbEntityInfo['approved'],
									currentUser=dbEntityInfo['currentUser'],
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

	def __getNewId( self ):
		'''
		Return a new entity id.
		'''

		newEntityId = 0

		for i in open( self.db, "r"):
			dbEntityInfo = eval(i)
			if dbEntityInfo['entityId'] > newEntityId:
				newEntityId = dbEntityInfo['entityId']

		return newEntityId + 1

	def __getDbLine( self, entityId ):

		linecount = 0
		for i in open( self.db, "r"):
			dbEntityInfo = eval(i)
			if dbEntityInfo['entityId'] == entityId:
				return linecount
			linecount += 1

		return None

	def addEntity(
					self,
					name=None,
					type=None,
					path=None,
					version=0,
					descriptions={},
					approved={},
					currentUser=None,
					parentId=None,
					childrenId=[],
					copyId=None,
					referenceId=None,
					assetId=None,
					masterAssetId=None,
					dependencyId=None,
					bundleId=None,
					sources={},
				):

		# define data
		with open( self.db, 'r' ) as file:
			data = file.readlines()


		# define new entity
		entityId = self.__getNewId()
		data.append( str({
					'entityId':entityId,
					'name':name,
					'type':type,
					'path':path,
					'version':version,
					'descriptions':descriptions,
					'approved':approved,
					'currentUser':currentUser,
					'parentId':parentId,
					'childrenId':childrenId,
					'copyId':copyId,
					'referenceId':referenceId,
					'assetId':assetId,
					'masterAssetId':masterAssetId,
					'dependencyId':dependencyId,
					'bundleId':bundleId,
					'sources':sources,
					}) + '\n' )



		# edit parent entity
		if parentId:
			parentLine = self.__getDbLine(parentId)
			if parentLine:
				parent = eval( data[parentLine] )

				childrenList = parent['childrenId']
				childrenList.append( entityId )

				data[parentLine] = str({
									'entityId':parent['entityId'],
									'name':parent['name'],
									'type':parent['type'],
									'path':parent['path'],
									'version':parent['version'],
									'descriptions':parent['descriptions'],
									'approved':parent['approved'],
									'currentUser':parent['currentUser'],
									'parentId':parent['parentId'],
									'childrenId':childrenList,
									'copyId':parent['copyId'],
									'referenceId':parent['referenceId'],
									'assetId':parent['assetId'],
									'masterAssetId':parent['masterAssetId'],
									'dependencyId':parent['dependencyId'],
									'bundleId':parent['bundleId'],
									'sources':parent['sources'],
									}) + '\n'

		with open( self.db, 'w' ) as file:
			file.writelines( data )

	def removeEntity( self, entityId ):

		# define data
		with open( self.db, 'r' ) as file:
			data = file.readlines()


		# grab entity
		entityLine = self.__getDbLine(entityId)

		parentId = eval( data[entityLine] )['parentId']

		data[entityLine] = ''

		# edit parent entity
		if parentId:
			parentLine = self.__getDbLine(parentId)
			if not parentLine == None:
				parent = eval( data[parentLine] )

				childrenList = parent['childrenId']
				childrenList.remove( entityId )

				data[parentLine] = str({
									'entityId':parent['entityId'],
									'name':parent['name'],
									'type':parent['type'],
									'path':parent['path'],
									'version':parent['version'],
									'descriptions':parent['descriptions'],
									'approved':parent['approved'],
									'currentUser':parent['currentUser'],
									'parentId':parent['parentId'],
									'childrenId':childrenList,
									'copyId':parent['copyId'],
									'referenceId':parent['referenceId'],
									'assetId':parent['assetId'],
									'masterAssetId':parent['masterAssetId'],
									'dependencyId':parent['dependencyId'],
									'bundleId':parent['bundleId'],
									'sources':parent['sources'],
									}) + '\n'

			with open( self.db, 'w' ) as file:
				file.writelines( data )
