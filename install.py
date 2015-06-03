import subprocess
import shlex
import os
import sys
import shutil


softwareEnvironment = 'f:/software/'

FORGE_VERSION = '0.0.0.1dev'
ANVIL_VERSION = '0.0.0.1dev'

forgePath  = '%sforge_%s' %( softwareEnvironment, FORGE_VERSION )
anvilPath  = '%sanvil_%s' %( softwareEnvironment, ANVIL_VERSION )
parentPath = '/'.join( sys.path[0].replace('\\', '/').split('/')[:-1] )

envs = [ forgePath, anvilPath, parentPath ]
for env in envs:
	sys.path.append( env )

import Forge
import Hammer


###############################################################################################
# Version
###############################################################################################


coalMilestoneVersion = 0 # for announcing major milestones - may contain all of the below
coalMajorVersion     = 0 # backwards-incompatible changes
coalMinorVersion     = 0 # new backwards-compatible features
coalPatchVersion     = 1 # bug fixes


###############################################################################################
# Environment
###############################################################################################


softwareEnvironment = 'f:/software/'
softwareName = 'hammer_%s.%s.%s.%sdev/%s' %( coalMilestoneVersion, coalMajorVersion, coalMinorVersion, coalPatchVersion, 'Hammer' )
softwarePath = '%s%s/' %( softwareEnvironment, softwareName )


###############################################################################################
# Folder creation
###############################################################################################


curentPath = os.path.dirname(os.path.realpath(__file__))
binDir              = 'bin'
coreDir             = 'core'
coreEntityTypeDir   = 'core/EntityType'
coreIconDir         = 'core/icon'
corePythonHammerDir = 'core/python/Hammer'
coreMayaActionsDir  = 'maya/actions'
uiDir               = 'ui'

Fsystem = Forge.core.System()

for folder in 	[
					coreDir,
					uiDir,
					binDir,
					coreEntityTypeDir,
					coreIconDir,
					corePythonHammerDir,
					coreMayaActionsDir,
				]:
	Fsystem.mkdir( '%s%s' %(softwarePath, folder) )

###############################################################################################
# Moving compiles files
###############################################################################################


print '>>> Install Begin'

for folder in 	[
					curentPath,
					coreDir,
					uiDir,
					binDir,
					coreEntityTypeDir,
					coreIconDir,
					corePythonHammerDir,
					coreMayaActionsDir,
				]:
	for file in os.listdir( folder ):
		currentFile = '%s/%s' %( folder, file )
		newFile = '%s%s/%s' %( softwarePath, folder, file )

		if folder == binDir:
			shutil.copy( currentFile, newFile )
			print '>>>   "%s" is well compiled.' %( newFile )
		else:
			if '.pyc' in file:
				if folder == curentPath:
					newFile = '%s/%s' %( softwarePath, file )

				if os.path.exists( newFile ):
					os.remove( newFile )

				os.rename( currentFile, newFile )
				print '>>>   "%s" is well compiled.' %( newFile )

			elif '.png' in file:
				if folder == curentPath:
					newFile = '%s/%s' %( softwarePath, file )

				# os.rename( currentFile, newFile )
				shutil.copy(currentFile, newFile)
				print '>>>   "%s" is well copy.' %( newFile )

			elif file == 'db':
				if folder == curentPath:
					newFile = '%s/%s' %( softwarePath, file )

				shutil.copy(currentFile, newFile)
				# os.rename( currentFile, newFile )
				print '>>>   "%s" is well copy.' %( newFile )


print '>>> Install End'
