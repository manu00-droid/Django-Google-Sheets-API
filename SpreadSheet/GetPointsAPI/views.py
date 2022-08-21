from rest_framework.decorators import api_view
from rest_framework.response import Response

import requests


from SpreadSheet import settings


@api_view(['GET'])
def getPoints(request):
    sh=settings.google_sheet
    points_array=sh.sheet1.get_all_values()
    print(points_array[0])
    for i in range(len(points_array)):
        points_array[i]=[points_array[i][1],points_array[i][2]]
    print(points_array[0],"HERERERRERERERERERe")
    return Response(points_array)



@api_view(['POST'])
def addPoint(request):
    sheet = settings.google_sheet
    lat = request.data['lat']
    lng = request.data['lng']
    length = len(sheet.sheet1.get_all_values())
    sheet.sheet1.update_cell(length + 1, 2, lat)
    sheet.sheet1.update_cell(length + 1, 3, lng)
    return Response("done")
