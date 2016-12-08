"""External program to create interactive 3D scatter plot."""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

from mpl_toolkits.mplot3d import Axes3D

df = pd.read_csv('Module3/Datasets/wheat.data')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df.width, df.groove, df.length, c='red')

plt.show()
