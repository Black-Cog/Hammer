
import Anvil.core
import Forge.core

class Applications():
	def __init__( self, parent ):

		# defind class
		Alayout = Anvil.core.Layout
		Abutton = Anvil.core.Button
		env = Forge.core.Env()

		# layout init
		layout_user = Alayout( parent=parent )

		# actions init
		launchMaya = Forge.core.Process.partial( Forge.core.Process.launchSoftware, env.maya )
		launchNuke = Forge.core.Process.partial( Forge.core.Process.launchSoftware, env.nuke )
		launchCoal = Forge.core.Process.partial( Forge.core.Process.launchSoftware, env.python, env.coal )
		launchBcconverter = Forge.core.Process.partial( Forge.core.Process.launchSoftware, env.python, env.bcconverter )

		# buttons init
		button_maya = Abutton( name='', cmd=launchMaya, h=128, w=128, icon='../core/icon/mayaApp128.png', iconSize=[128,128] )
		button_nuke = Abutton( name='', cmd=launchNuke, h=128, w=128, icon='../core/icon/nukeApp128.png', iconSize=[128,128] )
		button_coal = Abutton( name='', cmd=launchCoal, h=128, w=128, icon='../core/icon/coalApp128.png', iconSize=[128,128] )
		button_bcconverter = Abutton( name='', cmd=launchBcconverter, h=128, w=128, icon='../core/icon/bcconverterApp128.png', iconSize=[128,128] )

		# defind layouts content
		layout_user.add( [button_maya, button_nuke, button_coal, button_bcconverter] )
