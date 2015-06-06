
import Hammer.core.Actions

class FnBaseEntity():

	def initFn( self ):
		self._fn = 	[
					self.property,
					self.delete,
					self.rename,
					]

	def property( self, entity ):
		self.baseEntityProperty = Hammer.core.Actions.BaseEntityProperty( ui=True, entity=entity )

	def delete( self, entity ):
		self.baseEntityProperty = Hammer.core.Actions.BaseEntityDelete( ui=True, entity=entity )

	def rename( self, entity ):
		print 'rename : %s' %( str(entity) )
