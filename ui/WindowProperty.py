
import Forge.core.Process
import Anvil.core
import Hammer

import WindowPopup

class WindowProperty( WindowPopup.WindowPopup ):
	def __init__( self, title=None, iconPath=None, size=[ 700, 530 ], entity=None ):

		if not title:
			title = 'Property of entity : %i' %( entity['entityId'] )

		self.init( title=title, iconPath=iconPath, size=size )

		version = False
		if len( entity['approved'] ) > 0:
			version = True

		tabList = [ 'Globals' ]
		if version:
			tabList.append( 'Versions' )

		# tabs init
		tab_main = Anvil.core.Tab(
						parent=self.window,
						tabs=tabList,
						)

		# layout init
		_Globals( parent=tab_main.widget(0), entity=entity, size=size )
		if version:
			_Version( parent=tab_main.widget(1), entity=entity, size=size )


class _Globals():
	def __init__( self, parent, entity, size ):

		# defind class
		Atext = Anvil.core.Text

		# globals init
		propertyList = [
						'entityType',
						'name',
						'entityId',
						'path',
						'version',
						'currentUser',
						'parentId',
						'childrenId',
						'copyId',
						'referenceId',
						'assetId',
						'masterAssetId',
						'dependencyId',
						'bundleId',
						]

		layout_globals = Anvil.core.Layout( parent=parent )

		for item in propertyList:
			layout_globals.add( [
								Atext( text=item , w=size[0]*0.25 ),
								Atext( text=str(entity[item]) , w=size[0]*0.75 ),
							 ] )

class _Version():
	def __init__( self, parent, entity, size ):

		# defind class
		Alayout = Anvil.core.Layout

		# boxs init
		box_menuBar = Anvil.core.Box( name='Actions', w=size[0]*0.25-20, h=size[1]-20 )

		# layout init
		layout_sceneContent = Alayout( parent=parent, w=size[0], h=size[1] )
		layout_menuBar = Alayout( parent=box_menuBar )

		# buttons init
		button_refresh = Anvil.core.Button(
							name='',
							cmd=Forge.core.Process.partial( self._buildTreeEntity, entity['entityId'] ),
							w=25,
							h=25,
							icon='../core/icon/refresh.png',
							iconSize=[25, 25],
							)

		# tree init
		self.tree_hierarchy = Anvil.core.Tree( w=size[0]*0.75-20, h=size[1]-20 )
		self._buildTreeEntity( entityId=entity['entityId'] )

		# defind layouts content
		layout_sceneContent.add( button_refresh )
		layout_sceneContent.add( [ self.tree_hierarchy, box_menuBar ] )

		# signals
		self.tree_hierarchy.signalRightClick.connect( Forge.core.Process.partial(self.menuBar, self.tree_hierarchy) )
		self.tree_hierarchy.signalLeftClick.connect( Forge.core.Process.partial(self.__addActionsToMenuBar, self.tree_hierarchy, layout_menuBar) )


	def _buildTreeEntity( self, entityId ):

		entity = Hammer.getEntity( entityId )

		hierarchyList = []

		# versions init
		for version in range( len(entity['approved']) ):
			version = version + 1

			if entity['approved'][version]:
				iconType = 'approved'
			else:
				iconType = 'unapproved'

			if version == entity['version']:
				iconType += 'Actif'

			source = ''
			if entity['source']:
				source = entity['source'][version]


			hierarchyList.append( 	{
									'name':' %i : %s' %( version, entity['descriptions'][version] ),
									'id':entity['entityId'],
									'iconPath':'../core/icon/%s.png' %( iconType ),
									'tooltip':'source : %s ' %(source),
									'iconTooltip':'',
									'parent':None,
									'parentId':None,
									} )


		# tree init
		self.tree_hierarchy.add( hierarchyList )

	def __addActionsToMenuBar( self, tree, parent ):

		entityId = tree.getCurrentItemId()
		itemName = tree.getCurrentItemName()
		version = eval( itemName.split( ':' )[0] )

		if entityId:
			entity = Hammer.getEntity( entityId )
			entity.setVersion( version=version )
			actions = Hammer.getActions( entity, 'Version' )
			actions += Hammer.getActions( entity )
			arg = {}

			parent.clean()
			if actions:
				for action in actions:
					if action.__name__ in [ 'approved', 'setCurrent', 'openScene', 'openSourceScene', 'get' ]:
						parent.add( Anvil.core.Button(name=action.__name__, cmd=Forge.core.Process.partial( action, entity, arg, self ), w=110) )

	def menuBar( self, tree ):
		entityId = tree.getCurrentItemId()
		if entityId:
			entity = Hammer.getEntity( entityId )
			print entity.getName()


