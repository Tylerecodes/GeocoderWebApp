from flask import Flask, render_template, request
import geopandas as gpd
import geoplot as gplt

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
        if request.method=='POST':
        email=request.form["email_name"]
        height=request.form["height_name"]
        if db.session.query(Data).filter(Data.email_==email).count() == 0:
            data=Data(email,height)
            db.session.add(data)
            db.session.commit()
            average_height=db.session.query(func.avg(Data.height_)).scalar()
            average_height=round(average_height,1)
            count=db.session.query(Data.height_).count()
            send_email(email, height, average_height, count)
            print(average_height)
            return render_template("success.html")
    return render_template('index.html',
    text="Please make sure you have an address column in your CSV file")

# @app.route("/success", methods=['POST'])
# def success():
#     if request.method=='POST':
#         email=request.form["email_name"]
#         height=request.form["height_name"]
#         if db.session.query(Data).filter(Data.email_==email).count() == 0:
#             data=Data(email,height)
#             db.session.add(data)
#             db.session.commit()
#             average_height=db.session.query(func.avg(Data.height_)).scalar()
#             average_height=round(average_height,1)
#             count=db.session.query(Data.height_).count()
#             send_email(email, height, average_height, count)
#             print(average_height)
#             return render_template("success.html")
#     return render_template('index.html',
#     text="Seems like we've got something from that email address already")

if __name__== '__main__':
    app.debug=True
    app.run()