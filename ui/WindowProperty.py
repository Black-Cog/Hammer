
import Anvil.core

import WindowPopup

class WindowProperty( WindowPopup.WindowPopup ):
	def __init__( self, title=None, iconPath=None, size=[ 900, 530 ], entity=None ):

		if not title:
			title = 'Property of entity : %i' %( entity['entityId'] )

		self.init( title=title, iconPath=iconPath, size=size )

		# defind class
		Atext = Anvil.core.Text

		# tabs init
		tab_main = Anvil.core.Tab(
						parent=self.window,
						tabs=[
							'Globals',
							'Versions',
							],
						)

		# layout init
		layout_globals = Anvil.core.Layout( parent=tab_main.widget(0), w=size[0], h=size[1] )
		layout_versions = Anvil.core.Layout( parent=tab_main.widget(1), w=size[0], h=size[1] )

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
		for item in propertyList:
			layout_globals.add( [
								Atext( text=item , w=size[0]*0.25 ),
								Atext( text=str(entity[item]) , w=size[0]*0.75 ),
							 ] )


		# versions init
		for version in range( len(entity['approved']) ):
			version = version + 1

			actif = 'unactif'
			if version == entity['version']:
				actif = 'actif'

			source = ''
			if entity['source']:
				source = entity['source'][version]

			layout_versions.add( [
								Atext( text='version %i : ' %(version) , w=size[0]*0.1 ),
								Atext( text=actif, w=size[0]*0.05 ),
								Atext( text=entity['descriptions'][version] , w=size[0]*0.2 ),
								Atext( text='approved : %s ' %(entity['approved'][version]) , w=size[0]*0.15 ),
								Atext( text='source : %s ' %(source) , w=size[0]*0.5 ),
								] )
