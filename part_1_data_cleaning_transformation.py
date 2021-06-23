#!/usr/bin/env python
# coding: utf-8

# <h2 align='center'> Cyclistic: a bike-share program </h2>
# 
# <h4 align='center'> (Part 1: Data Cleaning & Transformation) </h4>

# ### 1. Import libraries and datasets

# In[10]:


import pandas as pd


# In[11]:


bt_202004 = pd.read_csv('~/00_PROJECTS/cs_1_bike_share/original_datasets/202004-divvy-tripdata.csv')
bt_202005 = pd.read_csv('~/00_PROJECTS/cs_1_bike_share/original_datasets/202005-divvy-tripdata.csv')
bt_202006 = pd.read_csv('~/00_PROJECTS/cs_1_bike_share/original_datasets/202006-divvy-tripdata.csv')
bt_202007 = pd.read_csv('~/00_PROJECTS/cs_1_bike_share/original_datasets/202007-divvy-tripdata.csv')
bt_202008 = pd.read_csv('~/00_PROJECTS/cs_1_bike_share/original_datasets/202008-divvy-tripdata.csv')
bt_202009 = pd.read_csv('~/00_PROJECTS/cs_1_bike_share/original_datasets/202009-divvy-tripdata.csv')
bt_202010 = pd.read_csv('~/00_PROJECTS/cs_1_bike_share/original_datasets/202010-divvy-tripdata.csv')
bt_202011 = pd.read_csv('~/00_PROJECTS/cs_1_bike_share/original_datasets/202011-divvy-tripdata.csv')
bt_202012 = pd.read_csv('~/00_PROJECTS/cs_1_bike_share/original_datasets/202012-divvy-tripdata.csv')
bt_202101 = pd.read_csv('~/00_PROJECTS/cs_1_bike_share/original_datasets/202101-divvy-tripdata.csv')
bt_202102 = pd.read_csv('~/00_PROJECTS/cs_1_bike_share/original_datasets/202102-divvy-tripdata.csv')
bt_202103 = pd.read_csv('~/00_PROJECTS/cs_1_bike_share/original_datasets/202103-divvy-tripdata.csv')


# ### 2. Examine datasets

# <h4 style="color:Green;">(2-1) dataset: bike trips of April 2020</h4>

# In[4]:


bt_202004.head()


# In[5]:


bt_202004.dtypes


# <h4 style="color:Blue;">The "started_at" column and the "ended_at" column are objects which they should be datetimes. However, I will leave them as-is for now (in fact, I will leave these two columns in all datasets) since my goal for the initial data cleaning is mainly clean out invalid and incorrect data.</h4>

# In[6]:


bt_202004.isna().sum()


# In[7]:


# drop all NAN values in bt_202004
bt_202004.dropna(inplace=True)


# In[8]:


# convert 'end_station_id' column from floating points to integers
bt_202004['end_station_id'] = bt_202004['end_station_id'].astype('int64')


# <h4 style="color:Green;">(2-2) dataset: bike trips of May 2020</h4>

# In[10]:


bt_202005.head()


# In[11]:


bt_202005.dtypes


# In[12]:


bt_202005.isna().sum()


# In[13]:


# drop all NAN values in bt_202005
bt_202005.dropna(inplace=True)


# In[14]:


# convert 'end_station_id' from floating points to integers
bt_202005['end_station_id'] = bt_202005['end_station_id'].astype('int64')


# <h4 style="color:Green;">(2-3) dataset: bike trips of June 2020</h4>

# In[15]:


bt_202006.head()


# In[16]:


bt_202006.dtypes


# In[17]:


bt_202006.isna().sum()


# In[18]:


# drop all NAN values in bt_202006
bt_202006.dropna(inplace=True)


# In[19]:


# convert 'end_station_id' from floating points to integers
bt_202006['end_station_id'] = bt_202006['end_station_id'].astype('int64')


# <h4 style="color:Green;">(2-4) dataset: bike trips of July 2020</h4>

# In[20]:


bt_202007.head()


# In[21]:


bt_202007.dtypes


# In[22]:


bt_202007.isna().sum()


# In[23]:


# drop all NAN values in bt_202007
bt_202007.dropna(inplace=True)


# In[24]:


# convert 'start_station_id' column from floating points to integers
bt_202007['start_station_id'] = bt_202007['start_station_id'].astype('int64')

# convert 'end_station_id' column from floating points to integers
bt_202007['end_station_id'] = bt_202007['end_station_id'].astype('int64')


# <h4 style="color:Green;">(2-5) dataset: bike trips of August 2020</h4>

# In[25]:


bt_202008.head()


# In[26]:


bt_202008.dtypes


# In[27]:


bt_202008.isna().sum()


# In[28]:


# drop all NAN values in bt_202008
bt_202008.dropna(inplace=True)


# In[29]:


# convert 'start_station_id' column from floating points to integers
bt_202008['start_station_id'] = bt_202008['start_station_id'].astype('int64')

# convert 'end_station_id' column from floating points to integers
bt_202008['end_station_id'] = bt_202008['end_station_id'].astype('int64')


# <h4 style="color:Green;">(2-6) dataset: bike trips of September 2020</h4>

# In[30]:


bt_202009.head()


# In[31]:


bt_202009.dtypes


# In[32]:


bt_202009.isna().sum()


# In[33]:


# drop all NAN values in bt_202009
bt_202009.dropna(inplace=True)


# In[34]:


# convert 'start_station_id' column from floating points to integers
bt_202009['start_station_id'] = bt_202009['start_station_id'].astype('int64')

# convert 'end_station_id' column from floating points to integers
bt_202009['end_station_id'] = bt_202009['end_station_id'].astype('int64')


# <h4 style="color:Green;">(2-7) dataset: bike trips of October 2020</h4>

# In[35]:


bt_202010.head()


# In[36]:


bt_202010.dtypes


# In[37]:


bt_202010.isna().sum()


# In[38]:


# drop all NAN values in bt_202010
bt_202010.dropna(inplace=True)


# In[39]:


# convert 'start_station_id' column from floating points to integers
bt_202010['start_station_id'] = bt_202010['start_station_id'].astype('int64')

# convert 'end_station_id' column from floating points to integers
bt_202010['end_station_id'] = bt_202010['end_station_id'].astype('int64')


# <h4 style="color:Green;">(2-8) dataset: bike trips of November 2020</h4>

# In[40]:


bt_202011.head()


# In[41]:


bt_202011.dtypes


# In[42]:


bt_202011.isna().sum()


# In[43]:


# drop all NAN values in bt_202011
bt_202011.dropna(inplace=True)


# In[44]:


# convert 'start_station_id' column from floating points to integers
bt_202011['start_station_id'] = bt_202011['start_station_id'].astype('int64')

# convert 'end_station_id' column from floating points to integers
bt_202011['end_station_id'] = bt_202011['end_station_id'].astype('int64')


# <h4 style="color:Green;">(2-9) dataset: bike trips of December 2020</h4>

# In[45]:


bt_202012.head()


# In[46]:


bt_202012.dtypes


# In[47]:


bt_202012.isna().sum()


# In[48]:


# drop all NAN values in bt_202012
bt_202012.dropna(inplace=True)


# <h4 style="color:Red;"> After examinging the 'start_station_id' column and 'end_station_id' in this dataset, I found an inconsistency issue between station ids and their corresponding names. Specifically, if a start or end station's name is "Rhodes Ave & 32nd St", then its corresponding id is 263 in all previous nine datasets, but in this dataset it is associated with id 13215. </h4>
#     
# <h4 style="color:Red;"> Therefore, I will re-validate the correct ids from cross-referecing all previous datasets, and then cast these two columns into integer datatype. </h4>

# In[49]:


# get all pairs of station names and ids from previous 8 datasets

station_id = dict(zip(bt_202004['start_station_name'], bt_202004['start_station_id']))
station_id.update(zip(bt_202004['end_station_name'], bt_202004['end_station_id']))

station_id.update(zip(bt_202005['start_station_name'], bt_202005['start_station_id']))
station_id.update(zip(bt_202005['end_station_name'], bt_202005['end_station_id']))

station_id.update(zip(bt_202006['start_station_name'], bt_202006['start_station_id']))
station_id.update(zip(bt_202006['end_station_name'], bt_202006['end_station_id']))

station_id.update(zip(bt_202007['start_station_name'], bt_202007['start_station_id']))
station_id.update(zip(bt_202007['end_station_name'], bt_202007['end_station_id']))

station_id.update(zip(bt_202008['start_station_name'], bt_202008['start_station_id']))
station_id.update(zip(bt_202008['end_station_name'], bt_202005['end_station_id']))

station_id.update(zip(bt_202009['start_station_name'], bt_202009['start_station_id']))
station_id.update(zip(bt_202009['end_station_name'], bt_202009['end_station_id']))

station_id.update(zip(bt_202010['start_station_name'], bt_202010['start_station_id']))
station_id.update(zip(bt_202010['end_station_name'], bt_202010['end_station_id']))

station_id.update(zip(bt_202011['start_station_name'], bt_202011['start_station_id']))
station_id.update(zip(bt_202011['end_station_name'], bt_202011['end_station_id']))


# <h4 style="color:Blue;"> The function 'correct_station_name_id' below will grab all start station names and end station names from the input dataframe, determine if each station's name appears in the previous 8 datasets: </h4>
# 
# - <p style="color:Blue;"> if it does exist, update its corresponding id from the input dataframe to the correct one; </p>
# - <p style="color:Blue;"> if it does not exist, mark the station's name in a list 'not_changed' for further cleaning.</p>

# In[50]:


not_changed = list()

def correct_station_name_id(dataframe):
    start_station_names = set(dataframe['start_station_name'])
    end_station_names = set(dataframe['end_station_name'])
    
    # correct start_station_ids in the dataset
    for name in start_station_names:
        if name not in station_id.keys():
            not_changed.append(name) # catch exceptions in case any station name haven't appeared in previous 8 datasets
        else:
            dataframe.loc[dataframe['start_station_name'] == name, 'start_station_id'] = station_id[name]
    
    # correct end_station_ids in the dataset
    for name in end_station_names:
        if name in not_changed:
            continue
        elif name not in station_id.keys():
            not_changed.append(name) # catch exceptions in case any station name haven't appeared in previous 8 datasets
        else:
            dataframe.loc[dataframe['end_station_name'] == name, 'end_station_id'] = station_id[name]
    
    print('These stations below are not existed in the previous 8 datasets:')
    return not_changed


# In[51]:


# update stations' ids in bt_202012 and catch stations that're not existed from previous 8 datasets
correct_station_name_id(bt_202012)


# <h4 style="color:Red;"> As showed above, 5 station names were caught as exceptions in the list not_changed </h4>
#     
# <h4 style="color:Red;"> Meanwhile, I've examined the rest 3 datasets, and I found in these 3 datasets these 5 station names and their corresponding ids are not correct as well. </h4>
# 
# <h4 style="color:Blue;"> Therefore, I've found the official dataset of all Divvy Bicycle Stations at <a href="https://data.cityofchicago.org/d/bbyy-e7gq?category=Transportation&view_name=Divvy-Bicycle-Stations"> here </a> on <a href="httP://data.cityofchicago.org"> The Chicago Data Portal website </a></h4>
# 
# <h4 style="color:Blue;"> I will download this dataset and import it below as the official reference to get the correct station names and/or corresponding ids.</h4>

# In[53]:


# import the official bike stations information dataset
official_station_info = pd.read_csv('~/00_PROJECTS/cs_1_bike_share/original_datasets/official_bike_stations_info.csv')

# get the station name and id in pairs from the official station information dataset
official_station_name_id = dict(zip(official_station_info['Station Name'], official_station_info['ID']))


# In[54]:


# get the correct id of each station that're not existed in the previous 8 datasets from the official stations information dataset
def get_correct_id():
    cannot_find_this_station = []
    for name in not_changed:
        if name not in official_station_name_id.keys():
            if name not in cannot_find_this_station:
                cannot_find_this_station.append(name)
        else:
            correct_id = official_station_name_id[name]
            print(name, ': ', correct_id)
            print()
    
    print('These stations below cannot be found in the official stations information dataset:')
    return cannot_find_this_station


# In[55]:


# get the correct ids of exceptional stations in list not_changed
get_correct_id()


# <h4 style="color:red;"> The station 'Base - 2132 W Hubbard Warehouse' cannot be found in the official station information dataset. Due to lack of information, I will drop these records. </h4>

# In[56]:


# drop records with start_station_name as 'Base - 2132 W Hubbard Warehouse'
bt_202012.drop(bt_202012[bt_202012['start_station_name'] == 'Base - 2132 W Hubbard Warehouse'].index, inplace=True)

# drop records with end_station_name as 'Base - 2132 W Hubbard Warehouse'
bt_202012.drop(bt_202012[bt_202012['end_station_name'] == 'Base - 2132 W Hubbard Warehouse'].index, inplace=True)


# <h4 style="color:blue;"> For the other 4 stations, I will manually update the ids in bt_202012 </h4>

# In[57]:


# update station's id with name of 'N Green St & W Lake St'
filt_a1 = (bt_202012['start_station_name'] == 'N Green St & W Lake St')
bt_202012.loc[filt_a1, 'start_station_id'] = 1436495109493626546

filt_a2 = (bt_202012['end_station_name'] == 'N Green St & W Lake St')
bt_202012.loc[filt_a2, 'end_station_id'] = 1436495109493626546


# In[58]:


# update station's id with name of 'W Oakdale Ave & N Broadway'
filt_b1 = (bt_202012['start_station_name'] == 'W Oakdale Ave & N Broadway')
bt_202012.loc[filt_b1, 'start_station_id'] = 1436495100903691938

filt_b2 = (bt_202012['end_station_name'] == 'W Oakdale Ave & N Broadway')
bt_202012.loc[filt_b2, 'end_station_id'] = 1436495100903691938


# In[59]:


# update station's id with name of 'W Armitage Ave & N Sheffield Ave'
filt_c1 = (bt_202012['start_station_name'] == 'W Armitage Ave & N Sheffield Ave')
bt_202012.loc[filt_c1, 'start_station_id'] = 1436495105198659242

filt_c2 = (bt_202012['end_station_name'] == 'W Armitage Ave & N Sheffield Ave')
bt_202012.loc[filt_c2, 'end_station_id'] = 1436495105198659242


# In[60]:


# update station's id with name of 'N Carpenter St & W Lake St'
filt_d1 = (bt_202012['start_station_name'] == 'N Carpenter St & W Lake St')
bt_202012.loc[filt_d1, 'start_station_id'] = 1436495105198659246

filt_d2 = (bt_202012['end_station_name'] == 'N Carpenter St & W Lake St')
bt_202012.loc[filt_d2, 'end_station_id'] = 1436495105198659246


# <h4 style="color:green;"> (2-10) dataset: bike trips of January 2021 </h4>

# In[61]:


bt_202101.head()


# In[62]:


bt_202101.dtypes


# In[63]:


bt_202101.isna().sum()


# In[64]:


# drop all NAN values in bt_202101
bt_202101.dropna(inplace=True)


# <h4 style="color:red;"> After examinging the 'start_station_id' column and 'end_station_id' in this dataset, I found the same inconsistency issue between station ids and their corresponding names as before. </h4>
#     
# <h4 style="color:blue;"> Therefore, I will re-run the whole process of validating station names with corresponding ids as before using: </h4>
# 
# - <p style="color:blue;"> the official stations information dataset from Chicago Data Portral website;</p>
# - <p style="color:blue;"> the dictionary "station_id" of all stations and ids existed in the previous 8 datasets;</p>
# - <p style="color:blue;"> the function "correct_station_name_id" to either update ids or catch exceptions;</p>
# - <p style="color:blue;"> the function "get_correct_id" to grab the correct ids for exceptions.</p>

# In[65]:


# reset the not_changed list to empty
not_changed = []

# update stations' ids in bt_202101 or catch stations that're not existed from previous 8 datasets
correct_station_name_id(bt_202101)


# In[66]:


# get the correct ids of exceptional stations in list not_changed
get_correct_id()


# <h4 style="color:red;"> The stations 'Base - 2132 W Hubbard Warehouse' and 'N Damen Ave & W Wabansia St' cannot be found in the official station information dataset. Due to lack of information, I will drop these records. </h4>

# In[67]:


# drop records with start_station_name as 'Base - 2132 W Hubbard Warehouse'
bt_202101.drop(bt_202101[bt_202101['start_station_name'] == 'Base - 2132 W Hubbard Warehouse'].index, inplace=True)

# drop records with end_station_name as 'Base - 2132 W Hubbard Warehouse'
bt_202101.drop(bt_202101[bt_202101['end_station_name'] == 'Base - 2132 W Hubbard Warehouse'].index, inplace=True)

# drop records with start_station_name as 'N Damen Ave & W Wabansia St'
bt_202101.drop(bt_202101[bt_202101['start_station_name'] == 'N Damen Ave & W Wabansia St'].index, inplace=True)

# drop records with end_station_name as 'N Damen Ave & W Wabansia St'
bt_202101.drop(bt_202101[bt_202101['end_station_name'] == 'N Damen Ave & W Wabansia St'].index, inplace=True)


# <h4 style="color:blue;"> For the other 12 stations, I will manually update the ids in bt_202101 </h4>

# In[68]:


# update station's id with name of 'Malcolm X College Vaccination Site'
filt_a1 = (bt_202101['start_station_name'] == 'Malcolm X College Vaccination Site')
bt_202101.loc[filt_a1, 'start_station_id'] = 631

filt_a2 = (bt_202101['end_station_name'] == 'Malcolm X College Vaccination Site')
bt_202101.loc[filt_a2, 'end_station_id'] = 631


# In[69]:


# update station's id with name of 'N Southport Ave & W Newport Ave'
filt_b1 = (bt_202101['start_station_name'] == 'N Southport Ave & W Newport Ave')
bt_202101.loc[filt_b1, 'start_station_id'] = 1436495115557663136

filt_b2 = (bt_202101['end_station_name'] == 'N Southport Ave & W Newport Ave')
bt_202101.loc[filt_b2, 'end_station_id'] = 1436495115557663136


# In[70]:


# update station's id with name of 'N Sheffield Ave & W Wellington Ave'
filt_c1 = (bt_202101['start_station_name'] == 'N Sheffield Ave & W Wellington Ave')
bt_202101.loc[filt_c1, 'start_station_id'] = 1436495118083561146

filt_c2 = (bt_202101['end_station_name'] == 'N Sheffield Ave & W Wellington Ave')
bt_202101.loc[filt_c2, 'end_station_id'] = 1436495115557663136


# In[71]:


# update station's id with name of 'N Paulina St & Lincoln Ave'
filt_d1 = (bt_202101['start_station_name'] == 'N Paulina St & Lincoln Ave')
bt_202101.loc[filt_d1, 'start_station_id'] = 1436495122378528446


# In[72]:


# update station's id with name of 'N Green St & W Lake St'
filt_e1 = (bt_202101['start_station_name'] == 'N Green St & W Lake St')
bt_202101.loc[filt_e1, 'start_station_id'] = 1436495109493626546

filt_e2 = (bt_202101['end_station_name'] == 'N Green St & W Lake St')
bt_202101.loc[filt_e2, 'end_station_id'] = 1436495109493626546


# In[73]:


# update station's id with name of 'W Oakdale Ave & N Broadway'
filt_f1 = (bt_202101['start_station_name'] == 'W Oakdale Ave & N Broadway')
bt_202101.loc[filt_f1, 'start_station_id'] = 1436495100903691938

filt_f2 = (bt_202101['end_station_name'] == 'W Oakdale Ave & N Broadway')
bt_202101.loc[filt_f2, 'end_station_id'] = 1436495100903691938


# In[74]:


# update station's id with name of 'W Armitage Ave & N Sheffield Ave'
filt_g1 = (bt_202101['start_station_name'] == 'W Armitage Ave & N Sheffield Ave')
bt_202101.loc[filt_g1, 'start_station_id'] = 1436495105198659242

filt_g2 = (bt_202101['end_station_name'] == 'W Armitage Ave & N Sheffield Ave')
bt_202101.loc[filt_g2, 'end_station_id'] = 1436495105198659242


# In[75]:


# update station's id with name of 'Broadway & Wilson - Truman College Vaccination Site'
filt_h1 = (bt_202101['start_station_name'] == 'Broadway & Wilson - Truman College Vaccination Site')
bt_202101.loc[filt_h1, 'start_station_id'] = 293

filt_h2 = (bt_202101['end_station_name'] == 'Broadway & Wilson - Truman College Vaccination Site')
bt_202101.loc[filt_h2, 'end_station_id'] = 293


# In[76]:


# update station's id with name of 'N Carpenter St & W Lake St'
filt_i1 = (bt_202101['end_station_name'] == 'N Carpenter St & W Lake St')
bt_202101.loc[filt_i1, 'end_station_id'] = 1436495105198659246


# In[77]:


# update station's id with name of 'Western & 28th - Velasquez Institute Vaccination Site'
filt_j1 = (bt_202101['end_station_name'] == 'Western & 28th - Velasquez Institute Vaccination Site')
bt_202101.loc[filt_j1, 'end_station_id'] = 446


# In[78]:


# update station's id with name of 'W Washington Blvd & N Peoria St'
filt_k1 = (bt_202101['end_station_name'] == 'W Washington Blvd & N Peoria St')
bt_202101.loc[filt_k1, 'end_station_id'] = 1436495109493626544


# In[79]:


# update station's id with name of 'Avenue L & 114th St'
filt_l1 = (bt_202101['end_station_name'] == 'Avenue L & 114th St')
bt_202101.loc[filt_l1, 'end_station_id'] = 1448642175142467184


# <h4 style="color:green;"> (2-11) dataset: bike trips of Feburary 2021 </h4>

# In[80]:


bt_202102.head()


# In[81]:


bt_202102.dtypes


# In[82]:


bt_202102.isna().sum()


# In[83]:


# drop all NAN values in bt_202102
bt_202102.dropna(inplace=True)


# <h4 style="color:red;"> After examinging the 'start_station_id' column and 'end_station_id' in this dataset, I found the same inconsistency issue between station ids and their corresponding names as before. </h4>
#     
# <h4 style="color:blue;"> Therefore, I will re-run the whole process of validating station names with corresponding ids as before using: </h4>
# 
# - <p style="color:blue;"> the official stations information dataset from Chicago Data Portral website;</p>
# - <p style="color:blue;"> the dictionary "station_id" of all stations and ids existed in the previous 8 datasets;</p>
# - <p style="color:blue;"> the function "correct_station_name_id" to either update ids or catch exceptions;</p>
# - <p style="color:blue;"> the function "get_correct_id" to grab the correct ids for exceptions.</p>

# In[84]:


# reset the not_changed list to empty
not_changed = []

# update stations' ids in bt_202102 or catch stations that're not existed from previous 8 datasets
correct_station_name_id(bt_202102)


# In[85]:


# get the correct ids of exceptional stations in list not_changed
get_correct_id()


# <h4 style="color:red;"> The stations 'Base - 2132 W Hubbard Warehouse' and 'N Hampden Ct & W Diversey Ave' cannot be found in the official station information dataset. Due to lack of information, I will drop these records. </h4>

# In[86]:


# drop records with start_station_name as 'Base - 2132 W Hubbard Warehouse'
bt_202102.drop(bt_202102[bt_202102['start_station_name'] == 'Base - 2132 W Hubbard Warehouse'].index, inplace=True)

# drop records with end_station_name as 'Base - 2132 W Hubbard Warehouse'
bt_202102.drop(bt_202102[bt_202102['end_station_name'] == 'Base - 2132 W Hubbard Warehouse'].index, inplace=True)

# drop records with start_station_name as 'N Hampden Ct & W Diversey Ave'
bt_202102.drop(bt_202102[bt_202102['start_station_name'] == 'N Hampden Ct & W Diversey Ave'].index, inplace=True)

# drop records with end_station_name as 'N Hampden Ct & W Diversey Ave'
bt_202102.drop(bt_202102[bt_202102['end_station_name'] == 'N Hampden Ct & W Diversey Ave'].index, inplace=True)


# <h4 style="color:blue;"> For the other 10 stations, I will manually update the ids in bt_202102 </h4>

# In[87]:


# update station's id with name of 'Malcolm X College Vaccination Site'
filt_a1 = (bt_202102['start_station_name'] == 'Malcolm X College Vaccination Site')
bt_202102.loc[filt_a1, 'start_station_id'] = 631

filt_a2 = (bt_202102['end_station_name'] == 'Malcolm X College Vaccination Site')
bt_202102.loc[filt_a2, 'end_station_id'] = 631


# In[88]:


# update station's id with name of 'N Paulina St & Lincoln Ave'
filt_b1 = (bt_202102['start_station_name'] == 'N Paulina St & Lincoln Ave')
bt_202102.loc[filt_b1, 'start_station_id'] = 1436495122378528446

filt_b2 = (bt_202102['end_station_name'] == 'N Paulina St & Lincoln Ave')
bt_202102.loc[filt_b2, 'end_station_id'] = 1436495122378528446


# In[89]:


# update station's id with name of 'W Oakdale Ave & N Broadway'
filt_c1 = (bt_202102['start_station_name'] == 'W Oakdale Ave & N Broadway')
bt_202102.loc[filt_c1, 'start_station_id'] = 1436495100903691938

filt_c2 = (bt_202102['end_station_name'] == 'W Oakdale Ave & N Broadway')
bt_202102.loc[filt_c2, 'end_station_id'] = 1436495100903691938


# In[90]:


# update station's id with name of 'W Washington Blvd & N Peoria St'
filt_d1 = (bt_202102['start_station_name'] == 'W Washington Blvd & N Peoria St')
bt_202102.loc[filt_d1, 'start_station_id'] = 1436495109493626544

filt_d2 = (bt_202102['end_station_name'] == 'W Washington Blvd & N Peoria St')
bt_202102.loc[filt_d2, 'end_station_id'] = 1436495109493626544


# In[91]:


# update station's id with name of 'W Armitage Ave & N Sheffield Ave'
filt_e1 = (bt_202102['start_station_name'] == 'W Armitage Ave & N Sheffield Ave')
bt_202102.loc[filt_e1, 'start_station_id'] = 1436495105198659242

filt_e2 = (bt_202102['end_station_name'] == 'W Armitage Ave & N Sheffield Ave')
bt_202102.loc[filt_e2, 'end_station_id'] = 1436495105198659242


# In[92]:


# update station's id with name of 'Broadway & Wilson - Truman College Vaccination Site'
filt_f1 = (bt_202102['start_station_name'] == 'Broadway & Wilson - Truman College Vaccination Site')
bt_202102.loc[filt_f1, 'start_station_id'] = 293

filt_f2 = (bt_202102['end_station_name'] == 'Broadway & Wilson - Truman College Vaccination Site')
bt_202102.loc[filt_f2, 'end_station_id'] = 293


# In[93]:


# update station's id with name of 'N Carpenter St & W Lake St'
filt_g1 = (bt_202102['end_station_name'] == 'N Carpenter St & W Lake St')
bt_202102.loc[filt_g1, 'end_station_id'] = 1436495105198659246


# In[94]:


# update station's id with name of 'Western & 28th - Velasquez Institute Vaccination Site'
filt_h1 = (bt_202102['end_station_name'] == 'Western & 28th - Velasquez Institute Vaccination Site')
bt_202102.loc[filt_h1, 'end_station_id'] = 446


# In[95]:


# update station's id with name of 'N Sheffield Ave & W Wellington Ave'
filt_i1 = (bt_202102['end_station_name'] == 'N Sheffield Ave & W Wellington Ave')
bt_202102.loc[filt_i1, 'end_station_id'] = 1436495118083561146


# In[96]:


# update station's id with name of 'N Green St & W Lake St'
filt_j1 = (bt_202102['end_station_name'] == 'N Green St & W Lake St')
bt_202102.loc[filt_j1, 'end_station_id'] = 1436495109493626546


# <h4 style="color:green;"> (2-12) dataset: bike trips of March 2021 </h4> 

# In[97]:


bt_202103.head()


# In[98]:


bt_202103.dtypes


# In[99]:


bt_202103.isna().sum()


# In[100]:


# drop all NAN values in bt_202103
bt_202103.dropna(inplace=True)


# <h4 style="color:red;"> After examinging the 'start_station_id' column and 'end_station_id' in this dataset, I found the same inconsistency issue between station ids and their corresponding names as before. </h4>
#     
# <h4 style="color:blue;"> Therefore, I will re-run the whole process of validating station names with corresponding ids as before using: </h4>
# 
# - <p style="color:blue;"> the official stations information dataset from Chicago Data Portral website;</p>
# - <p style="color:blue;"> the dictionary "station_id" of all stations and ids existed in the previous 8 datasets;</p>
# - <p style="color:blue;"> the function "correct_station_name_id" to either update ids or catch exceptions;</p>
# - <p style="color:blue;"> the function "get_correct_id" to grab the correct ids for exceptions.</p>

# In[101]:


# reset the not_changed list to empty
not_changed = []

# update stations' ids in bt_202103 or catch stations that're not existed from previous 8 datasets
correct_station_name_id(bt_202103)


# In[102]:


# get the correct ids of exceptional stations in list not_changed
get_correct_id()


# <h4 style="color:red;"> The stations 'Base - 2132 W Hubbard Warehouse', 'N Hampden Ct & W Diversey Ave', and 'N Damen Ave & W Wabansia St' cannot be found in the official station information dataset. Due to lack of information, I will drop these records. </h4>

# In[103]:


# drop records with start_station_name as 'Base - 2132 W Hubbard Warehouse'
bt_202103.drop(bt_202103[bt_202103['start_station_name'] == 'Base - 2132 W Hubbard Warehouse'].index, inplace=True)

# drop records with end_station_name as 'Base - 2132 W Hubbard Warehouse'
bt_202103.drop(bt_202103[bt_202103['end_station_name'] == 'Base - 2132 W Hubbard Warehouse'].index, inplace=True)

# drop records with start_station_name as 'N Hampden Ct & W Diversey Ave'
bt_202103.drop(bt_202103[bt_202103['start_station_name'] == 'N Hampden Ct & W Diversey Ave'].index, inplace=True)

# drop records with end_station_name as 'N Hampden Ct & W Diversey Ave'
bt_202103.drop(bt_202103[bt_202103['end_station_name'] == 'N Hampden Ct & W Diversey Ave'].index, inplace=True)

# drop records with start_station_name as 'N Damen Ave & W Wabansia St'
bt_202103.drop(bt_202103[bt_202103['start_station_name'] == 'N Damen Ave & W Wabansia St'].index, inplace=True)

# drop records with end_station_name as 'N Damen Ave & W Wabansia St'
bt_202103.drop(bt_202103[bt_202103['end_station_name'] == 'N Damen Ave & W Wabansia St'].index, inplace=True)


# <h4 style="color:blue;"> For the other 15 stations, I will manually update the ids in bt_202102 </h4>

# In[104]:


# update station's id with name of 'Broadway & Wilson - Truman College Vaccination Site'
filt_a1 = (bt_202103['start_station_name'] == 'Broadway & Wilson - Truman College Vaccination Site')
bt_202103.loc[filt_a1, 'start_station_id'] = 293

filt_a2 = (bt_202103['end_station_name'] == 'Broadway & Wilson - Truman College Vaccination Site')
bt_202103.loc[filt_a2, 'end_station_id'] = 293


# In[105]:


# update station's id with name of 'Damen Ave & Wabansia Ave'
filt_b1 = (bt_202103['start_station_name'] == 'Damen Ave & Wabansia Ave')
bt_202103.loc[filt_b1, 'start_station_id'] = 1521686986436309688

filt_b2 = (bt_202103['end_station_name'] == 'Damen Ave & Wabansia Ave')
bt_202103.loc[filt_b2, 'end_station_id'] = 1521686986436309688


# In[106]:


# update station's id with name of 'Western & 28th - Velasquez Institute Vaccination Site'
filt_c1 = (bt_202103['start_station_name'] == 'Western & 28th - Velasquez Institute Vaccination Site')
bt_202103.loc[filt_c1, 'start_station_id'] = 446

filt_c2 = (bt_202103['end_station_name'] == 'Western & 28th - Velasquez Institute Vaccination Site')
bt_202103.loc[filt_c2, 'end_station_id'] = 446


# In[107]:


# update station's id with name of 'Chicago State University'
filt_d1 = (bt_202103['start_station_name'] == 'Chicago State University')
bt_202103.loc[filt_d1, 'start_station_id'] = 737

filt_d2 = (bt_202103['end_station_name'] == 'Chicago State University')
bt_202103.loc[filt_d2, 'end_station_id'] = 737


# In[108]:


# update station's id with name of 'W Armitage Ave & N Sheffield Ave'
filt_e1 = (bt_202103['start_station_name'] == 'W Armitage Ave & N Sheffield Ave')
bt_202103.loc[filt_e1, 'start_station_id'] = 1436495105198659242

filt_e2 = (bt_202103['end_station_name'] == 'W Armitage Ave & N Sheffield Ave')
bt_202103.loc[filt_e2, 'end_station_id'] = 1436495105198659242


# In[109]:


# update station's id with name of 'W Washington Blvd & N Peoria St'
filt_f1 = (bt_202103['start_station_name'] == 'W Washington Blvd & N Peoria St')
bt_202103.loc[filt_f1, 'start_station_id'] = 1436495109493626544

filt_f2 = (bt_202103['end_station_name'] == 'W Washington Blvd & N Peoria St')
bt_202103.loc[filt_f2, 'end_station_id'] = 1436495109493626544


# In[110]:


# update station's id with name of 'N Paulina St & Lincoln Ave'
filt_g1 = (bt_202103['start_station_name'] == 'N Paulina St & Lincoln Ave')
bt_202103.loc[filt_g1, 'start_station_id'] = 1436495122378528446
              
filt_g2 = (bt_202103['end_station_name'] == 'N Paulina St & Lincoln Ave')
bt_202103.loc[filt_g2, 'end_station_id'] = 1436495122378528446


# In[111]:


# update station's id with name of 'Halsted & 63rd - Kennedy-King Vaccination Site'
filt_h1 = (bt_202103['start_station_name'] == 'Halsted & 63rd - Kennedy-King Vaccination Site')
bt_202103.loc[filt_h1, 'start_station_id'] = 388

filt_h2 = (bt_202103['end_station_name'] == 'Halsted & 63rd - Kennedy-King Vaccination Site')
bt_202103.loc[filt_h2, 'end_station_id'] = 388


# In[112]:


# update station's id with name of 'Kedzie Ave & 110th St'
filt_i1 = (bt_202103['start_station_name'] == 'Kedzie Ave & 110th St')
bt_202103.loc[filt_i1, 'start_station_id'] = 736

filt_i2 = (bt_202103['end_station_name'] == 'Kedzie Ave & 110th St')
bt_202103.loc[filt_i2, 'end_station_id'] = 736


# In[113]:


# update station's id with name of 'N Carpenter St & W Lake St'
filt_j1 = (bt_202103['start_station_name'] == 'N Carpenter St & W Lake St')
bt_202103.loc[filt_j1, 'start_station_id'] = 1436495105198659246

filt_j2 = (bt_202103['end_station_name'] == 'N Carpenter St & W Lake St')
bt_202103.loc[filt_j2, 'end_station_id'] = 1436495105198659246


# In[114]:


# update station's id with name of 'Malcolm X College Vaccination Site'
filt_k1 = (bt_202103['start_station_name'] == 'Malcolm X College Vaccination Site')
bt_202103.loc[filt_k1, 'start_station_id'] = 631

filt_k2 = (bt_202103['end_station_name'] == 'Malcolm X College Vaccination Site')
bt_202103.loc[filt_k2, 'end_station_id'] = 631


# In[115]:


# update station's id with name of 'N Sheffield Ave & W Wellington Ave'
filt_l1 = (bt_202103['start_station_name'] == 'N Sheffield Ave & W Wellington Ave')
bt_202103.loc[filt_l1, 'start_station_id'] = 1436495118083561146

filt_l2 = (bt_202103['end_station_name'] == 'N Sheffield Ave & W Wellington Ave')
bt_202103.loc[filt_l2, 'end_station_id'] = 1436495118083561146


# In[116]:


# update station's id with name of 'W Oakdale Ave & N Broadway'
filt_m1 = (bt_202103['start_station_name'] == 'W Oakdale Ave & N Broadway')
bt_202103.loc[filt_m1, 'start_station_id'] = 1436495100903691938

filt_m2 = (bt_202103['end_station_name'] == 'W Oakdale Ave & N Broadway')
bt_202103.loc[filt_m2, 'end_station_id'] = 1436495100903691938


# In[117]:


# update station's id with name of 'N Southport Ave & W Newport Ave'
filt_n1 = (bt_202103['start_station_name'] == 'N Southport Ave & W Newport Ave')
bt_202103.loc[filt_n1, 'start_station_id'] = 1436495115557663136

filt_n2 = (bt_202103['end_station_name'] == 'N Southport Ave & W Newport Ave')
bt_202103.loc[filt_n2, 'end_station_id'] = 1436495115557663136


# In[118]:


# update station's id with name of 'N Green St & W Lake St'
filt_o1 = (bt_202103['start_station_name'] == 'N Green St & W Lake St')
bt_202103.loc[filt_o1, 'start_station_id'] = 1436495109493626546

filt_o2 = (bt_202103['end_station_name'] == 'N Green St & W Lake St')
bt_202103.loc[filt_o2, 'end_station_id'] = 1436495109493626546


# ### 3. Save cleaned datasets

# In[9]:


bt_202004.to_csv('~/00_PROJECTS/cs_1_bike_share/cleaned_datasets/bt_202004.csv', index=False)
bt_202005.to_csv('~/00_PROJECTS/cs_1_bike_share/cleaned_datasets/bt_202005.csv', index=False)
bt_202006.to_csv('~/00_PROJECTS/cs_1_bike_share/cleaned_datasets/bt_202006.csv', index=False)
bt_202007.to_csv('~/00_PROJECTS/cs_1_bike_share/cleaned_datasets/bt_202007.csv', index=False)
bt_202008.to_csv('~/00_PROJECTS/cs_1_bike_share/cleaned_datasets/bt_202008.csv', index=False)
bt_202009.to_csv('~/00_PROJECTS/cs_1_bike_share/cleaned_datasets/bt_202009.csv', index=False)
bt_202010.to_csv('~/00_PROJECTS/cs_1_bike_share/cleaned_datasets/bt_202010.csv', index=False)
bt_202011.to_csv('~/00_PROJECTS/cs_1_bike_share/cleaned_datasets/bt_202011.csv', index=False)
bt_202012.to_csv('~/00_PROJECTS/cs_1_bike_share/cleaned_datasets/bt_202012.csv', index=False)
bt_202101.to_csv('~/00_PROJECTS/cs_1_bike_share/cleaned_datasets/bt_202101.csv', index=False)
bt_202102.to_csv('~/00_PROJECTS/cs_1_bike_share/cleaned_datasets/bt_202102.csv', index=False)
bt_202103.to_csv('~/00_PROJECTS/cs_1_bike_share/cleaned_datasets/bt_202103.csv', index=False)


# In[ ]:




