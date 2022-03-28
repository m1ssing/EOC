
import arcpy
import datetime
import re
#(Monday - 0, Tuesday - 1, Wednesday - 2, Thursday - 3, Friday - 4, Saturday - 5, Sunday - 6)
currentDate= datetime.datetime.today().weekday()
currentTime = str(datetime.datetime.now().strftime("%H:%M:%S"))
print(currentTime)

dict = {"0": {"7110 MAGNOLIA PKWY": ["08:00:00", "22:00:00"],
              "12806 BROADWAY ST": ["09:00:00", "20:00:00"],
              "9522 BROADWAY ST": ["08:00:00", "22:00:00"],
              "11600 SHADOW CREEK PKWY": ["10:00:00", "20:00:00"],
              "2900 BROADWAY ST": ["00:00:00", "23:59:59"],
              "1801-115 COUNTRY PLACE PKWY": ["09:00:00", "17:00:00"],
              "11233-123A SHADOW CREEK PKWY": ["09:00:00", "17:00:00"],
              "6302-100 BROADWAY ST": ["09:30:00", "18:00:00"],
              "9215-113 BROADWAY ST": ["09:00:00", "18:00:00"],
              "1834 BROADWAY ST": ["09:00:00", "19:00:00"],
              "7121 BROADWAY ST": ["09:00:00", "19:00:00"],
              "6122 BROADWAY ST": ["09:00:00", "20:00:00"],
              "3287 BROADWAY ST": ["00:00:00", "23:59:59"],
              "11633 SHADOW CREEK PKWY": ["09:00:00", "21:00:00"],
              "1515 BROADWAY ST": ["09:00:00", "21:00:00"]},

        "1": {"7110 MAGNOLIA PKWY": ["08:00:00", "22:00:00"],
              "12806 BROADWAY ST": ["09:00:00", "20:00:00"],
              "9522 BROADWAY ST": ["08:00:00", "22:00:00"],
              "11600 SHADOW CREEK PKWY": ["10:00:00", "20:00:00"],
              "2900 BROADWAY ST": ["00:00:00", "23:59:59"],
              "1801-115 COUNTRY PLACE PKWY": ["09:00:00", "17:00:00"],
              "11233-123A SHADOW CREEK PKWY": ["09:00:00", "17:00:00"],
              "6302-100 BROADWAY ST": ["09:30:00", "18:00:00"],
              "9215-113 BROADWAY ST": ["09:00:00", "18:00:00"],
              "1834 BROADWAY ST": ["09:00:00", "19:00:00"],
              "7121 BROADWAY ST": ["09:00:00", "19:00:00"],
              "6122 BROADWAY ST": ["09:00:00", "20:00:00"],
              "3287 BROADWAY ST": ["00:00:00", "23:59:59"],
              "11633 SHADOW CREEK PKWY": ["09:00:00", "21:00:00"],
              "1515 BROADWAY ST": ["09:00:00", "21:00:00"]},

        "2": {"7110 MAGNOLIA PKWY": ["08:00:00", "22:00:00"],
              "12806 BROADWAY ST": ["09:00:00", "20:00:00"],
              "9522 BROADWAY ST": ["08:00:00", "22:00:00"],
              "11600 SHADOW CREEK PKWY": ["10:00:00", "20:00:00"],
              "2900 BROADWAY ST": ["00:00:00", "23:59:59"],
              "1801-115 COUNTRY PLACE PKWY": ["09:00:00", "17:00:00"],
              "11233-123A SHADOW CREEK PKWY": ["09:00:00", "17:00:00"],
              "6302-100 BROADWAY ST": ["09:30:00", "18:00:00"],
              "9215-113 BROADWAY ST": ["09:00:00", "18:00:00"],
              "1834 BROADWAY ST": ["09:00:00", "19:00:00"],
              "7121 BROADWAY ST": ["09:00:00", "19:00:00"],
              "6122 BROADWAY ST": ["09:00:00", "20:00:00"],
              "3287 BROADWAY ST": ["00:00:00", "23:59:59"],
              "11633 SHADOW CREEK PKWY": ["09:00:00", "21:00:00"],
              "1515 BROADWAY ST": ["09:00:00", "21:00:00"]},

        "3": {"7110 MAGNOLIA PKWY": ["08:00:00", "22:00:00"],
              "12806 BROADWAY ST": ["09:00:00", "20:00:00"],
              "9522 BROADWAY ST": ["08:00:00", "22:00:00"],
              "11600 SHADOW CREEK PKWY": ["10:00:00", "20:00:00"],
              "2900 BROADWAY ST": ["00:00:00", "23:59:59"],
              "1801-115 COUNTRY PLACE PKWY": ["09:00:00", "17:00:00"],
              "11233-123A SHADOW CREEK PKWY": ["09:00:00", "17:00:00"],
              "6302-100 BROADWAY ST": ["09:30:00", "18:00:00"],
              "9215-113 BROADWAY ST": ["09:00:00", "18:00:00"],
              "1834 BROADWAY ST": ["09:00:00", "19:00:00"],
              "7121 BROADWAY ST": ["09:00:00", "19:00:00"],
              "6122 BROADWAY ST": ["09:00:00", "20:00:00"],
              "3287 BROADWAY ST": ["00:00:00", "23:59:59"],
              "11633 SHADOW CREEK PKWY": ["09:00:00", "21:00:00"],
              "1515 BROADWAY ST": ["09:00:00", "21:00:00"]},

        "4": {"7110 MAGNOLIA PKWY": ["08:00:00", "22:00:00"],
              "12806 BROADWAY ST": ["09:00:00", "20:00:00"],
              "9522 BROADWAY ST": ["08:00:00", "22:00:00"],
              "11600 SHADOW CREEK PKWY": ["10:00:00", "20:00:00"],
              "2900 BROADWAY ST": ["00:00:00", "23:59:59"],
              "1801-115 COUNTRY PLACE PKWY": ["09:00:00", "15:00:00"],
              "11233-123A SHADOW CREEK PKWY": ["09:00:00", "17:00:00"],
              "6302-100 BROADWAY ST": ["09:30:00", "18:00:00"],
              "9215-113 BROADWAY ST": ["09:00:00", "18:00:00"],
              "1834 BROADWAY ST": ["09:00:00", "19:00:00"],
              "7121 BROADWAY ST": ["09:00:00", "19:00:00"],
              "6122 BROADWAY ST": ["09:00:00", "20:00:00"],
              "3287 BROADWAY ST": ["00:00:00", "23:59:59"],
              "11633 SHADOW CREEK PKWY": ["09:00:00", "21:00:00"],
              "1515 BROADWAY ST": ["09:00:00", "21:00:00"]},

        "5": {"7110 MAGNOLIA PKWY": ["09:00:00", "18:00:00"],
              "12806 BROADWAY ST": ["09:00:00", "18:00:00"],
              "9522 BROADWAY ST": ["08:00:00", "20:00:00"],
              "11600 SHADOW CREEK PKWY": ["10:00:00", "18:00:00"],
              "2900 BROADWAY ST": ["00:00:00", "23:59:59"],
              "1801-115 COUNTRY PLACE PKWY": ["09:00:00", "13:00:00"],
              "11233-123A SHADOW CREEK PKWY": ["00:00:00", "00:00:00"],
              "6302-100 BROADWAY ST": ["00:00:00", "00:00:00"],
              "9215-113 BROADWAY ST": ["10:00:00", "14:00:00"],
              "1834 BROADWAY ST": ["09:00:00", "16:00:00"],
              "7121 BROADWAY ST": ["00:00:00", "00:00:00"],
              "6122 BROADWAY ST": ["09:00:00", "18:00:00"],
              "3287 BROADWAY ST": ["00:00:00", "23:59:59"],
              "11633 SHADOW CREEK PKWY": ["09:00:00", "18:00:00"],
              "1515 BROADWAY ST": ["09:00:00", "18:00:00"]},

        "6": {"7110 MAGNOLIA PKWY": ["10:00:00", "18:00:00"],
              "12806 BROADWAY ST": ["10:00:00", "18:00:00"],
              "9522 BROADWAY ST": ["08:00:00", "20:00:00"],
              "11600 SHADOW CREEK PKWY": ["10:00:00", "18:00:00"],
              "2900 BROADWAY ST": ["00:00:00", "23:59:59"],
              "1801-115 COUNTRY PLACE PKWY": ["00:00:00", "00:00:00"],
              "11233-123A SHADOW CREEK PKWY": ["00:00:00", "00:00:00"],
              "6302-100 BROADWAY ST": ["00:00:00", "00:00:00"],
              "9215-113 BROADWAY ST": ["00:00:00", "00:00:00"],
              "1834 BROADWAY ST": ["00:00:00", "00:00:00"],
              "7121 BROADWAY ST": ["00:00:00", "00:00:00"],
              "6122 BROADWAY ST": ["10:00:00", "18:00:00"],
              "3287 BROADWAY ST": ["00:00:00", "23:59:59"],
              "11633 SHADOW CREEK PKWY": ["10:00:00", "18:00:00"],
              "1515 BROADWAY ST": ["10:00:00", "18:00:00"]},


        }

fields = ["USER_Address", "Status"]
points = "\\\\GISAPP\\Workspace\\sdeFiles\\Horizon_Owner.sde\\Horizon.DBO.EOC\\Horizon.DBO.Pharmacies"
with arcpy.da.UpdateCursor(points, fields) as Ucur:
    for Urow in Ucur:
        for key, value in dict.items():
            if key == str(currentDate):
                for k, v in value.items():
                    if Urow[0] == k:
                        if currentTime >= v[0] and currentTime <= v[1]:
                            Urow[1] = "Open"
                            Ucur.updateRow(Urow)
                        else:
                            Urow[1] = "Closed"
                            Ucur.updateRow(Urow)