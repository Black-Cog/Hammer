import sys
import Forge.core

class FnUser(object):
	"""docstring for FnUser"""
	
	@staticmethod
	def logUser(login=None, password=None):
		"""docstring for logUser"""
		'@parameter string login User login.'
		'@parameter string password User password'

		database = Forge.core.Database()
		database.connection('localhost', 'root', '', 'bc_forge')
		conditionData = [login, password]
		queryList = database.select('*', 'users', 'user_name=%s AND password=PASSWORD(%s)', conditionData)
		result = "false"
		if len(queryList)==1: 
			result = queryList #Transmition of the user data

			# Update of the last_log date
			logDate = [["last_logged", "NOW()", None]]
			upCondition = "ID = %d" %float(result[0][0])
			database.update( logDate, 'users', upCondition)

		database.close() #Connection end
		return result

	def log( self, arg ):
		login    = arg.login.textfield_login.text()
		password = arg.login.textfield_password.text()

		if login and password:
			if self.checkLogin( login=login, password=password ) :
				message  = 'login success'
				arg.ui()
			else : message = 'login failed'
		else : message = 'Login or/and password are empty.'

		# feedback text
		arg.login.text_feedback.setText( message )

	@staticmethod
	def checkLogin( login, password ):
		# mysql call here
		# fake value
		loginArray    = ['toto', 'tata', 'clipo', 'cedric', 'sebastien']
		passwordArray = ['toto', 'tata', 'clipo', 'sebastien', 'cedric']
		check = False

		if login in loginArray:
			index = loginArray.index( login )
			if password == passwordArray[ index ] : check = True

		return check

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
