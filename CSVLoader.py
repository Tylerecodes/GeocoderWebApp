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

#Running Header Definition      
titleOutput=(common_data(columntitles,checktitles))

#define what is the exact header match between the two lists
same_values=set(columntitles) & set(checktitles)

#Checking header function output, true or false. If false, print message for user
if titleOutput == None:
    print("Please insert appropriate file")

#Sort user spreadsheet for Address/address values
for title in columntitles:
    if title == "Address":
        C=df['Address']
    elif title == "address":
        C=df['address']
    else:
        pass

#setup two empty dataframes for the Longitude and Latitude values
df2=pd.DataFrame(columns=['Longitude'])
df3=pd.DataFrame(columns=['Longitude'])

# Loop for geolocating all addresses from spreadsheet
for i in C:
    rows2 = [[i,i+1] for i in range(C)]
    location=geolocater.geocode(i)
    longitudecoordinate=location.longitude
    latitudecoordinate=location.latitude
    print(location.longitude, location.latitude)
    print(longitudecoordinate+i)
