import arcpy
from arcpy import env
from arcpy.sa import *


#set variables
target_featuresPolygonHouses=arcpy.GetParameterAsText(0)
join_PointHouses=arcpy.GetParameterAsText(1)
out_feature_class=arcpy.GetParameterAsText(2)

# The following inputs are layers or table views: "evler", "pointevler"
# Point -> polygon(for real)

arcpy.SpatialJoin_analysis(target_featuresPolygonHouses, join_PointHouses, out_feature_class)




