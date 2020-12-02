import sys
sys.path.append(r"C:\local_software\HEC-DSSVue-v4.0.00.345\jar\sys\jythonUtils.jar")
sys.path.append(r"C:\local_software\HEC-DSSVue-v4.0.00.345\jar\hec.jar")
sys.path.append(r"C:\local_software\HEC-DSSVue-v4.0.00.345\jar\jython-standalone-2.7.0.jar")
sys.path.append(r"C:\local_software\HEC-DSSVue-v4.0.00.345\jar\hec-dssvue-dev.jar")
sys.path.append(r"C:\local_software\HEC-DSSVue-v4.0.00.345\jar\rma.jar")

try:
    from hec.heclib.dss import HecDss
    from hec.io import TimeSeriesContainer
    print 'Sucessfully found DSS API'
except:
    print 'import from DSS failed'

import os
from glob import glob



files = glob(r"G:\UA\*.nc")

for file in files:

    root, name = os.path.split(file)

    dss_file  = root + os.sep + name[:-2] + 'dss'
    fid = HecDss.open(dss_file,6)
    fid.close()
    del fid
