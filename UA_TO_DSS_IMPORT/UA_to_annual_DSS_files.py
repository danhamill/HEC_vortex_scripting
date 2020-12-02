
from mil.army.usace.hec.vortex.io import BatchImporter
from mil.army.usace.hec.vortex import Options
from mil.army.usace.hec.vortex.geo import WktFactory
import os
from glob import glob

d_files = glob(r"G:\UA\*.dss")
ua_files = glob(r"G:\UA\*.nc")
for dss_file, ua_file in zip(d_files, ua_files):

    clip_shp = r"C:\workspace\Mo River\shp\MissouriRiverBasin_alb.shp"
    variables = ['SWE']
    basin = 'MISSOURI RIVER BASIN'
    ds = 'UA'

    geo_options = Options.create()
    geo_options.add('pathToShp', clip_shp)
    geo_options.add('targetCellSize', '2000')
    geo_options.add('targetWkt', WktFactory.shg())
    geo_options.add('resamplingMethod', 'Bilinear')

    destination = dss_file

    write_options = Options.create()
    write_options.add('partF', ds)
    write_options.add('partA', 'SHG')
    write_options.add('partB', basin)
    myImport = BatchImporter.builder().inFiles([ua_file]).variables(variables).geoOptions(geo_options).destination(destination).writeOptions(write_options).build()
    myImport.process() 