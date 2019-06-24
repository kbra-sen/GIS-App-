import arcpy
from arcpy import env
from arcpy.sa import *

#actıvate overwrıte
arcpy.env.overwriteOutput = True
#list of input data
PLayerHousesPoints=arcpy.GetParameterAsText(0)
LitofRasterLayers=arcpy.GetParameterAsText(1)


#extract value from multi raster layers to evler points
arcpy.gp.ExtractMultiValuesToPoints_sa(PLayerHousesPoints,LitofRasterLayers,"NONE")










