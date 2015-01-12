
# import Forge

class FnUser():
	"""docstring for FnUser"""
	
	@staticmethod
	def getUserName():
		# Fdatabase = Forge.core.Database()
		# username = Fdatabase.select()
		# return username
		return 'User               : %s' %( 'Launay Cedric' )
	
	@staticmethod
	def getMonthlyHours():
		return 'Hours this month   : %s' %( '85 hrs' )
	
	@staticmethod
	def getTimeOnProd():
		return 'Days on production : %s' %( '185 days' )
	
	@staticmethod
	def getContractBegin():
		return 'Contract start     : %s' %( 'November 17, 2014' )
	
	@staticmethod
	def getContractEnd():
		return 'Contract finish    : %s' %( 'November 20, 2015' )
	
	@staticmethod
	def getSupervisor():
		return 'Supervisor         : %s' %( 'Dupont Martin' )
