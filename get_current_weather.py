import requests
import json
import credentials
#import urllib.request
#from PIL import Image
#from io import BytesIO
#import StringIO
#https://developer.ibm.com/clouddataservices/2016/10/06/your-own-weather-forecast-in-a-python-notebook/
#https://console.bluemix.net/catalog/services/weather-company-data
username = credentials.login['username']
password = credentials.login['password']
# Request forecast for Home in Eagle Creek
lat = '39.845504'
lon = '-86.295995'
line='https://'+username+':'+password+'@twcservice.mybluemix.net/api/weather/v1/geocode/'+lat+'/'+lon+'/observations.json'

r=requests.get(line)
weather = json.loads(r.text)    

temp = weather['observation']['temp']
rh = weather['observation']['rh']
feels_like = weather['observation']['feels_like']
icon = weather['observation']['wx_icon']
url='https://raw.githubusercontent.com/ibm-watson-data-lab/python-notebooks/master/weathericons/icon'+str(int(icon))+'.png'


with open('icon.png', "wb") as file:
        response = requests.get(url)
        file.write(response.content)


print(temp, end ="")




#print(json.dumps(weather,indent=1))
