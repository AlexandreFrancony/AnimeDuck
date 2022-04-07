import requests

dep = "5 Avenue Anatole,Paris" #<adresse,ville>
arr = "Place Charles de Gaule, Paris";#<adresse,ville>

adr_dep=dep.split(',')[0]
vil_dep=dep.split(',')[1]

adr_arr=arr.split(',')[0]
vil_arr=arr.split(',')[1]

adr_dep_link = dep.split(',')[0].replace(' ', '+')
vil_dep_link = dep.split(',')[1].replace(' ', '+')

adr_arr_link = arr.split(',')[0].replace(' ', '+')
vil_arr_link = arr.split(',')[1].replace(' ', '+')

url_inf_dep = "https://api-adresse.data.gouv.fr/search/?q=" + adr_dep + "+" + vil_dep
url_inf_arr = "https://api-adresse.data.gouv.fr/search/?q=" + adr_arr + "+" + vil_arr

inf_dep = requests.get(url_inf_dep).json()
inf_arr = requests.get(url_inf_arr).json()

"""                     Coordinates
lat_dep=inf_dep['features'][0]['geometry']['coordinates'][1]
lon_dep=inf_dep['features'][0]['geometry']['coordinates'][0]

lat_arr = inf_arr["features"][0]["geometry"]["coordinates"][1]
lon_arr = inf_arr["features"][0]["geometry"]["coordinates"][0]
"""

CP_arr = str(inf_arr["features"][0]["properties"]["postcode"])

url_temp = "https://api.weatherbit.io/v2.0/current?postal_code=" + CP_arr + "&country=FR&lang=fr&key=8ff2fdc8513f447baac1893aff838be9"
inf_temp_arr = requests.get(url_temp).json()
temp_arr = inf_temp_arr["data"][0]["temp"]
mete_arr = inf_temp_arr["data"][0]["weather"]["description"]

print("Départ: " + str(adr_dep) + "; " + str(vil_dep) )
print("Destination: " + str(adr_arr) + "; " + str(vil_arr) )
print("Météo à l'arrivée: " + str(temp_arr) + "°C; " + str(mete_arr))