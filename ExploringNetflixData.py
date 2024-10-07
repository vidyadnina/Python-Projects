import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

netflix_df = pd.read_csv("netflix_data.csv")

# checking the latest and newest years movies were released
min_year = netflix_df['release_year'].min()
max_year = netflix_df['release_year'].max()

# creating new dataset for movies released in the 90s
netflix_df_1990 = netflix_df[(netflix_df['release_year'] <2000) & (netflix_df['release_year']>=1990) & (netflix_df['type'] == 'Movie')]

# checking which duration was the most frequent
duration_counts = netflix_df_1990.groupby('duration').size().reset_index(name='count').sort_values(by='count', ascending=False)
duration = int(duration_counts.iloc[0]['duration'])


# counting number of short movies
short_movie_count = netflix_df_1990[(netflix_df_1990['duration'] < 90) & (netflix_df_1990['genre'] == 'Action')]['duration'].count()

# printing results
print(f"Count of short action movies with durations less than 90: {short_movie_count}")
print(f"The most frequent movie duration: {duration}")
