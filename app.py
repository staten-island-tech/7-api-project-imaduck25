import requests

def cs():
    url = "http://colormind.io/api-access/"
    data = {"model":"default"}
    response = requests.get(url, data)

    if response.status_code != 200:
        print ("Error fething palette!")
        return None
    
    info = response.json()
    return info

palette = cs()
for key, value in palette.items():
    print(f"{key.title()}: {value}")