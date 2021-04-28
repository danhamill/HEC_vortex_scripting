from mil.army.usace.hec.vortex.convert import GridToPointConverter
from mil.army.usace.hec.vortex import Options
from mil.army.usace.hec.vortex.io import DataReader
import os
from glob import glob
from java.nio.file import Path
from java.nio.file import Paths

d_files = glob(r"G:\UA\*_noData.dss")
output_dss = Paths.get(r"G:\UA\ts\UA_SWE_Depth_MoRiverBasin.dss")
clip_shp = Paths.get("C:\workspace\Mo River\shp\MissouriRiverBasin_alb.shp")

for dss_file in d_files:

    sourceGrids = DataReader.getVariables(dss_file)
    basin = 'MISSOURI RIVER BASIN'
    ds = 'UA_sanitized'

    
    write_options = Options.create()
    write_options.add('partF', ds )
    write_options.add('partA', 'SHG')
    write_options.add('partB', basin)
    myImport = GridToPointConverter.builder()\
            .pathToGrids(dss_file)\
            .variables(sourceGrids)\
            .pathToFeatures(clip_shp)\
            .field('NAME')\
            .destination(output_dss)\
            .writeOptions(write_options).build()
    myImport.convert() 

d_files = glob(r"G:\UA\*.dss")[::2]

for dss_file in d_files:

    basin = 'MISSOURI RIVER BASIN'
    ds = 'UA_raw'
    sourceGrids = DataReader.getVariables(dss_file)
    write_options = Options.create()
    write_options.add('partF', ds )
    write_options.add('partA', 'SHG')
    write_options.add('partB', basin)
    myImport = GridToPointConverter.builder() \
            .pathToGrids(dss_file) \
            .variables(sourceGrids)\
            .pathToFeatures(clip_shp) \
            .field('NAME') \
            .destination(output_dss) \
            .writeOptions(write_options).build()
    myImport.convert() 