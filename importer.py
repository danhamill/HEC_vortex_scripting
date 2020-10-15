# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 15:29:16 2020

@author: RDCRLDDH
"""
from mil.army.usace.hec.vortex.io import BatchImporter
from mil.army.usace.hec.vortex import Options
from mil.army.usace.hec.vortex.geo import WktFactory
from glob import glob
in_files = glob(r"E:\Ririe_RTI_M\snodas\*_WC.dss")


clip_shp = r"E:\ririe\hms\GIS\Willow_Creek_Subbasin.shp"

geo_options = Options.create()
geo_options.add('pathToShp', clip_shp)
geo_options.add('targetCellSize', '2000')
geo_options.add('targetWkt', WktFactory.shg())

destination = r"E:\Ririe_RTI_M\snodas\clipped\RIRIE_IMPORTED_SNODAS.dss"

write_options = Options.create()
write_options.add('partF', 'SNODAAS')
write_options.add('partA', 'SHG')
write_options.add('partF', 'WILLOW CREEK')
myImport = BatchImporter.builder() \
    .inFiles(in_files) \
    .selectAllVariables() \
    .geoOptions(geo_options) \
    .destination(destination) \
    .writeOptions(write_options) \
    .build()

myImport.process()
