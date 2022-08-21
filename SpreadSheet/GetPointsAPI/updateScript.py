import gspread
import googlemaps as gm
import time as t

gmc=gm.Client(key="AIzaSyDhwmI3NkM9HWlohjrZQksbAetQ-M7ZOvQ")

gsc = gspread.service_account(filename='Djanog-Google-Sheets-API/SpreadSheet/SpreadSheet/testproject-347704-46bae9ce3d03.json')
google_sheet = gsc.open("test_sheet")

flag=0
while(1):
    sh=google_sheet
    points_array=sh.sheet1.get_all_values()
    flag2=flag
    for i in range(flag2+100,len(points_array),100):
        try:
            points_snapped=gmc.snap_to_roads(path=points_array[flag2:i],interpolate=False)
            
            flag2=i
            
        except:
            print("Error")
    for i in range(flag,flag2):
        sh.sheet1.update_cell(i,1,points_snapped[i-flag][0])
        sh.sheet1.update_cell(i,2,points_snapped[i-flag][1])
        print("Update Successful")

    flag=flag2
    t.sleep(86000)