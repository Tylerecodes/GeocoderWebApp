from flask import Flask, render_template, request
import pandas as pd
from geopy.geocoders import Nominatim
import csv
from flask import send_file, send_from_directory, safe_join, abort

geolocater= Nominatim(user_agent="GeocoderWebApp", timeout=1000)

app=Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route("/data", methods=['GET','POST'])
def data():
    if request.method == "POST":
        UserInput=request.form['csvfile']
        df = pd.read_csv(UserInput)
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

        if titleOutput != None:

            #Sort user spreadsheet for Address/address values
            for title in columntitles:
                if title == "Address":
                    C=df['Address']
                elif title == "address":
                    C=df['address']
                else:
                    pass

            #setup two empty lists for the Longitude and Latitude values
            rows2=[]
            rows3=[]

            # Loop for geolocating all addresses from spreadsheet
            for i in C:
                location=geolocater.geocode(i)
                longitudecoordinate=location.longitude
                latitudecoordinate=location.latitude
                rows2.append(longitudecoordinate)
                rows3.append(latitudecoordinate) 
                print(location.longitude, location.latitude)

            #Create Pandas dataframes from rows objects
            df2=pd.DataFrame(rows2,columns=['Longitude'])
            df3=pd.DataFrame(rows3,columns=['Latitude'])

            #Merge dataframes as new columns to user excel file
            df['Longitude']=df2
            df['Latitude']=df3

            #Convert dataframe to excel sheet for user to download
            df.to_csv ('exportDataframe.csv', index = False, header=True)

            #Convert df to html table for displaying
            HTMLTable=df.to_html(header="true", table_id="table")

            return render_template('data.html', data=HTMLTable )
    return render_template('index.html', text="Please insert appropriate file")

#Generating new page for downloading CSV file
@app.route('/download', methods=['GET', 'POST'])
def downloadfile():
        path = "exportDataframe.csv"
        return send_file(path, as_attachment=True)

if __name__== '__main__':
    app.debug=True
    app.run()