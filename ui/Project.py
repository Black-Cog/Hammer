
import Forge.core.Process
import Anvil.core
import Hammer


class Project():
	def __init__( self, parent ):

		# defind class
		Alayout    = Anvil.core.Layout
		Abutton    = Anvil.core.Button
		Atextfield = Anvil.core.Textfield

		# boxs init
		box_menuBar = Anvil.core.Box( name='Actions', w=150, h=400 )

		# layout init
		layout_project = Alayout( parent=parent )
		layout_menuBar = Anvil.core.Layout( parent=box_menuBar )

		# textfields init
		self.textfield_urlPath = Atextfield( text='/', w=380 )

		# buttons init
		button_up = Abutton(
							name='',
							cmd=Forge.core.Process.partial( Hammer.core.HFn.FnProject().upFolder, self ),
							w=25,
							h=25,
							icon='../core/icon/up.png',
							iconSize=[25, 25],
							)
		button_set = Abutton(
							name='',
							cmd=self._buildTreeEntity,
							w=25,
							h=25,
							icon='../core/icon/refresh.png',
							iconSize=[25, 25],
							)

		# tree init
		self.tree_hierarchy = Anvil.core.Tree( w=450, h=400 )
		self._buildTreeEntity()

		# defind layouts content
		layout_project.add( [button_up, button_set, self.textfield_urlPath] )
		layout_project.add( [ self.tree_hierarchy, box_menuBar ] )

		# signals
		self.tree_hierarchy.signalRightClick.connect( Forge.core.Process.partial(self.menuBar, self.tree_hierarchy) )
		self.tree_hierarchy.signalLeftClick.connect( Forge.core.Process.partial(self.__addActionsToMenuBar, self.tree_hierarchy, layout_menuBar) )


	def _buildTreeEntity( self, entityIdOverride=False ):

		if not entityIdOverride:
			self._currentEntityId = self.__getEntityIdFromPath()

		entity = Hammer.getEntity( self._currentEntityId )

		hierarchyList = []

		def setHierarchyList( childrenIds, parentId ):
			for childrenId in childrenIds:
				child = Hammer.getEntity( childrenId )
				entityType = child.getType()

				parent = None
				if parentId:
					parent = Hammer.getEntity( parentId ).getName()

				hierarchyList.append( 	{
										'name':child.getName(),
										'id':childrenId,
										'iconPath':'../core/icon/%s%s.png' %( entityType[0].lower(), entityType[1:] ),
										'tooltip':'%s | entityId:%s, name:%s, assetId:%s' %( child.getType(), child.getEntityId(), child.getName(), child.getAssetId() ),
										'iconTooltip':'type:%s' %( child.getType() ),
										'parent':parent,
										'parentId':parentId,
										} )

				subChildren = child.getChildrenId()
				child.getParentId()
				if subChildren:
					setHierarchyList( subChildren, childrenId )

		setHierarchyList( entity.getChildrenId(), None )

		# tree init
		self.tree_hierarchy.add( hierarchyList )

	def __getEntityIdFromPath( self ):

		path = self.textfield_urlPath.getValue()

		folders = []
		for folder in path.split( '/' ):
			if folder:
				folders.append( folder )

		def checkMatch( entityId, name ):
			childrenIds = Hammer.getEntity( entityId ).getChildrenId()
			for childrenId in childrenIds:
				if Hammer.getEntity( childrenId ).getName() == name:
					return childrenId
			return None

		entityId = 1
		newPath = '/'
		for folder in folders:
			if entityId:
				newEntityId = entityId
				entityId = checkMatch( entityId, folder )

				if entityId:
					newPath += '%s/' %( folder )
				else:
					entityId = newEntityId
					break

		self.textfield_urlPath.setValue( newPath )

		return entityId

	def __addActionsToMenuBar( self, tree, parent ):
		'''
		Build actions menu
		'''

		entityId = tree.getCurrentItemId()
		if entityId:
			entity = Hammer.getEntity( entityId )
			actions = Hammer.getActions( entity )
			arg = {}

			parent.clean()
			if actions:
				for action in actions:
					parent.add( Anvil.core.Button(name=action.__name__, cmd=Forge.core.Process.partial( action, entity, arg, self ), w=110) )

	def menuBar( self, tree ):
		entityId = tree.getCurrentItemId()
		if entityId:
			entity = Hammer.getEntity( entityId )
			print entity.getName()
