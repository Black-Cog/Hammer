
# import maya

class Modeling():
	"""docstring for Modeling"""

	@staticmethod
	def verification():
		import maya
		errorList = {'error':[], 'hole':[]}

		for mesh in maya.cmds.ls( type='mesh' ):
			meshError = False
			meshHole  = False

			for i in range( maya.cmds.polyEvaluate(mesh, edge=True) ):
				faceCount = 0
				infoFace  = maya.cmds.polyListComponentConversion( '%s.e[%i]' %(mesh, i), tf=True )

				for j in infoFace:
					faceCount += 1
					if ':' in j:
						tmp = eval( j.split('f')[1].replace( ':', ',') )
						faceCount += tmp[1] - tmp[0]

				if faceCount > 2 : meshError = True
				if faceCount < 2 : meshHole = True

			if meshError : errorList['error'].append( mesh )
			if meshHole  : errorList['hole'].append( mesh )

		for i in errorList['error'] : print 'Modeling error on %s' %( i )
		for i in errorList['hole'] : print 'Hole on %s' %( i )

	@staticmethod
	def publish():
		import maya
		out = 'F:/test/obj/outPublish/modPrint/'

		for mesh in maya.cmds.ls( type='mesh' ):
			transform = maya.cmds.listRelatives( mesh, p=True )[0]

			maya.cmds.select( transform )
			maya.cmds.file( '%s%s.obj' %(out, transform), force=True, options='groups=1;ptgroups=1;materials=0;smoothing=1;normals=1', type="OBJexport", es=True )

# Modeling().verification()
# Modeling().publish()
