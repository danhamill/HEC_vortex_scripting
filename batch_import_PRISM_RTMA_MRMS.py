# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 15:29:16 2020

@author: RDCRLDDH
"""
from mil.army.usace.hec.vortex.io import BatchImporter
from mil.army.usace.hec.vortex import Options
from mil.army.usace.hec.vortex.geo import WktFactory
from glob import glob
import os

shps ={'NORTH PLATTE':r"C:\workspace\Post-Wildfire\shp\Watersheds\huc4_northPlatte_ALB.shp",
        'SOUTH PLATTE':r"C:\workspace\Post-Wildfire\shp\Watersheds\huc4_southPlatte_ALB.shp",
        'WILLAMETTE':r"C:\workspace\Post-Wildfire\shp\Watersheds\huc4_willamette_ALB.shp"}

prism = {16:r"G:\PRISM\WY_2016_PRISM",
        17:r"G:\PRISM\WY_2017_PRISM",
        18:r"G:\PRISM\WY_2018_PRISM",
        19:r"G:\PRISM\WY_2019_PRISM",
        20:r"G:\PRISM\WY_2020_PRISM"}

mrms = {16:r"G:\MRMS\precip\2016",
        17:r"G:\MRMS\precip\2017",
        18:r"G:\MRMS\precip\2018",
        19:r"G:\MRMS\precip\2019",
        20:r"G:\MRMS\precip\2020"}

rtma = {16:r'G:\RTMA\Temp\2016',
        17:r'G:\RTMA\Temp\2017',
        18:r'G:\RTMA\Temp\2018',
        19:r'G:\RTMA\Temp\2019',
        20:r'G:\RTMA\Temp\2020'}

var_names = {'RTMA':'Temperature_height_above_ground',
             'MRMS':'GaugeCorrQPE01H_altitude_above_msl',
             'PRISM':'ppt'}

exts = {'RTMA':'*.grib2',
        'MRMS':'*.grib2',
        'PRISM':'*_*_stable_*_*.bil',}

for wy in [16,17,18,19,20]:
    print 'Now Processing Water Year ' + str(wy)
    for basin in ['NORTH PLATTE','SOUTH PLATTE', 'WILLAMETTE']:
        print 'Now Processing basin ' + basin
        clip_shp = shps[basin]
        if os.path.exists(clip_shp):
            print 'Found Shapefile'
        for ds, files in zip(['PRISM','MRMS','RTMA'][1:2], [prism,mrms,rtma][1:2]):
            print 'Now processing ' + ds + ' files'
            dss_file = r"C:\workspace\Post-Wildfire\dss" + os.sep + ds + os.sep + '_'.join([basin, 'WY'+str(wy), ds])+ ".dss"
            if os.path.exists(dss_file):
                print 'Found DSS File'
            in_files = glob(files[wy] + os.sep + exts[ds])
            print 'Found' + ' ' + str(len(in_files)) + ' Files'
            variables = [var_names[ds]]

            geo_options = Options.create()
            geo_options.add('pathToShp', clip_shp)
            geo_options.add('targetCellSize', '2000')
            geo_options.add('targetWkt', WktFactory.shg())
            geo_options.add('resamplingMethod', 'bilinear')

            destination = dss_file

            write_options = Options.create()
            write_options.add('partF', ds)
            write_options.add('partA', 'SHG')
            write_options.add('partB', basin)
            myImport = BatchImporter.builder().inFiles(in_files).variables(variables).geoOptions(geo_options).destination(destination).writeOptions(write_options).build()

            myImport.process()
