import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# ==== CONFIGURATION ====
API_KEY = '82666002a874972e310d753ff64c78d2'  # Replace this with your real API key
CITY = 'Chennai'
UNITS = 'metric'

# ==== API URL ====
url = f'https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units={UNITS}'

# ==== FETCH DATA ====
response = requests.get(url)
data = response.json()

# ==== CHECK FOR ERRORS ====
if response.status_code != 200:
    print("❌ API Error:", data.get("message", "Unknown error"))
    exit()

# ==== PARSE WEATHER DATA ====
timestamps = []
temperatures = []

for entry in data['list']:
    dt = datetime.strptime(entry['dt_txt'], '%Y-%m-%d %H:%M:%S')
    temp = entry['main']['temp']
    timestamps.append(dt)
    temperatures.append(temp)

# ==== VISUALIZATION ====
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))
plt.plot(timestamps, temperatures, marker='o', linestyle='-', color='teal')
plt.title(f'Temperature Forecast for {CITY}', fontsize=16)
plt.xlabel('Date and Time')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
