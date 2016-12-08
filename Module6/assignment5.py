import pandas as pd


#https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.names


# 
# TODO: Load up the mushroom dataset into dataframe 'X'
# Verify you did it properly.
# Indices shouldn't be doubled.
# Header information is on the dataset's website at the UCI ML Repo
# Check NA Encoding
#
# .. your code here ..

raw_col_names = [
    'class', 'cap_shape', 'cap_surface', 'cap_color', 'bruises', 'odor',
    'gill_attach', 'gill_spacing', 'gill_size', 'gill_color', 'stalk_shape',
    'stalk_root', 'stalk_surface_above_ring', 'stalk_surface_below_ring',
    'stalk_color_above_ring', 'stalk_color_below_ring', 'viel_type',
    'viel_color', 'ring_number', 'ring_type', 'spore_print_color',
    'population', 'habitat'
]

X = pd.read_csv('Datasets/agaricus-lepiota.data', names=raw_col_names, na_values='?')


# INFO: An easy way to show which rows have nans in them
# print(X[pd.isnull(X).any(axis=1)])


# 
# TODO: Go ahead and drop any row with a nan
#
# .. your code here ..

X = X.dropna(axis=0)


#
# TODO: Copy the labels out of the dset into variable 'y' then Remove
# them from X. Encode the labels, using the .map() trick we showed
# you in Module 5 -- canadian:0, kama:1, and rosa:2
#
# .. your code here ..

y = X.loc[:, 'class']
X.drop(labels='class', axis=1, inplace=True)

y = y.map({'p': 0, 'e': 1})



#
# TODO: Encode the entire dataset using dummies
#
# .. your code here ..

X = pd.get_dummies(X)


# 
# TODO: Split your data into test / train sets
# Your test size can be 30% with random_state 7
# Use variable names: X_train, X_test, y_train, y_test
#
# .. your code here ..

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=7)



#
# TODO: Create an DT classifier. No need to set any parameters
#
# .. your code here ..

from sklearn import tree

model = tree.DecisionTreeClassifier()

 
#
# TODO: train the classifier on the training data / labels:
# TODO: score the classifier on the testing data / labels:
#
# .. your code here ..
 
model = model.fit(X_train, y_train)
score = model.score(X_test, y_test)
 
 
print('High-Dimensionality Score: ', round((score*100), 3))


#
# TODO: Use the code on the courses SciKit-Learn page to output a .DOT file
# Then render the .DOT to .PNGs. Ensure you have graphviz installed.
# If not, `brew install graphviz. If you can't, use: http://webgraphviz.com/
#
# .. your code here ..

tree.export_graphviz(model.tree_, out_file='tree.dot', feature_names=X_train.columns)

from subprocess import call

call(['dot', '-T', 'png', 'tree.dot', '-o', 'tree.png'])


