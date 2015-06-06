
import Anvil.core

import WindowPopup

class WindowProperty( WindowPopup.WindowPopup ):
	def __init__( self, title=None, iconPath=None, size=[ 350, 450 ], entity=None ):

		if not title:
			title = 'Property of entity : %i' %( entity['entityId'] )

		self.init( title=title, iconPath=iconPath, size=size )

		# defind class
		Atext = Anvil.core.Text
		# Abutton = Anvil.core.Button

		# layout init
		layout_main = Anvil.core.Layout( parent=self.window )

		# texts init
		propertyList = [
						'entityType',
						'name',
						'entityId',
						'path',
						'version',
						'parentId',
						'childrenId',
						'copyId',
						'referenceId',
						'assetId',
						'masterAssetId',
						'dependencyId',
						'bundleId',
						'source',
					   ]

		for item in propertyList:
			
			layout_main.add( [
								Atext( text=item , w=size[0]/2 ),
								Atext( text=str(entity[item]) , w=size[0]/2 ),
							 ] )
