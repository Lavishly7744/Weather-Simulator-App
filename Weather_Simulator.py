import random

class WeatherSimulator:
    def __init__(self, location, season):
        self.location = location
        self.season = season
        self.weather_data = {
            'temperature': 0,
            'humidity': 0,
            'precipitation': 0,
            'wind_speed': 0
        }

    def generate_weather(self):
        if self.season == 'winter':
            self.weather_data['temperature'] = random.uniform(-10, 10)
        elif self.season == 'summer':
            self.weather_data['temperature'] = random.uniform(20, 40)
        elif self.season == 'spring' or self.season == 'fall':
            self.weather_data['temperature'] = random.uniform(10, 25)
        else:
            print("Unknown season. Please choose from 'winter', 'summer', 'spring', or 'fall'.")
            return

        self.weather_data['humidity'] = random.uniform(30, 90)
        self.weather_data['precipitation'] = random.uniform(0, 100)  # percentage chance of rain
        self.weather_data['wind_speed'] = random.uniform(0, 20)  # km/h

    def display_weather(self):
        print(f"Weather Report for {self.location} during {self.season}:")
        print(f"Temperature: {self.weather_data['temperature']:.2f}°C")
        print(f"Humidity: {self.weather_data['humidity']:.2f}%")
        print(f"Precipitation Chance: {self.weather_data['precipitation']:.2f}%")
        print(f"Wind Speed: {self.weather_data['wind_speed']:.2f} km/h")

if __name__ == "__main__":
    location = input("Enter the location: ")
    season = input("Enter the season (winter, summer, spring, fall): ").lower()

    simulator = WeatherSimulator(location, season)
    simulator.generate_weather()
    simulator.display_weather()
