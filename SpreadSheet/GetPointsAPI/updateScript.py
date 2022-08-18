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
    flag2=flag
    for i in range(flag2+100,len(points_array),100):
        try:
            points_snapped=gmc.snap_to_roads(path=points_array[flag2:i],interpolate=False)
            
            flag2=i
            
        except:
            print("No Points updated!")
            break
    for i in range(flag,flag2):
        sh.update_cell(i,1,points_snapped[i-flag][0])
        sh.update_cell(i,2,points_snapped[i-flag][1])
        
    flag=flag2
    t.sleep(86000)
    

    
