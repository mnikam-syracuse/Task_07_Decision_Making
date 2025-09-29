import pandas as pd

df = pd.read_csv('../data/raw_data.csv')
# Sensitivity: remove top 2 games by mean
game_means = df.groupby('id')['value'].mean().sort_values(ascending=False)
top2 = game_means.head(2).index.tolist()
sens = df[~df['id'].isin(top2)]
print('Original mean:', df['value'].mean())
print('Sensitivity mean:', sens['value'].mean())
