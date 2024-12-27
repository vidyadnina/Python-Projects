import pandas as pd
import matplotlib.pyplot as plt

# Load the datasets
flights_data = pd.read_csv('/mnt/data/flights2022.csv', usecols=['year', 'month', 'day', 'origin', 'arr_delay'])
weather_data = pd.read_csv('/mnt/data/flights_weather2022.csv', usecols=['year', 'month', 'day', 'origin', 'temp'])

# ---- Busiest Routes Analysis ----
# Group by origin and destination
busiest_routes = flights_data.groupby(['origin', 'dest']).size().reset_index(name='flight_count')
busiest_routes = busiest_routes.sort_values(by='flight_count', ascending=False).head(10)

# ---- Peak Periods Analysis ----
# Aggregate flights by month
flights_by_month = flights_data.groupby('month').size().reset_index(name='flight_count')

# Aggregate flights by hour
flights_by_hour = flights_data.groupby('hour').size().reset_index(name='flight_count')

# ---- Delay Analysis ----
# Calculate average delay by airline
average_delays = flights_data.groupby('airline')['arr_delay'].mean().reset_index()
average_delays = average_delays.sort_values(by='arr_delay', ascending=False)

# ---- Weather Impact Analysis ----
# Pre-aggregate weather data by origin and day
weather_aggregated = weather_data.groupby(['year', 'month', 'day', 'origin'])['temp'].mean().reset_index()

# Pre-aggregate flight delays by origin and day
flights_aggregated = flights_data.groupby(['year', 'month', 'day', 'origin'])['arr_delay'].mean().reset_index()

# Merge the aggregated data
merged_aggregated = pd.merge(flights_aggregated, weather_aggregated, on=['year', 'month', 'day', 'origin'])

# Analyze delays based on weather conditions (e.g., temperature)
weather_impact = merged_aggregated.groupby('temp')['arr_delay'].mean().reset_index()

# ---- Visualizations ----
plt.figure(figsize=(10, 6))

# Plot busiest routes
plt.barh(busiest_routes['origin'] + ' - ' + busiest_routes['dest'], busiest_routes['flight_count'], color='skyblue')
plt.xlabel('Number of Flights')
plt.ylabel('Route')
plt.title('Top 10 Busiest Routes')
plt.gca().invert_yaxis()
plt.show()

# Plot monthly trends
plt.figure(figsize=(10, 6))
plt.plot(flights_by_month['month'], flights_by_month['flight_count'], marker='o', linestyle='-', color='blue')
plt.xlabel('Month')
plt.ylabel('Number of Flights')
plt.title('Monthly Flight Trends')
plt.grid()
plt.show()

# Plot hourly trends
plt.figure(figsize=(10, 6))
plt.bar(flights_by_hour['hour'], flights_by_hour['flight_count'], color='orange')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Flights')
plt.title('Hourly Flight Trends')
plt.xticks(range(0, 24))
plt.grid()
plt.show()

# Plot average delays by airline
plt.figure(figsize=(10, 6))
plt.barh(average_delays['airline'], average_delays['arr_delay'], color='green')
plt.xlabel('Average Arrival Delay (minutes)')
plt.ylabel('Airline')
plt.title('Average Arrival Delays by Airline')
plt.gca().invert_yaxis()
plt.show()

# Plot weather impact on delays
plt.figure(figsize=(10, 6))
plt.scatter(weather_impact['temp'], weather_impact['arr_delay'], color='red')
plt.xlabel('Temperature (°F)')
plt.ylabel('Average Arrival Delay (minutes)')
plt.title('Impact of Temperature on Arrival Delays')
plt.grid()
plt.show()
