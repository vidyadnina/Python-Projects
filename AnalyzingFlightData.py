# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Problems:
#     1. Calculate average departure delay per routes and highest number of canceled flights, store as a DF routes_delays_cancels.
#     2. Determine the avg aperture delays per airlines and highest number of canceled flights, store as a DF airlines_delays_cancels.
#     3. Create 2 bar graphs: 1. show the highest number of cancellations by route called top9_route_cancels_bar 2.  highest average departure delays by airline called top9_airline_delays_bar
#     4. Determine if 10 mile per hour wind gusts or more have a larger average departure delay for both of SEA and PDX, setting wind_response to True if so and False if not.

flights_df = pd.read_csv("flights2022.csv")
flights_weather_df = pd.read_csv("flights_weather2022.csv")

flights_df['route'] = flights_df['origin'] + "-" + flights_df['dest']

# avg_dep_delays_route = flights_df.groupby('route')['dep_delay'].mean().rename("avg_dep_delays").reset_index()

# max_cancels = flights_df[flights_df['dep_time'].isna()].groupby('route').size().reset_index(name='cancelled_flights')

# routes_delays_cancels = pd.merge(avg_dep_delays_route, max_cancels, on='route', how='left')

routes_delays_cancels = flights_df.groupby('route').agg(
    avg_dep_delay=("dep_delay", "mean"),
    total_cancellations=("dep_time", lambda x: x.isna().sum())
).reset_index()

airlines_delays_cancels = flights_df.groupby("airline").agg(
    avg_dep_delay=("dep_delay", "mean"),
    total_cancellations=("dep_time", lambda x: x.isna().sum())
).reset_index()

top_routes_by_cancellations_route_cancels = routes_delays_cancels.sort_values(by='total_cancellations', ascending=False).head(9)

top_airlines_by_cancellations = airlines_delays_cancels.sort_values(by='total_cancellations', ascending=False).head(9)

plt.figure(figsize=(10, 5))
plt.bar(top9_route_cancels['route'], top9_route_cancels['cancelled_flights'])
plt.title('Top 9 Routes by Number of Cancellations')
plt.xlabel('Route')
plt.ylabel('Number of Cancellations')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 5))
plt.bar(top9_airline_cancels['airline'], top9_airline_cancels['cancelled_flights'])
plt.title('Top 9 Airlines by Number of Cancellations')
plt.xlabel('Airline')
plt.ylabel('Number of Cancellations')
plt.xticks(rotation=45)
plt.show()

flights_weather_df["group"] = flights_weather_df["wind_gust"].apply(lambda x: ">= 10mph" if x >= 10 else "< 10 mph")

wind_grouped_data = flights_weather_df.groupby(["group", "origin"]).agg(
    mean_dep_delay=("dep_delay", "mean")
).reset_index()

# Determine if 10 mile per hour wind gusts or more have a larger average departure delay for both SEA and PDX
sea_wind_delay = wind_grouped_data[(wind_grouped_data['origin'] == 'SEA') & (wind_grouped_data['group'] == '>= 10mph')]['mean_dep_delay'].values[0]
pdx_wind_delay = wind_grouped_data[(wind_grouped_data['origin'] == 'PDX') & (wind_grouped_data['group'] == '>= 10mph')]['mean_dep_delay'].values[0]

sea_no_wind_delay = wind_grouped_data[(wind_grouped_data['origin'] == 'SEA') & (wind_grouped_data['group'] == '< 10 mph')]['mean_dep_delay'].values[0]
pdx_no_wind_delay = wind_grouped_data[(wind_grouped_data['origin'] == 'PDX') & (wind_grouped_data['group'] == '< 10 mph')]['mean_dep_delay'].values[0]

wind_response = (sea_wind_delay > sea_no_wind_delay) and (pdx_wind_delay > pdx_no_wind_delay)
print("Wind response:", wind_response)

