set "DSS_HOME=C:\local_software\HEC-DSSVue-v4.0.00.345"
set "PATH=%DSS_HOME%\jar;%PATH%"
set "CLASSPATH=%DSS_HOME%\jar\sys\jythonLib.jar\lib*"


C:\jython2.7.2\bin\jython.exe -Djava.library.path=%DSS_HOME%\lib "C:\workspace\git_clones\vortex_scripting\test_dss_api_import.py"
cmd /k
