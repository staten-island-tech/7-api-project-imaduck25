""" import requests
import json

def cs():
    url = "http://colormind.io/api-access/"
    data = {"model":"default}"}
    response = requests.post(url, data=json.dumps(data))

    if response.status_code != 200:
        print ("Error fething palette!")
        return None
    
    data = response.json()
    return data

palette = cs()
print(palette) """


import requests

def cp():
    response = requests.get(f"http://colormind.io/api-access/")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return data

palette = cp()
print(palette)