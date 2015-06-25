
import Forge.core.Process
import Anvil.core
import Hammer


class SceneContent():
	def __init__( self, parent ):

		# defind class
		Alayout       = Anvil.core.Layout

		# boxs init
		box_menuBar = Anvil.core.Box( name='Actions', w=150, h=400 )

		# layout init
		layout_sceneContent = Alayout( parent=parent )
		layout_menuBar = Alayout( parent=box_menuBar )

		# tree init
		self.tree_hierarchy = Anvil.core.Tree( w=450, h=400 )
		self._buildTreeEntity()

		# defind layouts content
		layout_sceneContent.add( [ self.tree_hierarchy, box_menuBar ] )

		# signals
		self.tree_hierarchy.signalRightClick.connect( lambda: self.menuBar(self.tree_hierarchy) )
		self.tree_hierarchy.signalLeftClick.connect( lambda: self.__addActionsToMenuBar(self.tree_hierarchy, layout_menuBar) )


	def _buildTreeEntity( self, entityId=1 ):

		hierarchyList = []

		interpreter = Forge.core.System().interpreter()

		entities = []
		if interpreter == 'maya':
			entities = Hammer.Hmaya.Actions.GetEntitiesFromScene().returnValue
		elif interpreter == 'Nuke8.0':
			entities = Hammer.Hnuke.Actions.GetEntitiesFromScene().returnValue

		for entity in entities:
			hierarchyList.append( 	{
									'name':entity['name'],
									'id':entity['entityId'],
									'iconPath':'../core/icon/%s%s.png' %( entity['entityType'][0].lower(), entity['entityType'][1:] ),
									'tooltip':'%s | entityId:%s, name:%s, assetId:%s' %( entity['entityType'], entity['entityId'], entity['name'], entity['assetId'] ),
									'iconTooltip':'type:%s' %( entity['entityType'] ),
									'parent':None,
									'parentId':None,
									} )

		# tree init
		self.tree_hierarchy.add( hierarchyList )

	def __addActionsToMenuBar( self, tree, parent ):

		entityId = tree.getCurrentItemId()
		if entityId:
			entity = Hammer.getEntity( entityId )
			actions = Hammer.getActions( entity )

			parent.clean()
			if actions:
				for action in actions:
					parent.add( Anvil.core.Button(name=action.__name__, cmd=Forge.core.Process.partial(action, entity), w=110) )

	def menuBar( self, tree ):
		entityId = tree.getCurrentItemId()
		if entityId:
			entity = Hammer.getEntity( entityId )
			print entity.getName()
