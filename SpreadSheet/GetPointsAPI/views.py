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
    
    points=request.POST["point"]
  
    # print(points)
    point=points.split(",")
    # print(point)
    for j in range(len(point)):
        i=point[j]
        i=i.replace("(","")
        i=i.replace(")","")
        print(i,"here","\n")
        point[j]=float(i)
        print("FLOATAFEAGSRTGWERE")

    combPoint=[]
    a=[]
    for i in range(1,len(point),2):
        a.append(point[i-1])
        a.append(point[i])
        combPoint.append(a)
    print(combPoint)
    points_snapped=[]
    prev=0
    for i in range(100,len(combPoint),100):
        points_snapped.append(gmc.snap_to_roads(path=combPoint[prev:i],interpolate=True))
        prev=i
    points_snapped.append(gmc.snap_to_roads(path=combPoint[prev:len(combPoint)],interpolate=True))
    print(points_snapped,"AFSGHGR")
    return Response(points_snapped)
    
        