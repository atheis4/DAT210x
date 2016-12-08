import pandas as pd
from datetime import timedelta
import matplotlib.pyplot as plt
import matplotlib

matplotlib.style.use('ggplot') # Look Pretty

#
# INFO: This dataset has call records for 10 users tracked over the course of 3 years.
# Your job is to find out where the users likely live at!



#def showandtell(title=None):
#    if title != None: plt.savefig(title + ".png", bbox_inches='tight', dpi=300)
#    plt.show()

def clusterInfo(model):
    print('Cluster Analysis Inertia: ', model.inertia_)
    print('------------------------------------------')
    for i in range(len(model.cluster_centers_)):
        print('\n  Cluster ', i)
        print('    Centroid ', model.cluster_centers_[i])
        print('    #Samples ', (model.labels_==i).sum()) # NumPy Power

# Find the cluster with the least # attached nodes
def clusterWithFewestSamples(model):
    # Ensure there's at least on cluster...
    minSamples = len(model.labels_)
    minCluster = 0
    for i in range(len(model.cluster_centers_)):
        if minSamples > (model.labels_==i).sum():
            minCluster = i
            minSamples = (model.labels_==i).sum()
    print('\n  Cluster With Fewest Samples: ', minCluster)
    return (model.labels_==minCluster)


def doKMeans(data, clusters=0):
    #
    # TODO: Be sure to only feed in Lat and Lon coordinates to the KMeans algo, since none of the other
    # data is suitable for your purposes. Since both Lat and Lon are (approximately) on the same scale,
    # no feature scaling is required. Print out the centroid locations and add them onto your scatter
    # plot. Use a distinguishable marker and color.
    #
    # Hint: Make sure you fit ONLY the coordinates, and in the CORRECT order (lat first).
    # This is part of your domain expertise.
    #
    # .. your code here ..
    from sklearn.cluster import KMeans
    
    model = KMeans(n_clusters=clusters)

    data = data.loc[:, ['TowerLat', 'TowerLon']]
    model.fit(data)
    
    return model



#
# TODO: Load up the dataset and take a peek at its head and dtypes.
# Convert the date using pd.to_datetime, and the time using pd.to_timedelta
#
# .. your code here ..

df = pd.read_csv('Datasets/CDR.csv')

df.CallDate = pd.to_datetime(df.CallDate, infer_datetime_format=True, errors='coerce')
df.CallTime = pd.to_timedelta(df.CallTime, errors='coerce')

df = df[(df.DOW != 'Sat') & (df.DOW != 'Sun')]
df = df[(df.CallTime < '17:00:00')]

df.reset_index()


#
# TODO: Get a distinct list of "In" phone numbers (users) and store the values in a
# regular python list.
# Hint: https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.tolist.html
#
# .. your code here ..

users = df.In.unique().tolist()


print('\n\nExamining person: ', 0)

# 
# TODO: Create a slice called user1 that filters to only include dataset records where the
# "In" feature (user phone number) is equal to the first number on your unique list above
#
# .. your code here ..

user1 = df[df.In == users[0]]
user1 = user1.reset_index()

#
# TODO: Alter your slice so that it includes only Weekday (Mon-Fri) values.
#
# .. your code here ..


#
# TODO: The idea is that the call was placed before 5pm. From Midnight-730a, the user is
# probably sleeping and won't call / wake up to take a call. There should be a brief time
# in the morning during their commute to work, then they'll spend the entire day at work.
# So the assumption is that most of the time is spent either at work, or in 2nd, at home.
#
# .. your code here ..


#
# TODO: Plot the Cell Towers the user connected to
#
# .. your code here ..

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(user1.TowerLat, user1.TowerLon, c='blue', marker='o', alpha=0.1)




#
# INFO: Run K-Means with K=3 or K=4. There really should only be a two areas of concentration. If you
# notice multiple areas that are "hot" (multiple areas the usr spends a lot of time at that are FAR
# apart from one another), then increase K=5, with the goal being that all centroids except two will
# sweep up the annoying outliers and not-home, not-work travel occasions. the other two will zero in
# on the user's approximate home location and work locations. Or rather the location of the cell
# tower closest to them.....


model = doKMeans(user1, 3)

print()
print(model.labels_)
print(model.cluster_centers_)
print()

ax.scatter(model.cluster_centers_[:, 0], model.cluster_centers_[:, 1], s=169, c='red', marker='x', alpha=0.8, linewidths=2)


#
# INFO: Print out the mean CallTime value for the samples belonging to the cluster with the LEAST
# samples attached to it. If our logic is correct, the cluster with the MOST samples will be work.
# The cluster with the 2nd most samples will be home. And the K=3 cluster with the least samples
# should be somewhere in between the two. What time, on average, is the user in between home and
# work, between the midnight and 5pm?

midWayClusterIndices = clusterWithFewestSamples(model)
midWaySamples = user1[midWayClusterIndices]

print('    Its Waypoint Time: ', midWaySamples.CallTime.mean())


#
# Let's visualize the results!
# First draw the X's for the clusters:

#ax.scatter(model.cluster_centers_[:,1], model.cluster_centers_[:,0], s=169, c='r', marker='x', alpha=0.8, linewidths=2)

#
# Then save the results:
#showandtell('Weekday Calls Centroids')  # Comment this line out when you're ready to proceed
