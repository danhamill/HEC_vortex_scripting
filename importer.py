# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 15:29:16 2020

@author: RDCRLDDH
"""
from mil.army.usace.hec.vortex.io import BatchImporter
from mil.army.usace.hec.vortex import Options
from mil.army.usace.hec.vortex.geo import WktFactory
from glob import glob

in_files = glob(r"G:\PRISM\WY_2016_PRISM\*.bil")
variables = ['ppt']
clip_shp = r"C:\workspace\Post-Wildfire\shp\Watersheds\poudre_alb.shp"

geo_options = Options.create()
geo_options.add('pathToShp', clip_shp)
geo_options.add('targetCellSize', '2000')
geo_options.add('targetWkt', WktFactory.shg())

destination = r"C:\workspace\Post-Wildfire\dss\PRISM\POUDRE_WY16_PRISM.dss"

write_options = Options.create()
write_options.add('partF', 'PRISM')
write_options.add('partA', 'SHG')
write_options.add('partB', 'CACHE LA POUDRE')
myImport = BatchImporter.builder() \
    .inFiles(in_files) \
    .variables(variables) \
    .geoOptions(geo_options) \
    .destination(destination) \
    .writeOptions(write_options) \
    .build()

myImport.process()
