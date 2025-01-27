async function getWeather() {
    const location = document.getElementById("location").value;
    const container = document.getElementById("weather-container");

    if (location) {
        try {
            const response = await fetch('https://weather-website-szm0.onrender.com/get_weather', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ city: location }),
            });

            if (!response.ok) {
                const errorData = await response.json();
                alert(errorData.error || "An error occurred");
                return;
            }

            const weatherData = await response.json();
            container.innerHTML = `
                <div class="weather-details">
                    <p class="temperature"><b>${weatherData.temperature}°C</b></p>
                    <p class="details">${weatherData.description}</p>
                    <p class="details">Humidity: ${weatherData.humidity}%</p>
                    <button onclick="goBack()" class="back-button">Back</button>
                </div>
            `;
        } catch (error) {
            console.error("Error fetching weather data:", error);
            alert("Failed to fetch weather data. Please try again.");
        }
    } else {
        alert("Please enter a location.");
    }
}

function goBack() {
    const container = document.getElementById("weather-container");
    container.innerHTML = `
        <div class="input-box">
            <h2>Enter Location</h2>
            <input type="text" id="location" placeholder="City or Address">
            <button onclick="getWeather()">Get Weather</button>
        </div>
    `;
}
