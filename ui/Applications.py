
import Anvil.core
import Forge.core

class Applications():
	def __init__( self, parent ):

		# defind class
		Alayout = Anvil.core.Layout
		Abutton = Anvil.core.Button

		# layout init
		layout_user = Alayout( parent=parent )

		# actions init
		launchMaya = Forge.core.Process.partial( Forge.core.Process.launchSoftware, 'c:/Program Files/Autodesk/Maya2015/bin/maya.exe' )
		launchNuke = Forge.core.Process.partial( Forge.core.Process.launchSoftware, 'c:/Program Files/Nuke8.0v3/Nuke8.0.exe' )
		launchCoal = Forge.core.Process.partial( Forge.core.Process.launchSoftware, 'c:/Python27/python.exe', 'f:/software/coal_0.0.0.1dev/Coal/bin/launchCoal.py' )
		launchBcconverter = Forge.core.Process.partial( Forge.core.Process.launchSoftware, 'c:/Python27/python.exe', 'f:/software/BCconverter_0.0.0.1dev/BCconverter/bin/launchBCconverter.py' )

		# buttons init
		button_maya = Abutton( name='', cmd=launchMaya, h=128, w=128, icon='../core/icon/mayaApp128.png', iconSize=[128,128] )
		button_nuke = Abutton( name='', cmd=launchNuke, h=128, w=128, icon='../core/icon/nukeApp128.png', iconSize=[128,128] )
		button_coal = Abutton( name='', cmd=launchCoal, h=128, w=128, icon='../core/icon/coalApp128.png', iconSize=[128,128] )
		button_bcconverter = Abutton( name='', cmd=launchBcconverter, h=128, w=128, icon='../core/icon/bcconverterApp128.png', iconSize=[128,128] )

		# defind layouts content
		layout_user.add( [button_maya, button_nuke, button_coal, button_bcconverter] )
