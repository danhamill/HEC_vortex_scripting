import sys
sys.path.append(r"C:\local_software\HEC-DSSVue-v4.0.00.345\jar\sys\jythonUtils.jar")
sys.path.append(r"C:\local_software\HEC-DSSVue-v4.0.00.345\jar\hec.jar")
sys.path.append(r"C:\local_software\HEC-DSSVue-v4.0.00.345\jar\jython-standalone-2.7.0.jar")

try:
    from hec.heclib.dss import HecDss
    from hec.io import TimeSeriesContainer
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

fid = HecDss.open(r'C:\workspace\git_clones\vortex_scripting\test_dss_create.dss', version=6)
fid.close()
