import gspread
import googlemaps as gm
import time as t


flag=0
key="AIzaSyDhwmI3NkM9HWlohjrZQksbAetQ-M7ZOvQ"
gmc=gm.Client(key=key)

while(1):
    gc = gspread.service_account(filename='GetPointsAPI/testproject-347704-46bae9ce3d03.json')
    print(gc)
    sh = gc.open("test_sheet")
    print(sh)
    points_array=sh.sheet1.get_all_values()
    try:
        points_snapped=gmc.snap_to_roads(path=points_array[flag:],interpolate=True)
        flag=len(points_array)
    except:
        print("No Points updated!")
    t.sleep(86000)
    

    
