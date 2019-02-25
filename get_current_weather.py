import requests
import json
import credentials
import os
#import urllib.request
#from PIL import Image
#from io import BytesIO
#import StringIO
#https://developer.ibm.com/clouddataservices/2016/10/06/your-own-weather-forecast-in-a-python-notebook/
#https://console.bluemix.net/catalog/services/weather-company-data

import os

SECRET_KEY = os.environ.get('IN_CONTAINER', False)

if SECRET_KEY:
    os.system("/bin/mount -t cifs //mediacenter/Temp /tmp/media -o username=tv,password=")

username = credentials.login['username']
password = credentials.login['password']
# Request forecast for Home in Eagle Creek
lat = '39.845504'
lon = '-86.295995'
line='https://'+username+':'+password+'@twcservice.mybluemix.net/api/weather/v1/geocode/'+lat+'/'+lon+'/observations.json'

r=requests.get(line)
weather = json.loads(r.text)    

temp = weather['observation']['temp']
temp = str(temp)
rh = weather['observation']['rh']
rh = str(rh)+"%"
feels_like = weather['observation']['feels_like']
feels_like = str(feels_like)
dual_temp = temp+"/"+feels_like
icon = weather['observation']['wx_icon']
url='https://raw.githubusercontent.com/ibm-watson-data-lab/python-notebooks/master/weathericons/icon'+str(int(icon))+'.png'

with open('CurrHumidity.txt', "w") as file:
    file.write(rh)

if SECRET_KEY:
    with open('/tmp/media/icon.png', "wb") as file:
         response = requests.get(url)
         file.write(response.content)

if SECRET_KEY:
    with open('/tmp/media/CurrTemp.txt', "w") as file:
         file.write(str(dual_temp))

if SECRET_KEY:
    with open('/tmp/media/CurrHumidity.txt', "w") as file:
         file.write(rh)


print(temp, end ="")




#print(json.dumps(weather,indent=1))
