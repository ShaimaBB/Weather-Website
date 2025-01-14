from flask import Flask, request, jsonify
import requests
from flask_cors import CORS  # Add CORS for cross-origin support

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
API_KEY = 'a48d3f43096ab0de7cfc5201678b427b'  # Replace with your OpenWeatherMap API key

@app.route('/get_weather', methods=['POST'])
def get_weather():
    data = request.get_json()
    city = data.get('city')
    if not city:
        return jsonify({"error": "City is required"}), 400
    
    base_url = f"http://api.openweathermap.org/data/2.5/weather?appid={API_KEY}&q={city}&units=metric"
    response = requests.get(base_url)
    
    if response.status_code != 200:
        return jsonify({"error": "City not found or invalid API key"}), 404
    
    weather_data = response.json()
    return jsonify({
        "city": weather_data["name"],
        "temperature": weather_data["main"]["temp"],
        "description": weather_data["weather"][0]["description"],
        "humidity": weather_data["main"]["humidity"]
    })

if __name__ == '__main__':
    app.run(debug=True)
