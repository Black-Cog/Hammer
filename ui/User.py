
import Anvil.core
import Hammer.core

class User():
	def __init__( self, parent ):

		# defind class
		Alayout       = Anvil.core.Layout
		Atext         = Anvil.core.Text
		Abutton       = Anvil.core.Button

		fnUser        = Hammer.core.HFn.FnUser()
		userActions = Hammer.core.Actions.UserActions()

		# layout init
		layout_user = Alayout( parent=parent )

		# texts init
		text_user          = Atext( text=fnUser.getUserName(),      w=200 )
		text_hours         = Atext( text=fnUser.getMonthlyHours(),  w=200 )
		text_timeOnProd    = Atext( text=fnUser.getTimeOnProd(),    w=200 )
		text_contractBegin = Atext( text=fnUser.getContractBegin(), w=200 )
		text_contractEnd   = Atext( text=fnUser.getContractEnd(),   w=200 )
		text_supervisor    = Atext( text=fnUser.getSupervisor(),    w=200 )

		# buttons init
		button_mail = Abutton( name='Mail', cmd=userActions.mail )

		# defind layouts content
		layout_user.add( text_user )
		layout_user.add( text_hours )
		layout_user.add( text_timeOnProd )
		layout_user.add( text_contractBegin )
		layout_user.add( text_contractEnd )
		layout_user.add( text_supervisor )

		layout_user.add( button_mail )
