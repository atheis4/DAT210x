import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

from pandas.tools.plotting import andrews_curves

# Look pretty...
matplotlib.style.use('ggplot')


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
# .. your code here ..

df = pd.read_csv('Datasets/wheat.data')

#
# TODO: Drop the 'id', 'area', and 'perimeter' feature
# 
# .. your code here ..

df = df.drop(labels=['id'], axis=1)

#
# TODO: Plot a parallel coordinates chart grouped by
# the 'wheat_type' feature. Be sure to set the optional
# display parameter alpha to 0.4
# 
# .. your code here ..

plt.figure()
andrews_curves(df, 'wheat_type', alpha=0.4)

plt.show()


