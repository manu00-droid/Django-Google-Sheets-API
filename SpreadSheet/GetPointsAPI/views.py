from urllib import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
import gspread
import requests
import googlemaps as gm
<<<<<<< HEAD
import json
=======
from SpreadSheet import settings

>>>>>>> eddee071277bb8134c336641bdbacd6dba9e7f0f

@api_view(['GET'])
def getPoints(request):
<<<<<<< HEAD
    gc = gspread.service_account(filename='GetPointsAPI/testproject-347704-46bae9ce3d03.json')
    # print(gc)
    sh = gc.open("test_sheet")
    # print(sh) 
    points_array=sh.sheet1.get_all_values()
    print("sheet sent!")
    return Response(points_array)
 
@api_view(['POST'])
def snapPoly(request):
    
    points=request.POST["point"]


    
    
    points=points.replace("(","")
    point=points.split("),")
    combPoint=point
    combPoint[-1]=combPoint[-1].replace(")","")
    
    print(combPoint)
    points_snapped=[]
    prev=0
    for i in range(100,len(combPoint),100):
        points_snapped+=gmc.snap_to_roads(path=combPoint[prev:i],interpolate=True)
        prev=i

    points_snapped+=gmc.snap_to_roads(path=combPoint[prev:len(combPoint)],interpolate=True)
    # print(points_snapped[0])
    return Response(points_snapped)
    
        
=======
    sheet = settings.google_sheet
    points_array = sheet.sheet1.get_all_values()
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
>>>>>>> eddee071277bb8134c336641bdbacd6dba9e7f0f
