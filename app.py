from flask import Flask, request, jsonify
import requests
from flask_cors import CORS
import os


app = Flask(__name__)
CORS(app)

API_KEY = 'a48d3f43096ab0de7cfc5201678b427b'

@app.route('/get_weather', methods=['POST'])
def get_weather():
    data = request.get_json()
    city = data.get('city')
    
    if not city:
        return jsonify({"error": "City is required"}), 400
    
    base_url = f"http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code != 200:
        return jsonify({"error": "City not found or invalid API key"}), 404
    
    weather_data = response.json()
    return jsonify({
        "city": weather_data.get("name"),
        "temperature": weather_data["main"].get("temp"),
        "description": weather_data["weather"][0].get("description"),
        "humidity": weather_data["main"].get("humidity")
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000)) 
    app.run(host='0.0.0.0', port=port, debug=True)
