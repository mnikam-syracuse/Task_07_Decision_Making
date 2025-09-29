import pandas as pd
import numpy as np

df = pd.read_csv('../data/raw_data.csv')
values = df['value'].values
rng = np.random.default_rng(123)
boot_means = [rng.choice(values, size=len(values), replace=True).mean() for _ in range(1000)]
ci = np.percentile(boot_means,[2.5,97.5])
print('Bootstrap 95% CI:',ci)
