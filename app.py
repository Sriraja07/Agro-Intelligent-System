# Importing essential libraries and modules

from flask import Flask,render_template,request,Markup
import numpy as np
import pandas as pd
import requests
import pickle
import io
from static.utils.fertilizer import fertilizer_dic
from static.utils import cropindex
from static.utils import geoloc
# Loading crop recommendation model
crop_recommedation_model_path='Model/crop_recommender.pkl'
crop_recommedation_model=pickle.load(open(crop_recommedation_model_path,'rb'))

#Rain Model
rain_model_path='Model/rainfall.pkl'
rain_model=pickle.load(open(rain_model_path,'rb'))
#Crop Yield
crop_yield_model_path='Model/crop_yield.pkl'
crop_yield_model=pickle.load(open(crop_yield_model_path,'rb'))

# weather data
def weather_fetch(city_name):
    api_key= "9d7cde1f6d07ec55650544be1631307e"
    base_url="http://api.openweathermap.org/data/2.5/weather?"

    complete_url=base_url+"appid="+api_key+"&q="+city_name
    response=requests.get(complete_url)
    x=response.json()
    
    if x["cod"]!="404":
        y=x["main"]
        temperature=round((y["temp"]-273.15),2)
        humidity=y["humidity"]
        return temperature,humidity
    else:
        return None
# Flask APP

app=Flask(__name__)

#render home page
@app.route('/')
def home():
    return render_template('home.html')

#render crop recommendation from page
@app.route('/crop-recommend')
def crop_recommend():
    return render_template('crop.html')

@app.route('/crop-yield')
def crop_yield():
    title = 'Harvestify - Fertilizer Suggestion'
    return render_template('cropyield.html')

@app.route('/fertilizer')
def fertilizer_recommendation():
    title = 'Harvestify - Fertilizer Suggestion'

    return render_template('fertilizer.html', title=title)

@app.route('/about')
def about():
    return render_template('about.html')


# render crop recommendation result page
@app.route('/crop-predict',methods=['POST'])
def crop_prediction():
    title='Result Page'
    
    if request.method=='POST':
        N=int(request.form['nitrogen'])
        P=int(request.form['phosphorous'])
        K=int(request.form['pottasium'])
        ph=float(request.form['ph'])
        lat=float(request.form["lat"])
        lon=float(request.form["lon"])
        city=geoloc.geolo(lat,lon)
        
        if weather_fetch(city) != None:
            temperature,humidity = weather_fetch(city)
            rainfalls=np.array([[N,P,K,temperature,humidity,ph]])
            my_predictions=rain_model.predict(rainfalls)
            rainfall=float(my_predictions[0])
            data=np.array([[N,P,K,temperature,humidity,ph,rainfall]])
            my_prediction=crop_recommedation_model.predict(data)
            final_prediction=my_prediction[0]
            ws="You should grow "+final_prediction+" in your farm"

            return render_template('crop.html',prediction=ws)
        else:
            return render_template('crop.html',prediction="Can't predicted Some Error. Try Again")
@ app.route('/fertilizer-predict', methods=['POST'])
def fert_recommend():
    crop_name = str(request.form['cropname'])
    N = int(request.form['nitrogen'])
    P = int(request.form['phosphorous'])
    K = int(request.form['pottasium'])
    # ph = float(request.form['ph'])

    df = pd.read_csv('Model/fertilizer.csv')

    nr = df[df['Crop'] == crop_name]['N'].iloc[0]
    pr = df[df['Crop'] == crop_name]['P'].iloc[0]
    kr = df[df['Crop'] == crop_name]['K'].iloc[0]

    n = nr - N
    p = pr - P
    k = kr - K
    temp = {abs(n): "N", abs(p): "P", abs(k): "K"}
    max_value = temp[max(temp.keys())]
    if max_value == "N":
        if n < 0:
            key = 'NHigh'
        else:
            key = "Nlow"
    elif max_value == "P":
        if p < 0:
            key = 'PHigh'
        else:
            key = "Plow"
    else:
        if k < 0:
            key = 'KHigh'
        else:
            key = "Klow"

    response = Markup(str(fertilizer_dic[key]))

    return render_template('fertilizer-result.html', recommendation=response)

@app.route('/crop-yields',methods=['POST'])
def crop_yields():
    if request.method=='POST':
        crop=request.form.get("crops")
        area=float(request.form['area'])
        season=request.form.get('seasons')
        N=int(request.form['nitrogen'])
        P=int(request.form['phosphorous'])
        K=int(request.form['pottasium'])
        ph=float(request.form['ph'])
        lat=float(request.form["lat"])
        lon=float(request.form["lon"])
        city=geoloc.geolo(lat,lon)
        crop_i=cropindex.cpind(crop)
        season_i=cropindex.seaind(season)

        if weather_fetch(city) != None:
            temperature,humidity = weather_fetch(city)
            rainfalls=np.array([[N,P,K,temperature,humidity,ph]])
            my_predictions=rain_model.predict(rainfalls)
            rainfall=float(my_predictions[0])

            data=np.array([[season_i,crop_i,area,rainfall]])
            my_prediction=crop_yield_model.predict(data)
            final_prediction=int(my_prediction[0])
        
            ws="Yield:{} Production/KGs".format(final_prediction)
            return render_template('cropyield.html',prediction=ws)
        else:
            return render_template('cropyield.html',prediction="Can't predicted Some Error. Try Again")
if __name__=='__main__':
    app.run(debug=True)
