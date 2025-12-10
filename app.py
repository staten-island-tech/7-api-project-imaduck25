import requests

def cs():
    url = "http://colormind.io/api-access/"
    data = {"model":"default"}
    response = requests.post(url, data)

    if response.status_code != 200:
        print ("Error fething palette!")
        return None
    
    data = response.json()
    return data

palette = cs()
for key, value in palette.items():
    print(f"{key.title()}: {value}")