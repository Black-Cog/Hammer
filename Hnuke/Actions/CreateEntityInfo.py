
import Hammer.core.Actions.BaseAction

class CreateEntityInfo( Hammer.core.Actions.BaseAction ):

	def _doAction( self, entity, arg, ui ):

		import nuke

		entityInfo = nuke.createNode( "StickyNote" )
		entityInfo.setName( 'entityInfo' )

		entityInfo.knob('label').setValue( 'entityInfo' )
		entityInfo.knob('note_font').setValue( 'Arial Black Bold' )
		entityInfo.knob('note_font_size').setValue( 30 )
		entityInfo.knob('tile_color').setValue( 0x7f00ff )

		entityType = nuke.String_Knob("entityType", "entityType")
		entityType.setValue( entity['entityType'] )
		entityInfo.addKnob( entityType )

		entityId = nuke.Int_Knob("entityId", "entityId")
		entityId.setValue( entity['entityId'] )
		entityInfo.addKnob( entityId )

		entityVersion = nuke.Int_Knob("entityVersion", "entityVersion")
		entityVersion.setValue( entity['version'] )
		entityInfo.addKnob( entityVersion )

		entityName = nuke.String_Knob("entityName", "entityName")
		entityName.setValue( entity['name'] )
		entityInfo.addKnob( entityName )
