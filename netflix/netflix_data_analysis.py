import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt, figure

import re

net_df = pd.read_csv('netflix_titles.csv')

print(net_df.info)
print(net_df.describe())  # what does these two do? ifo and describe..
print(net_df.head())
print(net_df.columns)

print("1.How many content?->", net_df['show_id'].count())
print("2.How many Movies?->", net_df[net_df['type'] == 'Movie']['show_id'].count())
print("3.How many TV Shows?->", net_df[net_df['type'] == 'TV Show']['show_id'].count())

# ---------------- comparison between movies and tv shows ----------------#

fig = sns.FacetGrid(net_df, hue='type', aspect=4)
fig.map(sns.kdeplot, 'release_year', shade=False)
fig.add_legend()
plt.show()

# --------------Top 10 Countries with most and least number no.of TV shows and Movies--------------------#

query1 = net_df.title.groupby([net_df.type, net_df.country]).count()
print(query1, query1.index)
sub_query1 = query1[('Movie',)].sort_values(ascending=False)[:10]
print(sub_query1)
sns.barplot(y=sub_query1.index, x=sub_query1.values)
plt.title("Top 10 Countries with most no.of Movies")
plt.show()

sub_query2 = query1[('TV Show',)].sort_values(ascending=False)[:10]
print(sub_query2)
sns.barplot(x=sub_query2.index, y=sub_query2.values)
plt.xticks(rotation='vertical')
plt.title("Top 10 Countries with most number TV shows")
plt.show()

sub_query3 = query1['Movie'].sort_values()[:10]
print(sub_query3)
plt.figure(figsize=(10, 6))
plt.title("Top 10 Countries with least number of Movies")
sns.barplot(x=sub_query3.values, y=sub_query3.index)
plt.show()

sub_query4 = query1['TV Show'].sort_values()[:10]
plt.figure(figsize=(10, 6))
plt.title("Top 10 Countries with least number of TV Shows!")
sns.barplot(x=sub_query4.values, y=sub_query4.index)
plt.show()

#  -----------------------Movie Duration Distribution(seasons) ------------------------------ #

tv_shows_df = net_df[net_df['type'] == 'TV Show']
# print(tv_shows_df)
tv_shows_df['duration'] = tv_shows_df['duration'].apply(lambda x: (re.search(r'\d+', x)).group()).astype(dtype=int)
# print(tv_shows_df['duration'])
# print(type(tv_shows_df))

# Duration Distribution of TV Shows(no. of seasons)
plt.title("Duration Distribution of TV Shows(no. of seasons)")
sns.countplot(x='duration', data=tv_shows_df)
plt.show()

# Top 10 TV Shows having most seasons
top_10 = tv_shows_df['duration'].groupby(tv_shows_df['title']).obtained_credit().sort_values(ascending=False)[:10]
print(top_10)
plt.title("Top 10 TV Shows having most seasons")
sns.barplot(x=top_10.values, y=top_10.index)
plt.show()

# Duration Distribution of Movies
movie = net_df[net_df['type'] == 'Movie']
# print(movie)
movie = movie.dropna()
movie = movie.sort_values(by='duration', ascending=False)
# print(movie)
movie['duration'] = movie['duration'].apply(lambda x: re.search(r'\d+', x).group()).astype(dtype=int)

sns.displot(movie['duration'])  # better visualization than sns.countplot()
plt.title("Duration Distribution of Movies( displot)")
plt.show()

# Movies of longest minutes
top_10_movie = movie[:10]
plt.title("Movies of longest minutes", loc='right')
sns.barplot(x=top_10_movie['duration'], y=top_10_movie['title'])
plt.show()

# Top 10 years with most number of movies and series
top_years = net_df['title'].groupby(net_df['release_year']).count()
# print(top_years)
top_10_years = top_years.sort_values(ascending=False)[:10]
# print(top_10_years)

sns.barplot(x=top_10_years.index, y=top_10_years.values)
plt.title("Top 10 years with most number of movies and series")
plt.show()

# -----------------------Director with most no.of movies and series-------------------- #

print("--------Director with most no.of movies and series-----------")
net_df = net_df.drop('director', axis=1).join(
    net_df['director'].str.split(',', expand=True).stack().reset_index(level=1, drop=True).rename('director'))
d = net_df.dropna()
# print(d)

# Director with most no.of movies
dd = net_df[net_df['type'] == 'Movie']['director'].value_counts()[:10]
print(dd)
sns.barplot(y=dd.index, x=dd.values)
plt.title("Director with most no.of movies")
plt.show()

# Director with most no.of TV Shows
dd = net_df[net_df['type'] == 'TV Show']['director'].value_counts()[:10]
print(dd)
sns.barplot(y=dd.index, x=dd.values)
plt.title("Director with most no.of TV Shows")
plt.show()

# Countries with most number of movies and TV shows
print("--Countries with most number of movies and TV Shows--")
net_df = net_df.drop('country', axis=1).join(
    net_df['country'].str.split(',', expand=True).stack().reset_index(level=1, drop=True).rename('country'))
print(net_df)

# movies

cntry_movie = net_df[net_df['type'] == 'Movie']
# print(cntry_movie)
c = cntry_movie['title'].groupby(cntry_movie['country']).count().sort_values(ascending=False)[:10]
print(c)
sns.barplot(x=c.values, y=c.index)
plt.title("Countries with most number of movies")
plt.show()

# TV shows
print("--Countries with most number of TV shows--")
cntry_tvshow = net_df[net_df['type'] == 'TV Show']
t = cntry_tvshow['title'].groupby(cntry_tvshow['country']).count().sort_values(ascending=False)[:10]
sns.barplot(y=t.index, x=t.values)
plt.title("Countries with most number of TV Shows")
plt.show()
