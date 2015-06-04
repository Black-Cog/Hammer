
class FnBaseEntity():

	def initFn( self ):
		self._fn = 	[
					self.property,
					self.delete,
					self.rename,
					]

	def property( self ):
		print 'property'

	def delete( self ):
		print 'delete'

	def rename( self ):
		print 'rename'
