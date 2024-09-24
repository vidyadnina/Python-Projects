import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Importing data
workout_df = pd.read_csv("data/workout.csv")
keywords_df = pd.read_csv("data/three_keywords.csv")
workout_geo_df = pd.read_csv("data/workout_geo.csv")
keywords_geo_df = pd.read_csv("data/three_keywords_geo.csv")

# When was the global search for 'workout' at its peak?
plt.figure(figsize=(15,5))
plt.plot(workout_df['month'], workout_df['workout_worldwide'])
plt.xticks(rotation=90)

# workout_df.plot(x= 'month', y= 'workout_worldwide', rot=90,figsize=(12,5))

max_index_workout = np.argmax(workout_df['workout_worldwide'])
max_workout = workout_df['workout_worldwide'][max_index_workout]
max_month = workout_df['month'][max_index_workout]

year_str = str(pd.to_datetime(max_month).year)

# What was the most popular keyword during the covid pandemic?
# plt.plot(keywords_df['month'])
# plt.xticks(rotation=90)
# plt.figure(figsize=(15,5))
# plt.show()
# keywords_df.plot(x='month')
# peak_covid = 'home workout'
# current = 'gym workout'

def peak_covid():
    keywords_df['year'] = pd.to_datetime(keywords_df['month']).dt.year
    max_home_covid = keywords_df['home_workout_worldwide'][(keywords_df['year'] == 2019) | (keywords_df['year'] == 2020)].max()
    max_gym_covid = keywords_df['gym_workout_worldwide'][(keywords_df['year'] == 2019) | (keywords_df['year'] == 2020)].max()
    max_homegym_covid = keywords_df['home_gym_worldwide'][(keywords_df['year'] == 2019) | (keywords_df['year'] == 2020)].max()
    if max_home_covid > max_gym_covid and max_home_covid > max_homegym_covid:
        print('The most popular workout type during covid was home workout')
    elif max_gym_covid > max_home_covid and max_gym_covid > max_homegym_covid:
        print('The most popular workout type during covid was gym workout')
    else:
        print('The most popular workout type during covid was home gym')
    

# What country has the highest interest for workouts?
top_country = workout_geo_df.loc[workout_geo_df['workout_2018_2023'].idxmax(), 'country']

# Between Philippines and Malaysia, Which of the two countries has the highest interest in home workouts?
keywords_phimalay = keywords_geo_df[(keywords_geo_df['Country'] == "Philippines") | (keywords_geo_df['Country'] == "Malaysia")]
home_workout_geo = keywords_geo_df.loc[keywords_phimalay['home_workout_2018_2023'].idxmax(), 'Country']
print(home_workout_geo)
