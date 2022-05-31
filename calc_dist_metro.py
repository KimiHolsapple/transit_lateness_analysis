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
df = pd.read_csv('/Users/kimigrace/Desktop/Math140/final_project/metro_bus_with_schedule_df.csv')

print(df)

g = sns.FacetGrid(df, row="bus_id", col="stop_id")
g.map(plt.hist, "minutes_late", bins=np.arange(-30, 30))
g.set_titles('{col_name} {row_name}')
g.set_axis_labels('minutes late', 'number of buses');

plt.show()

