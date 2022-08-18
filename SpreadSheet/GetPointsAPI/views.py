from rest_framework.decorators import api_view
from rest_framework.response import Response
import gspread
import requests

global points_array


@api_view(['GET'])
def getPoints(request):
    gc = gspread.service_account(filename='GetPointsAPI/testproject-347704-46bae9ce3d03.json')
    print(gc)
    sh = gc.open("test_sheet")
    print(sh)
    points_array=sh.sheet1.get_all_values()
    return Response(sh.sheet1.get_all_values())
    

def snapToRoads():
    points=""
    url = f"https://roads.googleapis.com/v1/snapToRoads?path={points}&interpolate=true&key=AIzaSyDhwmI3NkM9HWlohjrZQksbAetQ-M7ZOvQ"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)