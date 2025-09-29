import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('../data/raw_data.csv')
print(df.groupby('game_minute')['value'].describe())
