#!/usr/bin/python2.7

import requests,json


api_key='cbc6d2ae9bbbce47aad5c0c96d20a4af' 
url='http://api.openweathermap.org/data/2.5/weather'#?zip='+zipcode+'&units=imperial&appid='+api_key

#get user zipcode
while True:
    zipcode = raw_input("Please enter zipcode to check weather(default Los Angeles): ") or "90001"
    if not zipcode.isdigit() or int(zipcode)/100000 !=0:
        print ("That does not look like a zipcode please try again")
        continue
    else:
        break


def getWeather(url,zipcode,api_key):
#Get api response for location given
    try:
	response = requests.get(url, params={'zip': zipcode, 'units': 'imperial', 'appid': api_key })
    except requests.exceptions.RequestException as e:
        print e
        exit()
#parse api response with json
    parsed_response = json.loads(response.text)

#print data
    #print parsed_response["main"]
    return parsed_response["main"]

print getWeather(url,zipcode,api_key)



exit()
