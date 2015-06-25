
class BaseEntity():

	typeId = 0x100000

	def __init__(
				self,
				entityId=None,
				name=None,
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

		self.__entityId = entityId
		self.__name = name
		self.__path = path
		self.__version = version
		self.__descriptions = descriptions
		self.__approved = approved
		self.__currentUser = currentUser
		self.__parentId = parentId
		self.__childrenId = childrenId
		self.__copyId = copyId
		self.__referenceId = referenceId
		self.__assetId = assetId
		self.__masterAssetId = masterAssetId
		self.__dependencyId = dependencyId
		self.__bundleId = bundleId
		self.__sources = sources

	def __getitem__(self, key):
		if key == 'entityType':
			return self.getType()

		elif key == 'name':
			return self.getName()

		elif key == 'entityId':
			return self.getEntityId()

		elif key == 'path':
			return self.getPath()

		elif key == 'version':
			return self.getVersion()

		elif key == 'descriptions':
			return self.getDescriptions()

		elif key == 'approved':
			return self.getApproved()

		elif key == 'currentUser':
			return self.getCurrentUser()

		elif key == 'parentId':
			return self.getParentId()

		elif key == 'childrenId':
			return self.getChildrenId()

		elif key == 'copyId':
			return self.getCopyId()

		elif key == 'referenceId':
			return self.getReferenceId()

		elif key == 'assetId':
			return self.getAssetId()

		elif key == 'masterAssetId':
			return self.getMasterAssetId()

		elif key == 'dependencyId':
			return self.getDependencyId()

		elif key == 'bundleId':
			return self.getBundleId()

		elif key == 'source':
			return self.getSource()


	def getType( self ):
		'''
		Return the type of the current entity.
		'''
		return self.__class__.__name__

	def getEntityId( self ):
		'''
		Return the id of the current entity.
		'''
		return self.__entityId

	def getName( self ):
		'''
		Return the name of the current entity.
		'''
		return self.__name

	def getPath( self ):
		'''
		Return the path of the current entity.
		'''
		return self.__path

	def getVersion( self ):
		'''
		Return the version of the current entity.
		'''
		return self.__version

	def getDescriptions( self, version=None ):
		'''
		Return descriptions of the current entity.
		'''
		if version:
			return self.__descriptions[version]
		else:
			return self.__descriptions

	def getApproved( self, version=None ):
		'''
		Return approved of the current entity.
		'''
		if version:
			return self.__approved[version]
		else:
			return self.__approved

	def getCurrentUser( self ):
		'''
		Return the current user of this entity.
		'''
		return self.__currentUser

	def getParentId( self ):
		'''
		Return the id of direct parent of this entity.
		'''
		return self.__parentId

	def getChildrenId( self ):
		'''
		Return the id of the direct parent of this entity.
		'''
		return self.__childrenId

	def getCopyId( self ):
		'''
		Return the id of the entity use to do the copy of this entity.
		'''
		return self.__copyId

	def getReferenceId( self ):
		'''
		Return the id of the reference entity of this entity.
		'''
		return self.__referenceId

	def getAssetId( self ):
		'''
		Return the id of the asset where live the entity.
		'''
		return self.__assetId

	def getMasterAssetId( self ):
		'''
		Return the id of the master asset id this entity.
		This master asset is not the asset where live the entity,
		but another asset, master to the current entity.
		'''
		return self.__masterAssetId

	def getDependencyId( self ):
		'''
		Return the id of the dependencies of this entity.
		'''
		return self.__dependencyId

	def getBundleId( self ):
		'''
		Return the id of the bundles where the entity is assigned.
		'''
		return self.__bundleId

	def getSource( self, version=None ):
		'''
		Return the sources of the current entity.
		'''
		if version:
			return self.__sources[version]
		else:
			return self.__sources

	def setVersion( self, version ):
		'''
		Set the version of the current entity.
		'''
		self.__version = version
