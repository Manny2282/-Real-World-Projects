# Wemby 

import pandas as pd
import numpy as np 
import seaborn as snb
import matplotlib.pyplot as plt


# Dataframe creation for Wemby's 2025 game stats

wemby_2025 = pd.DataFrame({
    'points' : [40 , 29, 31],
    'rebound':[15 , 11 , 14],
    'assist' : [1 , 2 , 4],
    'blocks' : [3 , 9 , 6],
    'fouls' : [4 , 6 , 3],
    'turnovers' : [0 , 0 , 2],
    '3-point_attempted': [2 , 3 , 6],
    '3-point_made' : [1 , 0 , 3],
    'free_throw_attempted' : [11 , 4 , 15],
    'free_throw_made' : [9 , 3 , 10]

})

wemby_2025.head()
wemby_2025.describe()
wemby_2025.info()

# Load the game log data
file_path = 'wemby_game_log.txt'
df = pd.read_csv(file_path)

# Check length and structure of the data
print(df.columns.to_list())
print(df.head(10))
print(df.describe())
print("n/Info: ")
print(df.info())

#Load 2023-2024 game stats
file_path_2 = 'wemby_2023_24_game_log.txt' 
df2 = pd.read_csv(file_path_2)

# Check length and structure
print(df2.columns.to_list())
print(df2.head(10))
print(df2.describe())
print("n/Info: ")
print(df2.info())



# Avg stats per season
avg_pts_2023 = df['points'].mean()
avg_pts_2024 = df2['points'].mean()
avg_pts_2025 = wemby_2025['points'].mean()

print("Average points in 2023-2024 season: ")
print(avg_pts_2023)
print("Average points in 2024-2025 season: ")
print(avg_pts_2024)
print("Average points in first 3 games of 2025 season: ")
print(avg_pts_2025)

avg_reb_2023 = df['rebounds'].mean()
avg_reb_2024 = df2['rebounds'].mean()
avg_reb_2025 = wemby_2025['rebound'].mean()

print("Avergae rebounds in 2023-2024 season: ")
print(avg_reb_2023)
print("Average rebounds in 2024-2025 season: ")
print(avg_reb_2024)
print("Average rebounds in first 3 games of 2025 season: ")
print(avg_reb_2025)

avg_ast_2023 = df['assists'].mean()
avg_ast_2024 = df2['assists'].mean()
avg_ast_2025 = wemby_2025['assist'].mean()

print("Average assists in 2023-2024 season: ")
print(avg_ast_2023)
print("Average assists in 2024-2025 season: ")
print(avg_ast_2024)
print("Average assists in first 3 games of 2025 season: ")
print(avg_ast_2025)

avg_fta_2023 = df['free_throw_attempted'].mean()
avg_fta_2024 = df2['free_throw_attempted'].mean()
avg_fta_2025 = wemby_2025['free_throw_attempted'].mean()

print("Average free throw attempts in 2023-2024 season: ")
print(avg_fta_2023)
print("Average free throw attempts in 2024-2025 season: ")
print(avg_fta_2024)
print("Average free throw attempts in first 3 games 2025 season: ")
print(avg_fta_2025)

avg_ftm_2023 = df['free_throw_made'].mean()
avg_ftm_2024 = df2['free_throw_made'].mean()
avg_ftm_2025 = wemby_2025['free_throw_made'].mean()

print("Average free throw made in 2023-2024 season: ")
print(avg_ftm_2023)
print("Average free throw made in 2024-2025 season: ")
print(avg_ftm_2024)
print("Average free throw made in first 3 games of 2025 season: ")
print(avg_ftm_2025)



#Visualization of Wemby avgs 
snb.barplot(x=['2023-2024', '2024-2025', '2025-2026'], y=[avg_pts_2023, avg_pts_2024, avg_pts_2025])

# visualization of Wemby performance trends
snb.lineplot(data=df, x='game', y='points', label='2024-2025 Season')
snb.lineplot(data=df2, x='game', y='points', label='2023-2024 Season')
plt.title('Wemby Points per Game Comparison: 2023-2024 vs 2024-2025')
plt.show()


snb.barplot(x=['2023-2024', '2024-2025', '2025-2026'], y=[avg_reb_2023, avg_reb_2024, avg_reb_2025])
plt.title('Wemby Average Rebounds per Season Comparison')
snb.lineplot(data=df, x='game', y='rebounds', label='2024-2025 Season')
snb.lineplot(data=df2, x='game', y='rebounds', label='2023-2024 Season')
plt.title('Wemby Rebounds per Game Comparison: 2023-2024 vs 2024-2025')
plt.show()

snb.barplot(x=['2023-2024', '2024-2025', '2025-2026'], y=[avg_ast_2023, avg_ast_2024, avg_ast_2025])
plt.title('Wemby Average Assists per Season Comparison')
snb.lineplot(data=df, x='game', y= 'assists', label= '2024-2025 Season')
snb.lineplot(data=df2, x='game', y='assists', label='2023-2024 Season')
plt.title('Wemby Assists per Game Comparison: 2023-2024 vs 2024-2025')
plt.show()

# Rolling average visualization points
df['points_avg_five']= df['points'].rolling(window=5).mean()
df2['points_avg_five']= df2['points'].rolling(window=5).mean()
snb.lineplot(data=df, x='game', y='points_avg_five', label='2024-2025 Season')
snb.lineplot(data=df2, x='game', y='points_avg_five', label='2023-2024 Season')
plt.title('Wemby 5-Game Rolling Average Points: 2023-2024 vs 2024-2025')
plt.show()

df['rebounds_avg_five']= df['rebounds'].rolling(window=5).mean()
df2['rebounds_avg_five']= df2['rebounds'].rolling(window=5).mean()
snb.lineplot(data=df, x='game', y='rebounds_avg_five', label='2024-2025 Season')
snb.lineplot(data=df2, x='game',y='rebounds_avg_five', label='2023-2024 Season')
plt.title('Wemby 5-Game Rolling Average Rebounds: 2023-2024 vs 2024-2025')
plt.show()

df['assists_avg_five']= df['assists'].rolling(window=5).mean()
df2['assists_avg_five']= df2['assists'].rolling(window=5).mean()
snb.lineplot(data=df, x='game', y='assists_avg_five', label='2024-2025 Season')
snb.lineplot(data=df2, x='game', y='assists_avg_five', label='2023-2024 Season')
plt.title('Wemby 5-Game Rolling Average Assists: 2023-2024 vs 2024-2025')
plt.show()

df['fta_avg_five']= df['free_throw_attempted'].rolling(window=5).mean()
df2['fta_avg_five']= df2['free_throw_attempted'].rolling(window=5).mean()
snb.lineplot(data=df, x='game', y='fta_avg_five', lable= '2024-2025 season')
snb.lineplot(data=df, x='game', y='fta_avg_five', label='2023-2024 Season')
plt.title('Wemby 5-Game Rolling Average Free Throws Attempted: 2023-2024 vs 2024-2025')
plt.show()

df['ftm_avg_five']= df['free_throw_made'].rolling(window=5).mean()
df2['fta_avg_five']= df2['free_throw_made'].rolling(window=5).mean()
snb.lineplot(data=df, x='game', y='fta_avg_five', label= '2024-2025 season')
snb.lineplot(data=df2, x='game', y='fta_avg_five', label= '2023-2024 season')
plt.title('Wemby 5-Game Rolling Average Free Throws Made ')
plt.show()
