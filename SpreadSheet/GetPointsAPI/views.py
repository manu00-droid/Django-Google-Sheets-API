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
    
# def pointsToString(point_array):
#     points_string=""
#     for i in point_array:
#         current_points_string="%2C".join(str(i[0]),str(i[1]))
#         points_string="%7C".join(points_string,current_points_string)
#     return points_string

# def snapToRoads():
#     points=""
#     url = f"https://roads.googleapis.com/v1/snapToRoads?path={points}&interpolate=true&key=AIzaSyDhwmI3NkM9HWlohjrZQksbAetQ-M7ZOvQ"

#     payload = {}
#     headers = {}

#     response = requests.request("GET", url, headers=headers, data=payload)

#     print(response.text)