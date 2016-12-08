import pandas as pd

import matplotlib.pyplot as plt
import matplotlib

matplotlib.style.use('ggplot') # Look Pretty

def showandtell(title=None):
  plt.show()



df = pd.read_csv('Datasets/CDR.csv')

users = df.In.unique().tolist()
df.CallTime = pd.to_datetime(df.CallTime, infer_datetime_format=True, errors='coerce')
df = df[(df.DOW == 'Sat') | (df.DOW == 'Sun')]
df = df[(df.CallTime < '06:00:00') | (df.CallTime > '22:00:00')]

clusters = []

user = df[df.In == users[0]]

user.plot.scatter(x='TowerLon', y='TowerLat', c='gray', alpha=0.1, title='Call Locations')

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(user.TowerLat,user.TowerLon, c='g', marker='o', alpha=0.2)
ax.set_title('Weekend Calls (<6am or >10p)')


from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=2)
kmeans.fit(user.loc[:, ['TowerLat', 'TowerLon']])

clusters.append(kmeans.cluster_centers_)

ax.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='r', marker='x', s=168, alpha=0.7, linewidths=2)

print(kmeans.cluster_centers_)
    

showandtell()  # TODO: Comment this line out when you're ready to proceed

#
# TODO: Repeat the above steps for all 10 individuals, being sure to record their approximate home
# locations. You might want to use a for-loop, unless you enjoy typing.
#
# .. your code here ..

