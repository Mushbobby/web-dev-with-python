from flask import Flask, render_template , request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/weather')

def get_weather():

    city = request.args.get('city')

    # empty str check
    
    if not bool(city.strip()):
       return render_template(
           "citynotfound.html"
           
       )
    weather_data = get_current_weather(city)
    
    # city not in api db
    if not weather_data['cod'] == 200:
        return render_template(
            "citynotfound.html"
        )

    
    return render_template(
        "weather.html",
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp = f"{weather_data['main']['temp']:.2f}",
        feels_like = f"{weather_data['main']['feels_like']:.2f}"

    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
