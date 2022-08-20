from rest_framework.decorators import api_view
from rest_framework.response import Response
import gspread
import requests
import googlemaps as gm


import json
from SpreadSheet import settings


@api_view(['GET'])
def getPoints(request):
    gc = gspread.service_account(filename='GetPointsAPI/testproject-347704-46bae9ce3d03.json')
    print(gc)
    sh = gc.open("test_sheet")
    print(sh)
    points_array=sh.sheet1.get_all_values()

    return Response(points_array)



@api_view(['POST'])
def addPoint(request):
    sheet = settings.google_sheet
    lat = request.data['lat']
    lng = request.data['lng']
    length = len(sheet.sheet1.get_all_values())
    sheet.sheet1.update_cell(length + 1, 1, lat)
    sheet.sheet1.update_cell(length + 1, 2, lng)
    return Response("done")
