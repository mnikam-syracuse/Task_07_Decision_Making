import pandas as pd
import numpy as np

df = pd.read_csv('../data/raw_data.csv')
for pos, group in df.groupby('position'):
    print(pos, group['value'].mean(), group['value'].std(), len(group))
