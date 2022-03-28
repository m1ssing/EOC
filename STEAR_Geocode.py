import arcpy
import arcgis
import os


stuff = arcpy.GetActivePortalURL()
print(stuff)
pointLayer = "\\\\GISAPP\\Workspace\\GIS Staff Workspace\\cschultz\\STEAR.gdb\\STEAR_Addresses_NOTFINAL"
geolocator = "https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/ArcGIS World Geocoding Service"
geoadr = "\\\\GISAPP\\Workspace\MyArcGIS\\Geocoders\\PerfectMind_Arcmap.loc"
geoTable = "\\\\GISAPP\\Workspace\\sdeFiles\\Faith.sde\\Faith.DBO.VW_STEAR_Evacuate"
geoParameters =  "'Address or Place' StreetAddress VISIBLE NONE;Address2 <None> VISIBLE NONE;Address3 <None> VISIBLE NONE;Neighborhood <None> VISIBLE NONE;City City VISIBLE NONE;County <None> VISIBLE NONE;State State VISIBLE NONE;ZIP Zip VISIBLE NONE;ZIP4 <None> VISIBLE NONE;Country <None> VISIBLE NONE"

if arcpy.Exists(pointLayer):
    arcpy.Delete_management(pointLayer)
    print("y")
    arcpy.geocoding.GeocodeAddresses(r"\\gisapp\Workspace\sdeFiles\Faith.sde\Faith.dbo.VW_STEAR_Evacuate", geolocator, geoParameters, pointLayer, "STATIC", "US", "ROUTING_LOCATION", "Address", "ALL")
else:
    print("n")
    arcpy.geocoding.GeocodeAddresses(r"\\gisapp\Workspace\sdeFiles\Faith.sde\Faith.dbo.VW_STEAR_Evacuate", geolocator, geoParameters, pointLayer, "STATIC", "US", "ROUTING_LOCATION", "Address", "ALL")
    
KEEP_LST = ["USER_StatusCode", "USER_FullName", "USER_StreetAddress", "USER_Apt", "USER_HomePhone", "USER_CellPhone", "USER_EmergencyContactName", "USER_EmergencyContactPhone", "USER_NeedTransportationToTheHub", "USER_Notes", "USER_LevelCodeDescription", "USER_AdditionalTravelers", "USER_NumberOfPets",
            "USER_AdditionalPetCratesNeeded", "USER_TransportationMethod", "USER_Language"]
fieldmappings = arcpy.FieldMappings()
fieldmappings.addTable(pointLayer)

fmPath =  "\\\\GISAPP\\Workspace\\GIS Staff Workspace\\cschultz\\STEAR.gdb"
fmName = "STEAR_Addresses"
fmLayer = "\\\\GISAPP\\Workspace\\GIS Staff Workspace\\cschultz\\STEAR.gdb\\STEAR_Addresses"
for f in fieldmappings.fields:
    if f.name not in KEEP_LST:
        fieldmappings.removeFieldMap(fieldmappings.findFieldMapIndex(f.name))

if arcpy.Exists(fmLayer):
    arcpy.Delete_management(fmLayer)
    arcpy.FeatureClassToFeatureClass_conversion(pointLayer, fmPath, fmName, "", fieldmappings)
else:
    arcpy.FeatureClassToFeatureClass_conversion(pointLayer, fmPath, fmName, "", fieldmappings)

arcpy.AlterField_management(fmLayer,"USER_StatusCode", "StatusCode", "StatusCode")
arcpy.AlterField_management(fmLayer,"USER_FullName", "FullName", "FullName")
arcpy.AlterField_management(fmLayer,"USER_StreetAddress", "StreetAddress", "StreetAddress")
arcpy.AlterField_management(fmLayer,"USER_Apt", "Apt", "Apt")
arcpy.AlterField_management(fmLayer,"USER_HomePhone","HomePhone", "HomePhone")
arcpy.AlterField_management(fmLayer,"USER_CellPhone","CellPhone", "CellPhone")
arcpy.AlterField_management(fmLayer,"USER_EmergencyContactName","EmergencyContactName", "EmergencyContactName")
arcpy.AlterField_management(fmLayer,"USER_EmergencyContactPhone", "EmergencyContactPhone", "EmergencyContactPhone")
arcpy.AlterField_management(fmLayer,"USER_NeedTransportationToTheHub", "NeedTransportationToTheHub", "NeedTransportationToTheHub")
arcpy.AlterField_management(fmLayer,"USER_Notes", "Notes", "Notes")
arcpy.AlterField_management(fmLayer,"USER_LevelCodeDescription", "LevelCodeDescription", "LevelCodeDescription")
arcpy.AlterField_management(fmLayer,"USER_AdditionalTravelers", "AdditionalTravelers", "AdditionalTravelers")
arcpy.AlterField_management(fmLayer,"USER_NumberOfPets", "NumberOfPets", "NumberOfPets")
arcpy.AlterField_management(fmLayer,"USER_AdditionalPetCratesNeeded", "AdditionalPetCratesNeeded", "AdditionalPetCratesNeeded")
arcpy.AlterField_management(fmLayer,"USER_TransportationMethod", "TransportationMethod", "TransportationMethod")
arcpy.AlterField_management(fmLayer,"USER_Language", "Language", "Language")

addrLayer = "\\\\GISAPP\\Workspace\\sdeFiles\\Hope_Owner.sde\\hope.DBO.GeoMAX\\hope.DBO.STEARAddresses"
if arcpy.Exists(addrLayer):
    arcpy.TruncateTable_management(addrLayer)
    arcpy.Append_management(fmLayer, addrLayer)

prjPath = "\\\\GISAPP\\Workspace\\Horizon\\ArcGISPro_Projects\\FeatureServices\\STEAR.aprx"

dict = {"STEAR Evacuees":["STEAR_Evacuees", "STEAR Evacuees, EOC", "This Layer shows the STEAR Evacuees throughout the City of Pearland.", 0]}
n=0
for key, value in dict.items():
    sd_fs_name = "{}".format(key)
    print(sd_fs_name)
    portal = "https://gis.pearlandtx.gov/arcgis"
    user = ""
    password = ""
    


    shrGroups = "4fa8cb0fb0374823899e58342bc5d6a5"

    relPath = "\\\\GISAPP\\Workspace\\Horizon\\Scripts"
    sddraft = os.path.join(relPath, "WebUpdate.sddraft")
    sd = os.path.join(relPath, "WebUpdate.sd")

    arcpy.env.overwriteOutput = True
    prj = arcpy.mp.ArcGISProject(prjPath)
    m = prj.listMaps('Map')[0]
    mp = m.listLayers()[n]
    arcpy.mp.CreateWebLayerSDDraft(mp, sddraft, sd_fs_name, 'MY_HOSTED_SERVICES', 'FEATURE_ACCESS',
                                    'Planning', True, True, False, True)
    arcpy.StageService_server(sddraft, sd)

    gis = arcgis.GIS(portal, user, password)
    sdItem = gis.content.search(query="title:"+ value[0] + " AND owner: " + user, item_type="Service Definition")[0]
    sdItem.update(data=sd)
    sdItem.update(item_properties={'tags': '{}'.format(value[1]),
                                    'snippet': "This Layer is updated automatically through a Python Script.",
                                    'description': '{}'.format(value[2])})

    fs = sdItem.publish(overwrite=True)
    fs.share(groups=shrGroups)

print(".")
