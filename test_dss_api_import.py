import sys

sys.path.append('C:\\local_software\\HEC-DSSVue-v2.6.00.59\\jar\\sys\\jythonLib.jar\\lib')
sys.path.append('C:\\local_software\\HEC-DSSVue-v2.6.00.59\\jar\\sys\\jythonUtils.jar')
sys.path.append(r"C:\local_software\HEC-DSSVue-v4.0.00.345\jar\hec.jar")

try:
    from hec.heclib.dss import HecDss
    print 'Sucessfully found DSS API'
except:
    print 'import from DSS failed'

try:
    from mil.army.usace.hec.vortex.io import BatchImporter
    from mil.army.usace.hec.vortex import Options
    from mil.army.usace.hec.vortex.geo import WktFactory
    print 'Sucessfully found vortex API'
except:
    print 'import from vortex failed'
