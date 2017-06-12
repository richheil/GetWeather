#!/usr/bin/python2.7

import requests,json

def getWeather(url,zipcode,api_key):
#Get api response for location given
    try:
	response = requests.get(url, params={'zip': zipcode, 'units': 'imperial', 'appid': api_key })
    except requests.exceptions.RequestException as e:
        print e
        exit()
#parse api response with json
    parsed_response = json.loads(response.text)

#pull information from parsed json response

    location = parsed_response["name"]
    description = parsed_response["weather"][0]["description"]
    temp = parsed_response["main"]["temp"]
    temp_max = parsed_response["main"]["temp_max"]
    temp_min = parsed_response["main"]["temp_min"]
    humidity = parsed_response["main"]["humidity"]
    degree = u'\xb0'

    print "In %s it is %s%sF and %s with a low of %s and a high of %s. Humidity is %s%%." % (location, temp, degree, description, temp_min, temp_max, humidity)

if __name__ == "__main__":

#I would not usually include an api key in a public git repo, but I erred on the side of ease of use in this case
    api_key='cbc6d2ae9bbbce47aad5c0c96d20a4af'
    url='http://api.openweathermap.org/data/2.5/weather'

#get user zipcode
    while True:
        zipcode = raw_input("Please enter zipcode to check weather(default Los Angeles): ") or "90001"
        if not zipcode.isdigit() or int(zipcode)/100000 !=0:
            print ("That does not look like a zipcode please try again")
            continue
        else:
            break

    getWeather(url,zipcode,api_key)

