
# import os
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# import Prediction
# import zipfile
# from .models import picture, zipFile,zipFile_csv
# from ClassifierService import settings
# import requests
# import base64
# import pandas as pd
import gspread
gsc = gspread.service_account(filename='/Users/aditya/Desktop/ROAD-DAMAGE/rd-wa/ClassifierService/ClassifierApi/testproject-347704-46bae9ce3d03.json')
google_sheet = gsc.open("UL_GPS_Data")

def addPoint(lat,lng):
    sheet = google_sheet
    print("got Lat LAng")
    length = len(sheet.sheet1.get_all_values())
    sheet.sheet2.update_cell(length + 1, 2, lat)
    sheet.sheet2.update_cell(length + 1, 3, lng)
    print("SHEET UPDATED!!")
    print("DOME")

addPoint(111,111)