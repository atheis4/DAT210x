import pandas as pd


# TODO: Load up the table, and extract the dataset
# out of it. If you're having issues with this, look
# carefully at the sample code provided in the reading
#
# .. your code here ..

df = pd.read_html('http://www.espn.com/nhl/statistics/player/_/stat/points/sort/points/year/2015/seasontype/2', header=1)[0]

print(df.head(5))


# TODO: Rename the columns so that they match the
# column definitions provided to you on the website
#
# .. your code here ..

col_names = ['RK', 'Player', 'Team', 'Games Played', 'Goals', 'Assists',
             'Points', 'Plus/Minus Rating', 'Penalty Minutes',
             'Points Per Game', 'Shots on Goal', 'Shooting Percentage',
             'Game-Winning Goals', 'Power-Play Goals', 'Power-Play Assists',
             'Short-Handed Goals', 'Short-Handed Assists']

df.columns = col_names

print(df.head(5))


# TODO: Get rid of any row that has at least 4 NANs in it
#
# .. your code here ..

df = df.dropna(axis=0, thresh=4)


# TODO: At this point, look through your dataset by printing
# it. There probably still are some erroneous rows in there.
# What indexing command(s) can you use to select all rows
# EXCEPT those rows?
#
# .. your code here ..

print(df)
df = df[df.Player != 'PLAYER']
print(df)

# TODO: Get rid of the 'RK' column
#
# .. your code here ..

df = df.drop(labels=['RK'], axis=1)
print(df)


# TODO: Ensure there are no holes in your index by resetting
# it. By the way, don't store the original index
#
# .. your code here ..

df = df.reset_index(drop=True)


# TODO: Check the data type of all columns, and ensure those
# that should be numeric are numeric

print(df.dtypes)

for i in range(2, len(df.columns)):
    df.iloc[:, i] = pd.to_numeric(df.iloc[:, i], errors='coerce')
    
print(df.dtypes)


# TODO: Your dataframe is now ready! Use the appropriate 
# commands to answer the questions on the course lab page.

pct_unique = df.iloc[:, 10].unique()
print(pct_unique)

added = df.iloc[15, 2] + df.iloc[16, 2]