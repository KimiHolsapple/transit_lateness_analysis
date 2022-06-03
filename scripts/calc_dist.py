#Python script to generate 

## requires packages seaborn, openpyxl, and pandas
##
##

import pandas as pd
import seaborn as sns
import openpyxl
import matplotlib.pyplot as plt
import numpy as np


import pandas as pd
df = pd.read_csv('/Users/kimigrace/Desktop/Math140/final_project/loop_df_1.csv')

print(df)

g = sns.FacetGrid(df, row="direction", col="route")
g.map(plt.hist, "minutes_late", bins=np.arange(-1, 20))
g.set_titles('{col_name} {row_name}')
g.set_axis_labels('minutes late', 'number of buses');

plt.show()

