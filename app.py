import requests
def cp(color):
    response = requests.get(f"http://colormind.io/api-access/{color.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    data = response.json()
    return data
colorpalette = cp("Bulbasaur")
print(colorpalette)