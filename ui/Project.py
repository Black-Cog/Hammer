
import Anvil.core
import Hammer.core

class Project():
	def __init__( self, parent ):

		# defind class
		Alayout       = Anvil.core.Layout
		Abutton       = Anvil.core.Button
		Atextfield    = Anvil.core.Textfield

		# boxs init
		box_menuBar = Anvil.core.Box( name='Actions', w=150, h=400 )

		# layout init
		layout_project = Alayout( parent=parent )
		layout_menuBar = Anvil.core.Layout( parent=box_menuBar )

		# textfields init
		self.textfield_urlPath = Atextfield( text='/', w=380 )

		# actions init
		upFolder = lambda: Hammer.core.HFn.FnProject().upFolder( self )

		# buttons init
		button_up = Abutton( name='UP', cmd=upFolder, w=25, h=25 )
		button_set = Abutton( name='>', cmd=upFolder, w=25, h=25 )

		# defind layouts content
		layout_project.add( [button_up, button_set, self.textfield_urlPath] )
		layout_project.add( [ self._buildTreeEntity(), box_menuBar ] )

		# signals
		self.tree_hierarchy.signalRightClick.connect( lambda: self.menuBar(self.tree_hierarchy) )
		self.tree_hierarchy.signalLeftClick.connect( lambda: self.__addActionsToMenuBar(self.tree_hierarchy, layout_menuBar) )


	def _buildTreeEntity( self, entityId=1 ):
		entity = Hammer.getEntity( entityId )

		# todo : replace by a Forge function
		import os
		currentPath = os.path.dirname(os.path.realpath(__file__))

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
										'iconPath':'%score/icon/%s%s.png' %( currentPath.replace( '\\', '/' )[:-2], entityType[0].lower(), entityType[1:] ),
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
		self.tree_hierarchy = Anvil.core.Tree( w=450, h=400 )
		self.tree_hierarchy.add( hierarchyList )

		return self.tree_hierarchy


	def __addActionsToMenuBar( self, tree, parent ):

		entityId = tree.getCurrentItemId()
		if entityId:
			entity = Hammer.getEntity( entityId )
			actions = Hammer.getActions( entity )

			parent.clean()
			if actions:
				for action in actions:
					parent.add( Anvil.core.Button(name=action.__name__, cmd=action, w=110) )

	def menuBar( self, tree ):
		entityId = tree.getCurrentItemId()
		if entityId:
			entity = Hammer.getEntity( entityId )
			print entity.getName()
