from rest_framework.decorators import api_view
from rest_framework.response import Response
import gspread
import requests
import googlemaps as gm

key="AIzaSyDhwmI3NkM9HWlohjrZQksbAetQ-M7ZOvQ"
gmc=gm.Client(key=key)
@api_view(['GET'])
def getPoints(request):
    gc = gspread.service_account(filename='GetPointsAPI/testproject-347704-46bae9ce3d03.json')
    print(gc)
    sh = gc.open("test_sheet")
    print(sh)
    points_array=sh.sheet1.get_all_values()

    return Response(points_array)
 
@api_view(['POST'])
def snapPoly(request):
    points=request.data["point"]
    points_snapped=[]
    prev=0
    for i in range(100,len(points),100):
        points_snapped.append(gmc.snap_to_roads(path=points[prev:i],interpolate=True))
        prev=i
    points_snapped.append(gmc.snap_to_roads(path=points[prev:len(points)],interpolate=True))
    print(points_snapped)
    return Response(points_snapped)
    
        