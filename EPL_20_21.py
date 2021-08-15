#!/usr/bin/env python
# coding: utf-8

# In[40]:


#importing the libraries
import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go


# In[4]:


#raeding the data
data=pd.read_csv('EPL_20_21.csv')
data


# In[5]:


#handling the missing data
msno.matrix(data)


# In[7]:


#data is good there's no missing data
#Understaning the data
data.describe()


# In[9]:


#Top 10 goals scorers
fig_goal=px.bar(data.nlargest(10,'Goals')[['Name','Goals']],x='Name',y='Goals',color='Goals',
          title='Top 10 goals scorers')
fig_goal.show()


# In[11]:


#Top 10 Assists
fig=px.bar(data.nlargest(10,'Assists')[['Name','Assists']],
          x='Name',y='Assists',color='Assists',title='Top 10 kings of assists')
fig.show()


# In[10]:


#TOP 10 Players got red cards
fig_red=px.bar(data.nlargest(10,'Red_Cards')[['Name','Red_Cards']],
          x='Name',y='Red_Cards',color='Red_Cards',title='TOP 10 Players got red cards')
fig_red.show()


# In[11]:


#TOP 10 Players got yellow cards
fig_yellow=px.bar(data.nlargest(10,'Yellow_Cards')[['Name','Yellow_Cards']],
          x='Name',y='Yellow_Cards',color='Yellow_Cards',title='TOP 10 Players got yellow cards')
fig_yellow.show()


# In[12]:


#the most Goalkepers Played 
df_goalkeper=data[data['Position']=='GK']
fig=px.bar(df_goalkeper.nlargest(10,'Mins')[['Name','Mins']],
          x='Name',y='Mins',color='Mins',title='TOP 10 Goalkeeper starts')


fig.show()


# In[13]:


#the most defenders Played 
df_defenders=data[data['Position']=='DF']
fig=px.bar(df_defenders.nlargest(10,'Mins')[['Name','Mins']],
          x='Name',y='Mins',color='Mins',title='TOP 10 DF starts')


fig.show()


# In[14]:


#the most defenders assisted

fig=px.bar(df_defenders.nlargest(10,'Assists')[['Name','Assists']],
          x='Name',y='Assists',color='Assists',title='Top 10 DF kings of assists')
fig.show()


# In[15]:


#Expected NO of Assists that the DF would make it 
df_defenders['Expected Assists']=df_defenders['xA']*df_defenders['Matches']
fig=px.bar(df_defenders.nlargest(10,'Expected Assists')[['Name','Expected Assists','Assists']],
          x='Name',y=['Expected Assists','Assists'],color_discrete_map={'Expected Assists':'black','Assists':'white'},title='Compering the Number of expected Assits to The Actule number of Assists')
fig.show()


# In[16]:


#Top medfilders played 
df_med=data[data['Position'].str.contains("MF")]
fig=px.bar(df_med.nlargest(10,'Mins')[['Name','Mins']],
          x='Name',y='Mins',color='Mins',title='TOP 10 MF Played')


fig.show()


# In[17]:


#the most medfielders assisted

fig=px.bar(df_med.nlargest(10,'Assists')[['Name','Assists']],
          x='Name',y='Assists',color='Assists',title='Top 10 MF kings of assists')
fig.show()


# In[18]:


#the most medfielders scored goeals

fig=px.bar(df_med.nlargest(10,'Goals')[['Name','Goals']],
          x='Name',y='Goals',color='Goals',title='Top 10 MF scores goals')
fig.show()


# In[19]:


#Expected NO of Assists that the DF would make it 
df_med['Expected Assists']=df_med['xA']*df_med['Matches']
fig=px.bar(df_med.nlargest(10,'Expected Assists')[['Name','Expected Assists','Assists']],
          x='Name',y=['Expected Assists','Assists'],color_discrete_map={'Expected Assists':'black','Assists':'white'},title='Compering the Number of expected Assits to The Actule number of Assists')
fig.show()


# In[20]:


#Expected NO of Goals that the DF would make it 
df_med['Expected Goals']=df_med['xG']*df_med['Matches']
fig=px.bar(df_med.nlargest(10,'Expected Goals')[['Name','Expected Goals','Goals']],
          x='Name',y=['Expected Goals','Goals'],color_discrete_map={'Expected Goals':'black','Goals':'white'},title='Compering the Number of expected Goals to The Actule number of Goals')
fig.show()


# In[21]:


#Top forward played 
df_FW=data[data['Position'].str.contains("FW")]
fig=px.bar(df_med.nlargest(10,'Mins')[['Name','Mins']],
          x='Name',y='Mins',color='Mins',title='TOP 10 FW Played')


fig.show()


# In[22]:


#the most Forwards assisted

fig=px.bar(df_FW.nlargest(10,'Assists')[['Name','Assists']],
          x='Name',y='Assists',color='Assists',title='Top 10 FW kings of assists')
fig.show()


# In[23]:


#the most Forwards Scored

fig=px.bar(df_FW.nlargest(10,'Goals')[['Name','Goals']],
          x='Name',y='Goals',color='Goals',title='Top 10 FW kings of assists')
fig.show()


# In[24]:


#Expected NO of Assists that the FW would make it 
df_FW['Expected Assists']=df_FW['xA']*df_FW['Matches']
fig=px.bar(df_FW.nlargest(10,'Expected Assists')[['Name','Expected Assists','Assists']],
          x='Name',y=['Expected Assists','Assists'],color_discrete_map={'Expected Assists':'black','Assists':'white'},title='Compering the Number of expected Assits to The Actule number of Assists')
fig.show()


# In[25]:



#Expected NO of Goals that the FW would make it 
df_FW['Expected Goals']=df_FW['xG']*df_FW['Matches']
fig=px.bar(df_FW.nlargest(10,'Expected Goals')[['Name','Expected Goals','Goals']],
          x='Name',y=['Expected Goals','Goals'],color_discrete_map={'Expected Goals':'black','Goals':'white'},title='Compering the Number of expected Goals to The Actule number of Goals')
fig.show()


# In[26]:


clubs = data['Club'].unique()
clubs


# In[27]:


teams = data.groupby('Club')


# In[28]:


def category(col):
    total=[]
    for club in clubs:
        total.append(teams.get_group(club)[col].sum())
    df=pd.DataFrame({'Club':clubs,f'Total {col}':total})
    return df


# In[29]:


total_goals=category('Goals')
fig=px.bar(total_goals.sort_values(by=['Total Goals']),x='Total Goals',y='Club',color='Total Goals')
fig.show()


# In[42]:


#The most aggrissive team
yellow_card=category('Yellow_Cards')
red_cards=category('Red_Cards')
aggrisive=red_cards.merge(yellow_card,on='Club')
aggrisive


# In[50]:


fig=px.bar(aggrisive,x=['Total Red_Cards','Total Yellow_Cards'],y='Club',
          color_discrete_map={'Total Red_Cards':'red','Total Yellow_Cards':'yellow'})
fig.show()


# In[52]:


Nationality = data.groupby(pd.Grouper(key='Nationality')).size().reset_index(name='count')
Nationality


# In[54]:


fig = px.treemap(Nationality, path=['Nationality'], values='count')
fig.show()


# In[ ]:




