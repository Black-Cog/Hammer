
import Hammer.core.Actions

class FnBaseEntity():

	def initFn( self ):
		self._fn = 	[
					self.property,
					self.delete,
					self.rename,
					]

	def property( self, entity, arg, ui ):
		self.baseEntityProperty = Hammer.core.Actions.BaseEntityProperty( window=True, entity=entity, arg=arg, ui=ui )

	def delete( self, entity, arg, ui ):
		self.baseEntitydelete = Hammer.core.Actions.BaseEntityDelete( window=True, entity=entity, arg=arg, ui=ui )

	def rename( self, entity, arg, ui ):
		print 'rename : %s' %( str(entity) )
