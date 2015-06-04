
class FnBaseEntity():

	def initFn( self ):
		self._fn = 	[
					self.property,
					self.delete,
					self.rename,
					]

	def property( self, entity ):
		print 'property : %s' %( str(entity) )

	def delete( self, entity ):
		print 'delete : %s' %( str(entity) )

	def rename( self, entity ):
		print 'rename : %s' %( str(entity) )
