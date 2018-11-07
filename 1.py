import urllib
import json

import json_obj as json_obj

locu_api='9fb8cd70cb34cab8e83690473133f51943b5c93f'

#url='https://api.locu.com/v1_0/venue/search/?localiity=...???'
#json_obj=urllib.urlopen(url)


#locality=Newport%20Becah&category=restaurant&



def locu_search(query):
    api_key=locu_api
    url='https://api.locu.com/v1_0/venue/search/?api_key=' + api_key
    locality=query.replace(' ','%20')
    final_url=url + "&locality=" + locality + "&category=restaurant"
    json_obj = urllib.urlopen(final_url)
    data = json.load(json_obj)

data=data = json.load(json_obj)


for item in data['objects']:
    print (item['name'], item['phone'])


#Sve za obrisati!
