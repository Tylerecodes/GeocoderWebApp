import pandas as pd
from geopy.geocoders import Nominatim

geolocater= Nominatim(user_agent="GeocoderWebApp")

df = pd.read_csv("Adata.csv")
columntitles=df.columns.tolist()
checktitles=['Address', 'address']

#Checking if Address and or address column is present in spreadsheet
def common_data(columntitles, checktitles):
    for x in columntitles:
        for y in checktitles:
            if x==y:
                result=True
                return result
                break
        

titleOutput=(common_data(columntitles,checktitles))

if titleOutput == None:
    print("Please insert appropriate file")

# for i in data:
#     location=geolocater.geocode(i, "Address")
#     print(location.latitude, location.longitude)