#!/usr/bin/env python
# coding: utf-8

# In[26]:


import sqlite3 as sq
import pandas as pd
import numpy as np


# In[34]:


df_1 = pd.read_csv('/Users/sophiaweidner/Downloads/soccer_df1.csv')


# In[39]:


# Uploading DF1 to SQLite Database.
conn = sqlite3.connect('project_database')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS dataframe1 (date, home_team, away_team, home_score, away_score, city, country, total_score)')
conn.commit()

df_1.to_sql('dataframe1', conn, if_exists='replace', index = False)
 
c.execute('''  
SELECT * FROM dataframe1
          ''')

for row in c.fetchall():
    print (row)


# In[42]:


# Uploading dataframes 2, 3, and 4 - wiki tables.
df_2 = pd.read_csv('/Users/sophiaweidner/Downloads/df_2.csv')
df_3 = pd.read_csv('/Users/sophiaweidner/Downloads/df_3.csv')
df_4 = pd.read_csv('/Users/sophiaweidner/Downloads/df_4.csv')

c.execute('CREATE TABLE IF NOT EXISTS dataframe2 (Player, Transfers, Fees US, Fee UK Pounds)')
conn.commit()

df_2.to_sql('dataframe2', conn, if_exists='replace', index = False)
 
c.execute('''  
SELECT * FROM dataframe2
          ''')

for row in c.fetchall():
    print (row)


# In[44]:


c.execute('CREATE TABLE IF NOT EXISTS dataframe3 (Year, Player, Selling club, Buying club, FeeUS, FeeUK Pounds)')
conn.commit()

df_3.to_sql('dataframe3', conn, if_exists='replace', index = False)
 
c.execute('''  
SELECT * FROM dataframe3
          ''')

for row in c.fetchall():
    print (row)


# In[50]:


c.execute('CREATE TABLE IF NOT EXISTS dataframe4 (Rank, Player, TeamFrom, TeamTo, Position, Year, FeeUS, FeeUK Pounds)')
conn.commit()

df_4.to_sql('dataframe4', conn, if_exists='replace', index = False)
 
c.execute('''  
SELECT * FROM dataframe4
          ''')

for row in c.fetchall():
    print (row)


# In[53]:


# Uploading dataframe 5.
df_5 = pd.read_csv('/Users/sophiaweidner/Downloads/df_5.csv')

c.execute('CREATE TABLE IF NOT EXISTS dataframe5 (a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, a1, a2, a3, a4, a5, a6, a7, a8, a9, b2, b3, b4, b5)')
conn.commit()

df_5.to_sql('dataframe5', conn, if_exists='replace', index = False)
 
c.execute('''  
SELECT * FROM dataframe5
          ''')

for row in c.fetchall():
    print (row)


# In[69]:


# Join all datasets together into 1.

# I decided to join what I consider the big 3 dataframes, as there are a lot of repeated column names despite
# the data having different context. I left df_3 and df_4 off from being merged so I could create separate
# visualizations for those datapoints.

df_combo1 = pd.merge(df_2, df_5, on='Player')
df_combined = pd.concat([df_combo1, df_1], axis = 1, join = 'inner')


# In[70]:


df_combined.head()


# In[82]:


def merged():
    c.execute('CREATE TABLE combined AS SELECT * FROM dataframe1 t1 INNER JOIN dataframe2 t2 ON Player')
    for line in c.fetchall():
        print(line)
merged()


# In[83]:


conn.close()


# In[66]:


# Creating visualizations.
import matplotlib.pyplot as plt


# In[67]:


# Created two visualizations from the merged dataset, df_combined.
df_combined.columns.tolist()


# In[71]:


print(df_combined['Player'])


# In[84]:


# First, I am going to see which position each player plays to see if there's a pattern amongst the highest
# paid players.
plt.scatter(df_combined['Position'],df_combined['Player'], cmap="Greys")
plt.xlabel('Position')
plt.ylabel('Player')
plt.title('Highest Paid Players and their Positions')


# In[94]:


# I am now going to compare physical aspects of the players. I will compare their heights and their weights.
plt.plot(df_combined['Player'],df_combined['Height'])
plt.xlabel('Players')
plt.ylabel('Height')
plt.title('Players Heights')


# In[109]:


plt.plot(df_combined['Player'],df_combined['Weight'])
plt.xlabel('Players')
plt.ylabel('Weight')
plt.title('Player Weight')


# In[107]:


# I am going to compare the Nationality the players are compared to the money they made to see if there is a pattern
# amongst where they are from.
plt.scatter(df_combined['Nationality'],df_combined['Fees (US)'])
plt.xlabel('Nationality')
plt.ylabel('Fees in USD Thousands')
plt.title('The Nationality of Players vs. Fees in USD (Thousands)')


# In[111]:


# Lastly, I will compare the club Team versus the fees to look for a pattern.
plt.scatter(df_combined['Team'],df_combined['Fees (US)'])
plt.xlabel('Club Team')
plt.ylabel('Fees in USD Thousands')
plt.title('Club Teams and Fees')


# # Summary 
# 
# My goal in the beginning of this project was to compare players with the teams that they play on to determine the "success" of said team. In the end, I ended up taking a more player-based approach and compared the players and the amount of money that they made. My datasets were not conducive to my original approach, and in the end, I had a small dataset to work with which resulted in simple visualizations. If I could go back and do this over again, I think that I would've found a CSV file that had more details about players, as my wikitables and my API had bountiful information on players rather than teams. It is also difficult to determine the definition of "sucessful" player or team; and that does fall under the ethical implications of this project. Though there is a relationship between amount of pay and skill of a player, the highest paid athletes may not be the best, and skill is subjective to whoever is watching. I would need a clear defintion of success to continue into this analysis. Furthermore, I manipulated my datasets so much that I could have lost some important information along the way. For example, the API I used had information for all sports, and I only created a dataframe with the players' names that were from my wiki tables (mostly to keep my data consistent). I could have used that API to get more details regarding the club teams that those players are on. In summary, the amount of data manipulation I performed made this final milestone more of a struggle than it needed to be, and I feel as if I did not discover anything substantial. 

# In[ ]:




