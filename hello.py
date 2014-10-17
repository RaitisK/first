from flask import Flask
from flask import render_template
import requests

app = Flask(__name__) #name ir viena no klasem

#MAX = 10 - definejam mainigos bez tipa.

# def route(fun):
	#print('pirms')
	#fun()
	#print('pec')

@app.route("/")
def hello(): #f-jas definesana, nosaukums, parametri
    #return "Hello World!"
    return render_template ('index.html')

@app.route("/about")
def hello1():
    return "We are the best!"

@app.route("/fc")
def forecast():
    API_KEY = "fd6e2be2474579f7314ec9eb4323874d"
    fc_url = ("https://api.forecast.io/forecast/{}/56.9496487,24.10518639999998?units=si".format(API_KEY)) #ar so ieliks {} iekavaas API_KEY tur esosaas linka dalas vietaa.
    # print(fc_url) parbaudei izvadija uz konsoles url
    data = requests.get(fc_url).json()
    hourly_data = data['hourly']['data']
    return render_template(
      'forecast.html', #renderee forecast template, un padod tur ieksaa mainigos, kam var pieklut forecast.html - tur ieliek timezone no sejienes.
      timezone=data['timezone'], # padod datus, kas attiecas uz template
      average=sum([d['temperature'] for d in hourly_data])/len(hourly_data),
      c_data=data['hourly']['data'], #padod datus pa stundam
    )
    # return requests.get(fc_url).text 
# return requests.get('http://eth0.me').text #izsauc request uz servisu, kas atgriez manu ip, un panem no taa texta dalju

if __name__ == "__main__": #palaizam galveno hello. Ideja - palaizam tikai tad, ja palaizam no konsoles.
# print('check') var te ielikt, paradas konsole, ja palaiz.
    app.run(debug=True)
