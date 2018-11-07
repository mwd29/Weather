import requests
#import math

i=input("Unesite neki broj razlicit od 0: ")

while i!='0':
    api_address='http://api.openweathermap.org/data/2.5/weather?appid=f3d7a7446155323b11fb4fc53ec7d7f3&q='
    city=input("City Name: ")

    url=api_address + city

    json_data=requests.get(url).json()
    weather_data=json_data['weather'] [0] ['main']
    weather_description=json_data['weather'] [0] ['description']

    temperature_data=json_data['main'] ['temp']
    temperature_celsius=temperature_data - 272.15

    #round(temperature_celsius,1)

    print ("Weather =" + " " + weather_data)
    print("Description =", weather_description.capitalize())

    #print ("Temperature =" + " " + str(temperature_celsius) + " " + "Celsius")
    print("Temperature =", round(temperature_celsius,1), "Celsius")

    i=input("\nAko ne zelite da nastavite unesite 0, u suprotnom bilo koji drugi broj: ")


print('End of program')
