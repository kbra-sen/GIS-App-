import arcpy
from arcpy import env
from arcpy.sa import *

#actıvate overwrıte
arcpy.env.overwriteOutput = True

#list of input data
IHistoricalHouses=arcpy.GetParameterAsText(0)
ICityCenter=arcpy.GetParameterAsText(1)
IStation=arcpy.GetParameterAsText(2)
IPoliceCenter=arcpy.GetParameterAsText(3)
IBank=arcpy.GetParameterAsText(4)
IHotel=arcpy.GetParameterAsText(5)

arcpy.env.mask =arcpy.GetParameterAsText(6)
arcpy.env.extent =arcpy.GetParameterAsText(7)


ODistanceCenter = arcpy.GetParameterAsText(8)
ODistanceStation = arcpy.GetParameterAsText(9)
ODistancePolice = arcpy.GetParameterAsText(10)
ODistanceBank = arcpy.GetParameterAsText(11)
ODistanceHotel = arcpy.GetParameterAsText(12)
OPointsOfEvler = arcpy.GetParameterAsText(13)


#make layer for distance from city center
arcpy.gp.EucDistance_sa(ICityCenter, ODistanceCenter , "", 15, "")

#make layer for distance from Station
arcpy.gp.EucDistance_sa(IStation, ODistanceStation , "", 15, "")


#make layer for distance from PoliceCenter
arcpy.gp.EucDistance_sa(IPoliceCenter, ODistancePolice, "", 15, "")


#make layer for distance from Bank
arcpy.gp.EucDistance_sa(IBank, ODistanceBank, "", 15, "")

#make layer for distance from Hotel
arcpy.gp.EucDistance_sa(IHotel, ODistanceHotel, "", 15, "")

#Convert Evler to Points
PointLayer = arcpy.FeatureToPoint_management(IHistoricalHouses, OPointsOfEvler, point_location="CENTROID")


