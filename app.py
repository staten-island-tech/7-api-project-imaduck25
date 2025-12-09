import requests
def cp(color):
    response = requests.get(f"http://colormind.io/api-access/{color.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    data = {
        "model" : "default",
	    input : [[44,43,44],[90,83,82],"N","N","N"]
    }
    return data
colorpalette = cp("")
print(colorpalette)