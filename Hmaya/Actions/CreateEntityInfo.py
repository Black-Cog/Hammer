
import Hammer.core.Actions.BaseAction

class CreateEntityInfo( Hammer.core.Actions.BaseAction ):

	def _doAction( self, entity, arg, ui ):

		import maya.cmds

		maya.cmds.group( em=True, name='|entityInfo' )
		maya.cmds.setAttr( "|entityInfo.visibility", 0 )

		maya.cmds.addAttr( '|entityInfo', longName='entityType', dt='string' )
		maya.cmds.setAttr( "|entityInfo.entityType", entity['entityType'], type='string' )
		maya.cmds.setAttr( "|entityInfo.entityType", lock=True )

		maya.cmds.addAttr( '|entityInfo', longName='entityId', at='long' ,defaultValue=entity['entityId'] )
		maya.cmds.setAttr( "|entityInfo.entityId", lock=True )

		maya.cmds.addAttr( '|entityInfo', longName='entityVersion', at='long' ,defaultValue=entity['version'] )
		maya.cmds.setAttr( "|entityInfo.entityVersion", lock=True )

		maya.cmds.addAttr( '|entityInfo', longName='entityName', dt='string' )
		maya.cmds.setAttr( "|entityInfo.entityName", entity['name'], type='string' )
		maya.cmds.setAttr( "|entityInfo.entityName", lock=True )

		maya.cmds.select(d=True)
