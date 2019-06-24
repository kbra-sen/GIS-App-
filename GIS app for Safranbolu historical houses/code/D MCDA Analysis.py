import arcpy
from arcpy import env
from arcpy.sa import *


#set variables
inFeatures =arcpy.GetParameterAsText(0)
fieldName1 =arcpy.GetParameterAsText(1)
fieldPrecision =9
fieldAlias =fieldName1
fieldLength=10


#execute AddField
arcpy.AddField_management(inFeatures,fieldName1,"FLOAT",
                          fieldPrecision,field_alias=fieldAlias,field_is_nullable="NULLABLE")

#execute AddField
inTable=inFeatures
fieldName=fieldName1


expression=arcpy.GetParameterAsText(2)
arcpy.CalculateField_management(inTable,fieldName,expression,"VB","")















