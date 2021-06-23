<h2 align='center'> Cyclistic: a bike-share program </h2>

<h4 align='center'> (Part 1: Data Cleaning & Transformation) </h4>

### 1. Import libraries and datasets


```python
import pandas as pd
```


```python
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
```

### 2. Examine datasets

<h4 style="color:Green;">(2-1) dataset: bike trips of April 2020</h4>


```python
bt_202004.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ride_id</th>
      <th>rideable_type</th>
      <th>started_at</th>
      <th>ended_at</th>
      <th>start_station_name</th>
      <th>start_station_id</th>
      <th>end_station_name</th>
      <th>end_station_id</th>
      <th>start_lat</th>
      <th>start_lng</th>
      <th>end_lat</th>
      <th>end_lng</th>
      <th>member_casual</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A847FADBBC638E45</td>
      <td>docked_bike</td>
      <td>2020-04-26 17:45:14</td>
      <td>2020-04-26 18:12:03</td>
      <td>Eckhart Park</td>
      <td>86</td>
      <td>Lincoln Ave &amp; Diversey Pkwy</td>
      <td>152.0</td>
      <td>41.8964</td>
      <td>-87.6610</td>
      <td>41.9322</td>
      <td>-87.6586</td>
      <td>member</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5405B80E996FF60D</td>
      <td>docked_bike</td>
      <td>2020-04-17 17:08:54</td>
      <td>2020-04-17 17:17:03</td>
      <td>Drake Ave &amp; Fullerton Ave</td>
      <td>503</td>
      <td>Kosciuszko Park</td>
      <td>499.0</td>
      <td>41.9244</td>
      <td>-87.7154</td>
      <td>41.9306</td>
      <td>-87.7238</td>
      <td>member</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5DD24A79A4E006F4</td>
      <td>docked_bike</td>
      <td>2020-04-01 17:54:13</td>
      <td>2020-04-01 18:08:36</td>
      <td>McClurg Ct &amp; Erie St</td>
      <td>142</td>
      <td>Indiana Ave &amp; Roosevelt Rd</td>
      <td>255.0</td>
      <td>41.8945</td>
      <td>-87.6179</td>
      <td>41.8679</td>
      <td>-87.6230</td>
      <td>member</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2A59BBDF5CDBA725</td>
      <td>docked_bike</td>
      <td>2020-04-07 12:50:19</td>
      <td>2020-04-07 13:02:31</td>
      <td>California Ave &amp; Division St</td>
      <td>216</td>
      <td>Wood St &amp; Augusta Blvd</td>
      <td>657.0</td>
      <td>41.9030</td>
      <td>-87.6975</td>
      <td>41.8992</td>
      <td>-87.6722</td>
      <td>member</td>
    </tr>
    <tr>
      <th>4</th>
      <td>27AD306C119C6158</td>
      <td>docked_bike</td>
      <td>2020-04-18 10:22:59</td>
      <td>2020-04-18 11:15:54</td>
      <td>Rush St &amp; Hubbard St</td>
      <td>125</td>
      <td>Sheridan Rd &amp; Lawrence Ave</td>
      <td>323.0</td>
      <td>41.8902</td>
      <td>-87.6262</td>
      <td>41.9695</td>
      <td>-87.6547</td>
      <td>casual</td>
    </tr>
  </tbody>
</table>
</div>




```python
bt_202004.dtypes
```




    ride_id                       object
    rideable_type                 object
    started_at            datetime64[ns]
    ended_at              datetime64[ns]
    start_station_name            object
    start_station_id               int64
    end_station_name              object
    end_station_id               float64
    start_lat                    float64
    start_lng                    float64
    end_lat                      float64
    end_lng                      float64
    member_casual                 object
    dtype: object



<h4 style="color:Blue;">The "started_at" column and the "ended_at" column are objects which they should be datetimes. However, I will leave them as-is for now (in fact, I will leave these two columns in all datasets) since my goal for the initial data cleaning is mainly clean out invalid and incorrect data.</h4>


```python
bt_202004.isna().sum()
```




    ride_id                0
    rideable_type          0
    started_at             0
    ended_at               0
    start_station_name     0
    start_station_id       0
    end_station_name      99
    end_station_id        99
    start_lat              0
    start_lng              0
    end_lat               99
    end_lng               99
    member_casual          0
    dtype: int64




```python
# drop all NAN values in bt_202004
bt_202004.dropna(inplace=True)
```


```python
# convert 'end_station_id' column from floating points to integers
bt_202004['end_station_id'] = bt_202004['end_station_id'].astype('int64')
```

<h4 style="color:Green;">(2-2) dataset: bike trips of May 2020</h4>


```python
bt_202005.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ride_id</th>
      <th>rideable_type</th>
      <th>started_at</th>
      <th>ended_at</th>
      <th>start_station_name</th>
      <th>start_station_id</th>
      <th>end_station_name</th>
      <th>end_station_id</th>
      <th>start_lat</th>
      <th>start_lng</th>
      <th>end_lat</th>
      <th>end_lng</th>
      <th>member_casual</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>02668AD35674B983</td>
      <td>docked_bike</td>
      <td>2020-05-27 10:03:52</td>
      <td>2020-05-27 10:16:49</td>
      <td>Franklin St &amp; Jackson Blvd</td>
      <td>36</td>
      <td>Wabash Ave &amp; Grand Ave</td>
      <td>199.0</td>
      <td>41.8777</td>
      <td>-87.6353</td>
      <td>41.8915</td>
      <td>-87.6268</td>
      <td>member</td>
    </tr>
    <tr>
      <th>1</th>
      <td>7A50CCAF1EDDB28F</td>
      <td>docked_bike</td>
      <td>2020-05-25 10:47:11</td>
      <td>2020-05-25 11:05:40</td>
      <td>Clark St &amp; Wrightwood Ave</td>
      <td>340</td>
      <td>Clark St &amp; Leland Ave</td>
      <td>326.0</td>
      <td>41.9295</td>
      <td>-87.6431</td>
      <td>41.9671</td>
      <td>-87.6674</td>
      <td>casual</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2FFCDFDB91FE9A52</td>
      <td>docked_bike</td>
      <td>2020-05-02 14:11:03</td>
      <td>2020-05-02 15:48:21</td>
      <td>Kedzie Ave &amp; Milwaukee Ave</td>
      <td>260</td>
      <td>Kedzie Ave &amp; Milwaukee Ave</td>
      <td>260.0</td>
      <td>41.9296</td>
      <td>-87.7079</td>
      <td>41.9296</td>
      <td>-87.7079</td>
      <td>casual</td>
    </tr>
    <tr>
      <th>3</th>
      <td>58991CF1DB75BA84</td>
      <td>docked_bike</td>
      <td>2020-05-02 16:25:36</td>
      <td>2020-05-02 16:39:28</td>
      <td>Clarendon Ave &amp; Leland Ave</td>
      <td>251</td>
      <td>Lake Shore Dr &amp; Wellington Ave</td>
      <td>157.0</td>
      <td>41.9680</td>
      <td>-87.6500</td>
      <td>41.9367</td>
      <td>-87.6368</td>
      <td>casual</td>
    </tr>
    <tr>
      <th>4</th>
      <td>A79651EFECC268CD</td>
      <td>docked_bike</td>
      <td>2020-05-29 12:49:54</td>
      <td>2020-05-29 13:27:11</td>
      <td>Hermitage Ave &amp; Polk St</td>
      <td>261</td>
      <td>Halsted St &amp; Archer Ave</td>
      <td>206.0</td>
      <td>41.8715</td>
      <td>-87.6699</td>
      <td>41.8472</td>
      <td>-87.6468</td>
      <td>member</td>
    </tr>
  </tbody>
</table>
</div>




```python
bt_202005.dtypes
```




    ride_id                object
    rideable_type          object
    started_at             object
    ended_at               object
    start_station_name     object
    start_station_id        int64
    end_station_name       object
    end_station_id        float64
    start_lat             float64
    start_lng             float64
    end_lat               float64
    end_lng               float64
    member_casual          object
    dtype: object




```python
bt_202005.isna().sum()
```




    ride_id                 0
    rideable_type           0
    started_at              0
    ended_at                0
    start_station_name      0
    start_station_id        0
    end_station_name      321
    end_station_id        321
    start_lat               0
    start_lng               0
    end_lat               321
    end_lng               321
    member_casual           0
    dtype: int64




```python
# drop all NAN values in bt_202005
bt_202005.dropna(inplace=True)
```


```python
# convert 'end_station_id' from floating points to integers
bt_202005['end_station_id'] = bt_202005['end_station_id'].astype('int64')
```

<h4 style="color:Green;">(2-3) dataset: bike trips of June 2020</h4>


```python
bt_202006.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ride_id</th>
      <th>rideable_type</th>
      <th>started_at</th>
      <th>ended_at</th>
      <th>start_station_name</th>
      <th>start_station_id</th>
      <th>end_station_name</th>
      <th>end_station_id</th>
      <th>start_lat</th>
      <th>start_lng</th>
      <th>end_lat</th>
      <th>end_lng</th>
      <th>member_casual</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>8CD5DE2C2B6C4CFC</td>
      <td>docked_bike</td>
      <td>2020-06-13 23:24:48</td>
      <td>2020-06-13 23:36:55</td>
      <td>Wilton Ave &amp; Belmont Ave</td>
      <td>117</td>
      <td>Damen Ave &amp; Clybourn Ave</td>
      <td>163.0</td>
      <td>41.940180</td>
      <td>-87.653040</td>
      <td>41.931931</td>
      <td>-87.677856</td>
      <td>casual</td>
    </tr>
    <tr>
      <th>1</th>
      <td>9A191EB2C751D85D</td>
      <td>docked_bike</td>
      <td>2020-06-26 07:26:10</td>
      <td>2020-06-26 07:31:58</td>
      <td>Federal St &amp; Polk St</td>
      <td>41</td>
      <td>Daley Center Plaza</td>
      <td>81.0</td>
      <td>41.872077</td>
      <td>-87.629543</td>
      <td>41.884241</td>
      <td>-87.629634</td>
      <td>member</td>
    </tr>
    <tr>
      <th>2</th>
      <td>F37D14B0B5659BCF</td>
      <td>docked_bike</td>
      <td>2020-06-23 17:12:41</td>
      <td>2020-06-23 17:21:14</td>
      <td>Daley Center Plaza</td>
      <td>81</td>
      <td>State St &amp; Harrison St</td>
      <td>5.0</td>
      <td>41.884241</td>
      <td>-87.629634</td>
      <td>41.874053</td>
      <td>-87.627716</td>
      <td>member</td>
    </tr>
    <tr>
      <th>3</th>
      <td>C41237B506E85FA1</td>
      <td>docked_bike</td>
      <td>2020-06-20 01:09:35</td>
      <td>2020-06-20 01:28:24</td>
      <td>Broadway &amp; Cornelia Ave</td>
      <td>303</td>
      <td>Broadway &amp; Berwyn Ave</td>
      <td>294.0</td>
      <td>41.945529</td>
      <td>-87.646439</td>
      <td>41.978353</td>
      <td>-87.659753</td>
      <td>casual</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4B51B3B0BDA7787C</td>
      <td>docked_bike</td>
      <td>2020-06-25 16:59:25</td>
      <td>2020-06-25 17:08:48</td>
      <td>Sheffield Ave &amp; Webster Ave</td>
      <td>327</td>
      <td>Wilton Ave &amp; Belmont Ave</td>
      <td>117.0</td>
      <td>41.921540</td>
      <td>-87.653818</td>
      <td>41.940180</td>
      <td>-87.653040</td>
      <td>casual</td>
    </tr>
  </tbody>
</table>
</div>




```python
bt_202006.dtypes
```




    ride_id                object
    rideable_type          object
    started_at             object
    ended_at               object
    start_station_name     object
    start_station_id        int64
    end_station_name       object
    end_station_id        float64
    start_lat             float64
    start_lng             float64
    end_lat               float64
    end_lng               float64
    member_casual          object
    dtype: object




```python
bt_202006.isna().sum()
```




    ride_id                 0
    rideable_type           0
    started_at              0
    ended_at                0
    start_station_name      0
    start_station_id        0
    end_station_name      468
    end_station_id        468
    start_lat               0
    start_lng               0
    end_lat               468
    end_lng               468
    member_casual           0
    dtype: int64




```python
# drop all NAN values in bt_202006
bt_202006.dropna(inplace=True)
```


```python
# convert 'end_station_id' from floating points to integers
bt_202006['end_station_id'] = bt_202006['end_station_id'].astype('int64')
```

<h4 style="color:Green;">(2-4) dataset: bike trips of July 2020</h4>


```python
bt_202007.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ride_id</th>
      <th>rideable_type</th>
      <th>started_at</th>
      <th>ended_at</th>
      <th>start_station_name</th>
      <th>start_station_id</th>
      <th>end_station_name</th>
      <th>end_station_id</th>
      <th>start_lat</th>
      <th>start_lng</th>
      <th>end_lat</th>
      <th>end_lng</th>
      <th>member_casual</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>762198876D69004D</td>
      <td>docked_bike</td>
      <td>2020-07-09 15:22:02</td>
      <td>2020-07-09 15:25:52</td>
      <td>Ritchie Ct &amp; Banks St</td>
      <td>180.0</td>
      <td>Wells St &amp; Evergreen Ave</td>
      <td>291.0</td>
      <td>41.906866</td>
      <td>-87.626217</td>
      <td>41.906724</td>
      <td>-87.634830</td>
      <td>member</td>
    </tr>
    <tr>
      <th>1</th>
      <td>BEC9C9FBA0D4CF1B</td>
      <td>docked_bike</td>
      <td>2020-07-24 23:56:30</td>
      <td>2020-07-25 00:20:17</td>
      <td>Halsted St &amp; Roscoe St</td>
      <td>299.0</td>
      <td>Broadway &amp; Ridge Ave</td>
      <td>461.0</td>
      <td>41.943670</td>
      <td>-87.648950</td>
      <td>41.984045</td>
      <td>-87.660274</td>
      <td>member</td>
    </tr>
    <tr>
      <th>2</th>
      <td>D2FD8EA432C77EC1</td>
      <td>docked_bike</td>
      <td>2020-07-08 19:49:07</td>
      <td>2020-07-08 19:56:22</td>
      <td>Lake Shore Dr &amp; Diversey Pkwy</td>
      <td>329.0</td>
      <td>Clark St &amp; Wellington Ave</td>
      <td>156.0</td>
      <td>41.932588</td>
      <td>-87.636427</td>
      <td>41.936497</td>
      <td>-87.647539</td>
      <td>casual</td>
    </tr>
    <tr>
      <th>3</th>
      <td>54AE594E20B35881</td>
      <td>docked_bike</td>
      <td>2020-07-17 19:06:42</td>
      <td>2020-07-17 19:27:38</td>
      <td>LaSalle St &amp; Illinois St</td>
      <td>181.0</td>
      <td>Clark St &amp; Armitage Ave</td>
      <td>94.0</td>
      <td>41.890762</td>
      <td>-87.631697</td>
      <td>41.918306</td>
      <td>-87.636282</td>
      <td>casual</td>
    </tr>
    <tr>
      <th>4</th>
      <td>54025FDC7440B56F</td>
      <td>docked_bike</td>
      <td>2020-07-04 10:39:57</td>
      <td>2020-07-04 10:45:05</td>
      <td>Lake Shore Dr &amp; North Blvd</td>
      <td>268.0</td>
      <td>Clark St &amp; Schiller St</td>
      <td>301.0</td>
      <td>41.911722</td>
      <td>-87.626804</td>
      <td>41.907993</td>
      <td>-87.631501</td>
      <td>member</td>
    </tr>
  </tbody>
</table>
</div>




```python
bt_202007.dtypes
```




    ride_id                object
    rideable_type          object
    started_at             object
    ended_at               object
    start_station_name     object
    start_station_id      float64
    end_station_name       object
    end_station_id        float64
    start_lat             float64
    start_lng             float64
    end_lat               float64
    end_lng               float64
    member_casual          object
    dtype: object




```python
bt_202007.isna().sum()
```




    ride_id                 0
    rideable_type           0
    started_at              0
    ended_at                0
    start_station_name    149
    start_station_id      152
    end_station_name      967
    end_station_id        969
    start_lat               0
    start_lng               0
    end_lat               770
    end_lng               770
    member_casual           0
    dtype: int64




```python
# drop all NAN values in bt_202007
bt_202007.dropna(inplace=True)
```


```python
# convert 'start_station_id' column from floating points to integers
bt_202007['start_station_id'] = bt_202007['start_station_id'].astype('int64')

# convert 'end_station_id' column from floating points to integers
bt_202007['end_station_id'] = bt_202007['end_station_id'].astype('int64')
```

<h4 style="color:Green;">(2-5) dataset: bike trips of August 2020</h4>


```python
bt_202008.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ride_id</th>
      <th>rideable_type</th>
      <th>started_at</th>
      <th>ended_at</th>
      <th>start_station_name</th>
      <th>start_station_id</th>
      <th>end_station_name</th>
      <th>end_station_id</th>
      <th>start_lat</th>
      <th>start_lng</th>
      <th>end_lat</th>
      <th>end_lng</th>
      <th>member_casual</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>322BD23D287743ED</td>
      <td>docked_bike</td>
      <td>2020-08-20 18:08:14</td>
      <td>2020-08-20 18:17:51</td>
      <td>Lake Shore Dr &amp; Diversey Pkwy</td>
      <td>329.0</td>
      <td>Clark St &amp; Lincoln Ave</td>
      <td>141.0</td>
      <td>41.932588</td>
      <td>-87.636427</td>
      <td>41.915689</td>
      <td>-87.634600</td>
      <td>member</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2A3AEF1AB9054D8B</td>
      <td>electric_bike</td>
      <td>2020-08-27 18:46:04</td>
      <td>2020-08-27 19:54:51</td>
      <td>Michigan Ave &amp; 14th St</td>
      <td>168.0</td>
      <td>Michigan Ave &amp; 14th St</td>
      <td>168.0</td>
      <td>41.864379</td>
      <td>-87.623681</td>
      <td>41.864221</td>
      <td>-87.623439</td>
      <td>casual</td>
    </tr>
    <tr>
      <th>2</th>
      <td>67DC1D133E8B5816</td>
      <td>electric_bike</td>
      <td>2020-08-26 19:44:14</td>
      <td>2020-08-26 21:53:07</td>
      <td>Columbus Dr &amp; Randolph St</td>
      <td>195.0</td>
      <td>State St &amp; Randolph St</td>
      <td>44.0</td>
      <td>41.884641</td>
      <td>-87.619549</td>
      <td>41.884971</td>
      <td>-87.627574</td>
      <td>casual</td>
    </tr>
    <tr>
      <th>3</th>
      <td>C79FBBD412E578A7</td>
      <td>electric_bike</td>
      <td>2020-08-27 12:05:41</td>
      <td>2020-08-27 12:53:45</td>
      <td>Daley Center Plaza</td>
      <td>81.0</td>
      <td>State St &amp; Kinzie St</td>
      <td>47.0</td>
      <td>41.884093</td>
      <td>-87.629639</td>
      <td>41.889583</td>
      <td>-87.627540</td>
      <td>casual</td>
    </tr>
    <tr>
      <th>4</th>
      <td>13814D3D661ECADB</td>
      <td>electric_bike</td>
      <td>2020-08-27 16:49:02</td>
      <td>2020-08-27 16:59:49</td>
      <td>Leavitt St &amp; Division St</td>
      <td>658.0</td>
      <td>Leavitt St &amp; Division St</td>
      <td>658.0</td>
      <td>41.902989</td>
      <td>-87.683767</td>
      <td>41.903002</td>
      <td>-87.683844</td>
      <td>casual</td>
    </tr>
  </tbody>
</table>
</div>




```python
bt_202008.dtypes
```




    ride_id                object
    rideable_type          object
    started_at             object
    ended_at               object
    start_station_name     object
    start_station_id      float64
    end_station_name       object
    end_station_id        float64
    start_lat             float64
    start_lng             float64
    end_lat               float64
    end_lng               float64
    member_casual          object
    dtype: object




```python
bt_202008.isna().sum()
```




    ride_id                   0
    rideable_type             0
    started_at                0
    ended_at                  0
    start_station_name     7595
    start_station_id       7691
    end_station_name      10035
    end_station_id        10110
    start_lat                 0
    start_lng                 0
    end_lat                 938
    end_lng                 938
    member_casual             0
    dtype: int64




```python
# drop all NAN values in bt_202008
bt_202008.dropna(inplace=True)
```


```python
# convert 'start_station_id' column from floating points to integers
bt_202008['start_station_id'] = bt_202008['start_station_id'].astype('int64')

# convert 'end_station_id' column from floating points to integers
bt_202008['end_station_id'] = bt_202008['end_station_id'].astype('int64')
```

<h4 style="color:Green;">(2-6) dataset: bike trips of September 2020</h4>


```python
bt_202009.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ride_id</th>
      <th>rideable_type</th>
      <th>started_at</th>
      <th>ended_at</th>
      <th>start_station_name</th>
      <th>start_station_id</th>
      <th>end_station_name</th>
      <th>end_station_id</th>
      <th>start_lat</th>
      <th>start_lng</th>
      <th>end_lat</th>
      <th>end_lng</th>
      <th>member_casual</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2B22BD5F95FB2629</td>
      <td>electric_bike</td>
      <td>2020-09-17 14:27:11</td>
      <td>2020-09-17 14:44:24</td>
      <td>Michigan Ave &amp; Lake St</td>
      <td>52.0</td>
      <td>Green St &amp; Randolph St</td>
      <td>112.0</td>
      <td>41.886692</td>
      <td>-87.623561</td>
      <td>41.883570</td>
      <td>-87.648731</td>
      <td>casual</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A7FB70B4AFC6CAF2</td>
      <td>electric_bike</td>
      <td>2020-09-17 15:07:31</td>
      <td>2020-09-17 15:07:45</td>
      <td>W Oakdale Ave &amp; N Broadway</td>
      <td>NaN</td>
      <td>W Oakdale Ave &amp; N Broadway</td>
      <td>NaN</td>
      <td>41.940000</td>
      <td>-87.640000</td>
      <td>41.940000</td>
      <td>-87.640000</td>
      <td>casual</td>
    </tr>
    <tr>
      <th>2</th>
      <td>86057FA01BAC778E</td>
      <td>electric_bike</td>
      <td>2020-09-17 15:09:04</td>
      <td>2020-09-17 15:09:35</td>
      <td>W Oakdale Ave &amp; N Broadway</td>
      <td>NaN</td>
      <td>W Oakdale Ave &amp; N Broadway</td>
      <td>NaN</td>
      <td>41.940000</td>
      <td>-87.640000</td>
      <td>41.940000</td>
      <td>-87.640000</td>
      <td>casual</td>
    </tr>
    <tr>
      <th>3</th>
      <td>57F6DC9A153DB98C</td>
      <td>electric_bike</td>
      <td>2020-09-17 18:10:46</td>
      <td>2020-09-17 18:35:49</td>
      <td>Ashland Ave &amp; Belle Plaine Ave</td>
      <td>246.0</td>
      <td>Montrose Harbor</td>
      <td>249.0</td>
      <td>41.956060</td>
      <td>-87.668916</td>
      <td>41.963985</td>
      <td>-87.638216</td>
      <td>casual</td>
    </tr>
    <tr>
      <th>4</th>
      <td>B9C4712F78C1AE68</td>
      <td>electric_bike</td>
      <td>2020-09-17 15:16:13</td>
      <td>2020-09-17 15:52:55</td>
      <td>Fairbanks Ct &amp; Grand Ave</td>
      <td>24.0</td>
      <td>Fairbanks Ct &amp; Grand Ave</td>
      <td>24.0</td>
      <td>41.891860</td>
      <td>-87.621008</td>
      <td>41.891346</td>
      <td>-87.620325</td>
      <td>casual</td>
    </tr>
  </tbody>
</table>
</div>




```python
bt_202009.dtypes
```




    ride_id                object
    rideable_type          object
    started_at             object
    ended_at               object
    start_station_name     object
    start_station_id      float64
    end_station_name       object
    end_station_id        float64
    start_lat             float64
    start_lng             float64
    end_lat               float64
    end_lng               float64
    member_casual          object
    dtype: object




```python
bt_202009.isna().sum()
```




    ride_id                   0
    rideable_type             0
    started_at                0
    ended_at                  0
    start_station_name    19691
    start_station_id      19901
    end_station_name      23373
    end_station_id        23524
    start_lat                 0
    start_lng                 0
    end_lat                 789
    end_lng                 789
    member_casual             0
    dtype: int64




```python
# drop all NAN values in bt_202009
bt_202009.dropna(inplace=True)
```


```python
# convert 'start_station_id' column from floating points to integers
bt_202009['start_station_id'] = bt_202009['start_station_id'].astype('int64')

# convert 'end_station_id' column from floating points to integers
bt_202009['end_station_id'] = bt_202009['end_station_id'].astype('int64')
```

<h4 style="color:Green;">(2-7) dataset: bike trips of October 2020</h4>


```python
bt_202010.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ride_id</th>
      <th>rideable_type</th>
      <th>started_at</th>
      <th>ended_at</th>
      <th>start_station_name</th>
      <th>start_station_id</th>
      <th>end_station_name</th>
      <th>end_station_id</th>
      <th>start_lat</th>
      <th>start_lng</th>
      <th>end_lat</th>
      <th>end_lng</th>
      <th>member_casual</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ACB6B40CF5B9044C</td>
      <td>electric_bike</td>
      <td>2020-10-31 19:39:43</td>
      <td>2020-10-31 19:57:12</td>
      <td>Lakeview Ave &amp; Fullerton Pkwy</td>
      <td>313.0</td>
      <td>Rush St &amp; Hubbard St</td>
      <td>125.0</td>
      <td>41.926101</td>
      <td>-87.638977</td>
      <td>41.890345</td>
      <td>-87.626068</td>
      <td>casual</td>
    </tr>
    <tr>
      <th>1</th>
      <td>DF450C72FD109C01</td>
      <td>electric_bike</td>
      <td>2020-10-31 23:50:08</td>
      <td>2020-11-01 00:04:16</td>
      <td>Southport Ave &amp; Waveland Ave</td>
      <td>227.0</td>
      <td>Kedzie Ave &amp; Milwaukee Ave</td>
      <td>260.0</td>
      <td>41.948172</td>
      <td>-87.663911</td>
      <td>41.929528</td>
      <td>-87.707818</td>
      <td>casual</td>
    </tr>
    <tr>
      <th>2</th>
      <td>B6396B54A15AC0DF</td>
      <td>electric_bike</td>
      <td>2020-10-31 23:00:01</td>
      <td>2020-10-31 23:08:22</td>
      <td>Stony Island Ave &amp; 67th St</td>
      <td>102.0</td>
      <td>University Ave &amp; 57th St</td>
      <td>423.0</td>
      <td>41.773462</td>
      <td>-87.585372</td>
      <td>41.791455</td>
      <td>-87.600050</td>
      <td>casual</td>
    </tr>
    <tr>
      <th>3</th>
      <td>44A4AEE261B9E854</td>
      <td>electric_bike</td>
      <td>2020-10-31 22:16:43</td>
      <td>2020-10-31 22:19:35</td>
      <td>Clark St &amp; Grace St</td>
      <td>165.0</td>
      <td>Broadway &amp; Sheridan Rd</td>
      <td>256.0</td>
      <td>41.950855</td>
      <td>-87.659244</td>
      <td>41.952809</td>
      <td>-87.650103</td>
      <td>casual</td>
    </tr>
    <tr>
      <th>4</th>
      <td>10B7DD76A6A2EB95</td>
      <td>electric_bike</td>
      <td>2020-10-31 19:38:19</td>
      <td>2020-10-31 19:54:32</td>
      <td>Southport Ave &amp; Wrightwood Ave</td>
      <td>190.0</td>
      <td>Stave St &amp; Armitage Ave</td>
      <td>185.0</td>
      <td>41.928857</td>
      <td>-87.663962</td>
      <td>41.917777</td>
      <td>-87.691434</td>
      <td>casual</td>
    </tr>
  </tbody>
</table>
</div>




```python
bt_202010.dtypes
```




    ride_id                object
    rideable_type          object
    started_at             object
    ended_at               object
    start_station_name     object
    start_station_id      float64
    end_station_name       object
    end_station_id        float64
    start_lat             float64
    start_lng             float64
    end_lat               float64
    end_lng               float64
    member_casual          object
    dtype: object




```python
bt_202010.isna().sum()
```




    ride_id                   0
    rideable_type             0
    started_at                0
    ended_at                  0
    start_station_name    31198
    start_station_id      31405
    end_station_name      35631
    end_station_id        35787
    start_lat                 0
    start_lng                 0
    end_lat                 474
    end_lng                 474
    member_casual             0
    dtype: int64




```python
# drop all NAN values in bt_202010
bt_202010.dropna(inplace=True)
```


```python
# convert 'start_station_id' column from floating points to integers
bt_202010['start_station_id'] = bt_202010['start_station_id'].astype('int64')

# convert 'end_station_id' column from floating points to integers
bt_202010['end_station_id'] = bt_202010['end_station_id'].astype('int64')
```

<h4 style="color:Green;">(2-8) dataset: bike trips of November 2020</h4>


```python
bt_202011.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ride_id</th>
      <th>rideable_type</th>
      <th>started_at</th>
      <th>ended_at</th>
      <th>start_station_name</th>
      <th>start_station_id</th>
      <th>end_station_name</th>
      <th>end_station_id</th>
      <th>start_lat</th>
      <th>start_lng</th>
      <th>end_lat</th>
      <th>end_lng</th>
      <th>member_casual</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>BD0A6FF6FFF9B921</td>
      <td>electric_bike</td>
      <td>2020-11-01 13:36:00</td>
      <td>2020-11-01 13:45:40</td>
      <td>Dearborn St &amp; Erie St</td>
      <td>110.0</td>
      <td>St. Clair St &amp; Erie St</td>
      <td>211.0</td>
      <td>41.894177</td>
      <td>-87.629127</td>
      <td>41.894434</td>
      <td>-87.623379</td>
      <td>casual</td>
    </tr>
    <tr>
      <th>1</th>
      <td>96A7A7A4BDE4F82D</td>
      <td>electric_bike</td>
      <td>2020-11-01 10:03:26</td>
      <td>2020-11-01 10:14:45</td>
      <td>Franklin St &amp; Illinois St</td>
      <td>672.0</td>
      <td>Noble St &amp; Milwaukee Ave</td>
      <td>29.0</td>
      <td>41.890959</td>
      <td>-87.635343</td>
      <td>41.900675</td>
      <td>-87.662480</td>
      <td>casual</td>
    </tr>
    <tr>
      <th>2</th>
      <td>C61526D06582BDC5</td>
      <td>electric_bike</td>
      <td>2020-11-01 00:34:05</td>
      <td>2020-11-01 01:03:06</td>
      <td>Lake Shore Dr &amp; Monroe St</td>
      <td>76.0</td>
      <td>Federal St &amp; Polk St</td>
      <td>41.0</td>
      <td>41.880983</td>
      <td>-87.616754</td>
      <td>41.872054</td>
      <td>-87.629550</td>
      <td>casual</td>
    </tr>
    <tr>
      <th>3</th>
      <td>E533E89C32080B9E</td>
      <td>electric_bike</td>
      <td>2020-11-01 00:45:16</td>
      <td>2020-11-01 00:54:31</td>
      <td>Leavitt St &amp; Chicago Ave</td>
      <td>659.0</td>
      <td>Stave St &amp; Armitage Ave</td>
      <td>185.0</td>
      <td>41.895499</td>
      <td>-87.682013</td>
      <td>41.917744</td>
      <td>-87.691392</td>
      <td>casual</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1C9F4EF18C168C60</td>
      <td>electric_bike</td>
      <td>2020-11-01 15:43:25</td>
      <td>2020-11-01 16:16:52</td>
      <td>Buckingham Fountain</td>
      <td>2.0</td>
      <td>Buckingham Fountain</td>
      <td>2.0</td>
      <td>41.876497</td>
      <td>-87.620358</td>
      <td>41.876448</td>
      <td>-87.620338</td>
      <td>casual</td>
    </tr>
  </tbody>
</table>
</div>




```python
bt_202011.dtypes
```




    ride_id                object
    rideable_type          object
    started_at             object
    ended_at               object
    start_station_name     object
    start_station_id      float64
    end_station_name       object
    end_station_id        float64
    start_lat             float64
    start_lng             float64
    end_lat               float64
    end_lng               float64
    member_casual          object
    dtype: object




```python
bt_202011.isna().sum()
```




    ride_id                   0
    rideable_type             0
    started_at                0
    ended_at                  0
    start_station_name    24324
    start_station_id      24434
    end_station_name      26749
    end_station_id        26826
    start_lat                 0
    start_lng                 0
    end_lat                 284
    end_lng                 284
    member_casual             0
    dtype: int64




```python
# drop all NAN values in bt_202011
bt_202011.dropna(inplace=True)
```


```python
# convert 'start_station_id' column from floating points to integers
bt_202011['start_station_id'] = bt_202011['start_station_id'].astype('int64')

# convert 'end_station_id' column from floating points to integers
bt_202011['end_station_id'] = bt_202011['end_station_id'].astype('int64')
```

<h4 style="color:Green;">(2-9) dataset: bike trips of December 2020</h4>


```python
bt_202012.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ride_id</th>
      <th>rideable_type</th>
      <th>started_at</th>
      <th>ended_at</th>
      <th>start_station_name</th>
      <th>start_station_id</th>
      <th>end_station_name</th>
      <th>end_station_id</th>
      <th>start_lat</th>
      <th>start_lng</th>
      <th>end_lat</th>
      <th>end_lng</th>
      <th>member_casual</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>70B6A9A437D4C30D</td>
      <td>classic_bike</td>
      <td>2020-12-27 12:44:29</td>
      <td>2020-12-27 12:55:06</td>
      <td>Aberdeen St &amp; Jackson Blvd</td>
      <td>13157</td>
      <td>Desplaines St &amp; Kinzie St</td>
      <td>TA1306000003</td>
      <td>41.877726</td>
      <td>-87.654787</td>
      <td>41.888716</td>
      <td>-87.644448</td>
      <td>member</td>
    </tr>
    <tr>
      <th>1</th>
      <td>158A465D4E74C54A</td>
      <td>electric_bike</td>
      <td>2020-12-18 17:37:15</td>
      <td>2020-12-18 17:44:19</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>41.930000</td>
      <td>-87.700000</td>
      <td>41.910000</td>
      <td>-87.700000</td>
      <td>member</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5262016E0F1F2F9A</td>
      <td>electric_bike</td>
      <td>2020-12-15 15:04:33</td>
      <td>2020-12-15 15:11:28</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>41.910000</td>
      <td>-87.690000</td>
      <td>41.930000</td>
      <td>-87.700000</td>
      <td>member</td>
    </tr>
    <tr>
      <th>3</th>
      <td>BE119628E44F871E</td>
      <td>electric_bike</td>
      <td>2020-12-15 15:54:18</td>
      <td>2020-12-15 16:00:11</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>41.920000</td>
      <td>-87.700000</td>
      <td>41.910000</td>
      <td>-87.700000</td>
      <td>member</td>
    </tr>
    <tr>
      <th>4</th>
      <td>69AF78D57854E110</td>
      <td>electric_bike</td>
      <td>2020-12-22 12:08:17</td>
      <td>2020-12-22 12:10:59</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>41.800000</td>
      <td>-87.590000</td>
      <td>41.800000</td>
      <td>-87.590000</td>
      <td>member</td>
    </tr>
  </tbody>
</table>
</div>




```python
bt_202012.dtypes
```




    ride_id                object
    rideable_type          object
    started_at             object
    ended_at               object
    start_station_name     object
    start_station_id       object
    end_station_name       object
    end_station_id         object
    start_lat             float64
    start_lng             float64
    end_lat               float64
    end_lng               float64
    member_casual          object
    dtype: object




```python
bt_202012.isna().sum()
```




    ride_id                   0
    rideable_type             0
    started_at                0
    ended_at                  0
    start_station_name    11699
    start_station_id      11699
    end_station_name      13237
    end_station_id        13237
    start_lat                 0
    start_lng                 0
    end_lat                 111
    end_lng                 111
    member_casual             0
    dtype: int64




```python
# drop all NAN values in bt_202012
bt_202012.dropna(inplace=True)
```

<h4 style="color:Red;"> After examinging the 'start_station_id' column and 'end_station_id' in this dataset, I found an inconsistency issue between station ids and their corresponding names. Specifically, if a start or end station's name is "Rhodes Ave & 32nd St", then its corresponding id is 263 in all previous nine datasets, but in this dataset it is associated with id 13215. </h4>
    
<h4 style="color:Red;"> Therefore, I will re-validate the correct ids from cross-referecing all previous datasets, and then cast these two columns into integer datatype. </h4>


```python
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
```

<h4 style="color:Blue;"> The function 'correct_station_name_id' below will grab all start station names and end station names from the input dataframe, determine if each station's name appears in the previous 8 datasets: </h4>

- <p style="color:Blue;"> if it does exist, update its corresponding id from the input dataframe to the correct one; </p>
- <p style="color:Blue;"> if it does not exist, mark the station's name in a list 'not_changed' for further cleaning.</p>


```python
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
```


```python
# update stations' ids in bt_202012 and catch stations that're not existed from previous 8 datasets
correct_station_name_id(bt_202012)
```

    These stations below are not existed in the previous 8 datasets:





    ['N Green St & W Lake St',
     'W Armitage Ave & N Sheffield Ave',
     'W Oakdale Ave & N Broadway',
     'Base - 2132 W Hubbard Warehouse',
     'N Carpenter St & W Lake St']



<h4 style="color:Red;"> As showed above, 5 station names were caught as exceptions in the list not_changed </h4>
    
<h4 style="color:Red;"> Meanwhile, I've examined the rest 3 datasets, and I found in these 3 datasets these 5 station names and their corresponding ids are not correct as well. </h4>

<h4 style="color:Blue;"> Therefore, I've found the official dataset of all Divvy Bicycle Stations at <a href="https://data.cityofchicago.org/d/bbyy-e7gq?category=Transportation&view_name=Divvy-Bicycle-Stations"> here </a> on <a href="httP://data.cityofchicago.org"> The Chicago Data Portal website </a></h4>

<h4 style="color:Blue;"> I will download this dataset and import it below as the official reference to get the correct station names and/or corresponding ids.</h4>


```python
# import the official bike stations information dataset
official_station_info = pd.read_csv('~/00_PROJECTS/cs_1_bike_share/original_datasets/official_bike_stations_info.csv')

# get the station name and id in pairs from the official station information dataset
official_station_name_id = dict(zip(official_station_info['Station Name'], official_station_info['ID']))
```


```python
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
```


```python
# get the correct ids of exceptional stations in list not_changed
get_correct_id()
```

    N Green St & W Lake St :  1436495109493626546
    
    W Armitage Ave & N Sheffield Ave :  1436495105198659242
    
    W Oakdale Ave & N Broadway :  1436495100903691938
    
    N Carpenter St & W Lake St :  1436495105198659246
    
    These stations below cannot be found in the official stations information dataset:





    ['Base - 2132 W Hubbard Warehouse']



<h4 style="color:red;"> The station 'Base - 2132 W Hubbard Warehouse' cannot be found in the official station information dataset. Due to lack of information, I will drop these records. </h4>


```python
# drop records with start_station_name as 'Base - 2132 W Hubbard Warehouse'
bt_202012.drop(bt_202012[bt_202012['start_station_name'] == 'Base - 2132 W Hubbard Warehouse'].index, inplace=True)

# drop records with end_station_name as 'Base - 2132 W Hubbard Warehouse'
bt_202012.drop(bt_202012[bt_202012['end_station_name'] == 'Base - 2132 W Hubbard Warehouse'].index, inplace=True)
```

<h4 style="color:blue;"> For the other 4 stations, I will manually update the ids in bt_202012 </h4>


```python
# update station's id with name of 'N Green St & W Lake St'
filt_a1 = (bt_202012['start_station_name'] == 'N Green St & W Lake St')
bt_202012.loc[filt_a1, 'start_station_id'] = 1436495109493626546

filt_a2 = (bt_202012['end_station_name'] == 'N Green St & W Lake St')
bt_202012.loc[filt_a2, 'end_station_id'] = 1436495109493626546
```


```python
# update station's id with name of 'W Oakdale Ave & N Broadway'
filt_b1 = (bt_202012['start_station_name'] == 'W Oakdale Ave & N Broadway')
bt_202012.loc[filt_b1, 'start_station_id'] = 1436495100903691938

filt_b2 = (bt_202012['end_station_name'] == 'W Oakdale Ave & N Broadway')
bt_202012.loc[filt_b2, 'end_station_id'] = 1436495100903691938
```


```python
# update station's id with name of 'W Armitage Ave & N Sheffield Ave'
filt_c1 = (bt_202012['start_station_name'] == 'W Armitage Ave & N Sheffield Ave')
bt_202012.loc[filt_c1, 'start_station_id'] = 1436495105198659242

filt_c2 = (bt_202012['end_station_name'] == 'W Armitage Ave & N Sheffield Ave')
bt_202012.loc[filt_c2, 'end_station_id'] = 1436495105198659242
```


```python
# update station's id with name of 'N Carpenter St & W Lake St'
filt_d1 = (bt_202012['start_station_name'] == 'N Carpenter St & W Lake St')
bt_202012.loc[filt_d1, 'start_station_id'] = 1436495105198659246

filt_d2 = (bt_202012['end_station_name'] == 'N Carpenter St & W Lake St')
bt_202012.loc[filt_d2, 'end_station_id'] = 1436495105198659246
```

<h4 style="color:green;"> (2-10) dataset: bike trips of January 2021 </h4>


```python
bt_202101.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ride_id</th>
      <th>rideable_type</th>
      <th>started_at</th>
      <th>ended_at</th>
      <th>start_station_name</th>
      <th>start_station_id</th>
      <th>end_station_name</th>
      <th>end_station_id</th>
      <th>start_lat</th>
      <th>start_lng</th>
      <th>end_lat</th>
      <th>end_lng</th>
      <th>member_casual</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>E19E6F1B8D4C42ED</td>
      <td>electric_bike</td>
      <td>2021-01-23 16:14:19</td>
      <td>2021-01-23 16:24:44</td>
      <td>California Ave &amp; Cortez St</td>
      <td>17660</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>41.900341</td>
      <td>-87.696743</td>
      <td>41.89</td>
      <td>-87.72</td>
      <td>member</td>
    </tr>
    <tr>
      <th>1</th>
      <td>DC88F20C2C55F27F</td>
      <td>electric_bike</td>
      <td>2021-01-27 18:43:08</td>
      <td>2021-01-27 18:47:12</td>
      <td>California Ave &amp; Cortez St</td>
      <td>17660</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>41.900333</td>
      <td>-87.696707</td>
      <td>41.90</td>
      <td>-87.69</td>
      <td>member</td>
    </tr>
    <tr>
      <th>2</th>
      <td>EC45C94683FE3F27</td>
      <td>electric_bike</td>
      <td>2021-01-21 22:35:54</td>
      <td>2021-01-21 22:37:14</td>
      <td>California Ave &amp; Cortez St</td>
      <td>17660</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>41.900313</td>
      <td>-87.696643</td>
      <td>41.90</td>
      <td>-87.70</td>
      <td>member</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4FA453A75AE377DB</td>
      <td>electric_bike</td>
      <td>2021-01-07 13:31:13</td>
      <td>2021-01-07 13:42:55</td>
      <td>California Ave &amp; Cortez St</td>
      <td>17660</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>41.900399</td>
      <td>-87.696662</td>
      <td>41.92</td>
      <td>-87.69</td>
      <td>member</td>
    </tr>
    <tr>
      <th>4</th>
      <td>BE5E8EB4E7263A0B</td>
      <td>electric_bike</td>
      <td>2021-01-23 02:24:02</td>
      <td>2021-01-23 02:24:45</td>
      <td>California Ave &amp; Cortez St</td>
      <td>17660</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>41.900326</td>
      <td>-87.696697</td>
      <td>41.90</td>
      <td>-87.70</td>
      <td>casual</td>
    </tr>
  </tbody>
</table>
</div>




```python
bt_202101.dtypes
```




    ride_id                object
    rideable_type          object
    started_at             object
    ended_at               object
    start_station_name     object
    start_station_id       object
    end_station_name       object
    end_station_id         object
    start_lat             float64
    start_lng             float64
    end_lat               float64
    end_lng               float64
    member_casual          object
    dtype: object




```python
bt_202101.isna().sum()
```




    ride_id                   0
    rideable_type             0
    started_at                0
    ended_at                  0
    start_station_name     8625
    start_station_id       8625
    end_station_name      10277
    end_station_id        10277
    start_lat                 0
    start_lng                 0
    end_lat                 103
    end_lng                 103
    member_casual             0
    dtype: int64




```python
# drop all NAN values in bt_202101
bt_202101.dropna(inplace=True)
```

<h4 style="color:red;"> After examinging the 'start_station_id' column and 'end_station_id' in this dataset, I found the same inconsistency issue between station ids and their corresponding names as before. </h4>
    
<h4 style="color:blue;"> Therefore, I will re-run the whole process of validating station names with corresponding ids as before using: </h4>

- <p style="color:blue;"> the official stations information dataset from Chicago Data Portral website;</p>
- <p style="color:blue;"> the dictionary "station_id" of all stations and ids existed in the previous 8 datasets;</p>
- <p style="color:blue;"> the function "correct_station_name_id" to either update ids or catch exceptions;</p>
- <p style="color:blue;"> the function "get_correct_id" to grab the correct ids for exceptions.</p>


```python
# reset the not_changed list to empty
not_changed = []

# update stations' ids in bt_202101 or catch stations that're not existed from previous 8 datasets
correct_station_name_id(bt_202101)
```

    These stations below are not existed in the previous 8 datasets:





    ['N Green St & W Lake St',
     'W Armitage Ave & N Sheffield Ave',
     'N Southport Ave & W Newport Ave',
     'N Sheffield Ave & W Wellington Ave',
     'Malcolm X College Vaccination Site',
     'W Oakdale Ave & N Broadway',
     'Base - 2132 W Hubbard Warehouse',
     'N Paulina St & Lincoln Ave',
     'Broadway & Wilson - Truman College Vaccination Site',
     'Western & 28th - Velasquez Institute Vaccination Site',
     'N Damen Ave & W Wabansia St',
     'Avenue L & 114th St',
     'W Washington Blvd & N Peoria St',
     'N Carpenter St & W Lake St']




```python
# get the correct ids of exceptional stations in list not_changed
get_correct_id()
```

    N Green St & W Lake St :  1436495109493626546
    
    W Armitage Ave & N Sheffield Ave :  1436495105198659242
    
    N Southport Ave & W Newport Ave :  1436495115557663136
    
    N Sheffield Ave & W Wellington Ave :  1436495118083561146
    
    Malcolm X College Vaccination Site :  631
    
    W Oakdale Ave & N Broadway :  1436495100903691938
    
    N Paulina St & Lincoln Ave :  1436495122378528446
    
    Broadway & Wilson - Truman College Vaccination Site :  293
    
    Western & 28th - Velasquez Institute Vaccination Site :  446
    
    Avenue L & 114th St :  1448642175142467184
    
    W Washington Blvd & N Peoria St :  1436495109493626544
    
    N Carpenter St & W Lake St :  1436495105198659246
    
    These stations below cannot be found in the official stations information dataset:





    ['Base - 2132 W Hubbard Warehouse', 'N Damen Ave & W Wabansia St']



<h4 style="color:red;"> The stations 'Base - 2132 W Hubbard Warehouse' and 'N Damen Ave & W Wabansia St' cannot be found in the official station information dataset. Due to lack of information, I will drop these records. </h4>


```python
# drop records with start_station_name as 'Base - 2132 W Hubbard Warehouse'
bt_202101.drop(bt_202101[bt_202101['start_station_name'] == 'Base - 2132 W Hubbard Warehouse'].index, inplace=True)

# drop records with end_station_name as 'Base - 2132 W Hubbard Warehouse'
bt_202101.drop(bt_202101[bt_202101['end_station_name'] == 'Base - 2132 W Hubbard Warehouse'].index, inplace=True)

# drop records with start_station_name as 'N Damen Ave & W Wabansia St'
bt_202101.drop(bt_202101[bt_202101['start_station_name'] == 'N Damen Ave & W Wabansia St'].index, inplace=True)

# drop records with end_station_name as 'N Damen Ave & W Wabansia St'
bt_202101.drop(bt_202101[bt_202101['end_station_name'] == 'N Damen Ave & W Wabansia St'].index, inplace=True)
```

<h4 style="color:blue;"> For the other 12 stations, I will manually update the ids in bt_202101 </h4>


```python
# update station's id with name of 'Malcolm X College Vaccination Site'
filt_a1 = (bt_202101['start_station_name'] == 'Malcolm X College Vaccination Site')
bt_202101.loc[filt_a1, 'start_station_id'] = 631

filt_a2 = (bt_202101['end_station_name'] == 'Malcolm X College Vaccination Site')
bt_202101.loc[filt_a2, 'end_station_id'] = 631
```


```python
# update station's id with name of 'N Southport Ave & W Newport Ave'
filt_b1 = (bt_202101['start_station_name'] == 'N Southport Ave & W Newport Ave')
bt_202101.loc[filt_b1, 'start_station_id'] = 1436495115557663136

filt_b2 = (bt_202101['end_station_name'] == 'N Southport Ave & W Newport Ave')
bt_202101.loc[filt_b2, 'end_station_id'] = 1436495115557663136
```


```python
# update station's id with name of 'N Sheffield Ave & W Wellington Ave'
filt_c1 = (bt_202101['start_station_name'] == 'N Sheffield Ave & W Wellington Ave')
bt_202101.loc[filt_c1, 'start_station_id'] = 1436495118083561146

filt_c2 = (bt_202101['end_station_name'] == 'N Sheffield Ave & W Wellington Ave')
bt_202101.loc[filt_c2, 'end_station_id'] = 1436495115557663136
```


```python
# update station's id with name of 'N Paulina St & Lincoln Ave'
filt_d1 = (bt_202101['start_station_name'] == 'N Paulina St & Lincoln Ave')
bt_202101.loc[filt_d1, 'start_station_id'] = 1436495122378528446
```


```python
# update station's id with name of 'N Green St & W Lake St'
filt_e1 = (bt_202101['start_station_name'] == 'N Green St & W Lake St')
bt_202101.loc[filt_e1, 'start_station_id'] = 1436495109493626546

filt_e2 = (bt_202101['end_station_name'] == 'N Green St & W Lake St')
bt_202101.loc[filt_e2, 'end_station_id'] = 1436495109493626546
```


```python
# update station's id with name of 'W Oakdale Ave & N Broadway'
filt_f1 = (bt_202101['start_station_name'] == 'W Oakdale Ave & N Broadway')
bt_202101.loc[filt_f1, 'start_station_id'] = 1436495100903691938

filt_f2 = (bt_202101['end_station_name'] == 'W Oakdale Ave & N Broadway')
bt_202101.loc[filt_f2, 'end_station_id'] = 1436495100903691938
```


```python
# update station's id with name of 'W Armitage Ave & N Sheffield Ave'
filt_g1 = (bt_202101['start_station_name'] == 'W Armitage Ave & N Sheffield Ave')
bt_202101.loc[filt_g1, 'start_station_id'] = 1436495105198659242

filt_g2 = (bt_202101['end_station_name'] == 'W Armitage Ave & N Sheffield Ave')
bt_202101.loc[filt_g2, 'end_station_id'] = 1436495105198659242
```


```python
# update station's id with name of 'Broadway & Wilson - Truman College Vaccination Site'
filt_h1 = (bt_202101['start_station_name'] == 'Broadway & Wilson - Truman College Vaccination Site')
bt_202101.loc[filt_h1, 'start_station_id'] = 293

filt_h2 = (bt_202101['end_station_name'] == 'Broadway & Wilson - Truman College Vaccination Site')
bt_202101.loc[filt_h2, 'end_station_id'] = 293
```


```python
# update station's id with name of 'N Carpenter St & W Lake St'
filt_i1 = (bt_202101['end_station_name'] == 'N Carpenter St & W Lake St')
bt_202101.loc[filt_i1, 'end_station_id'] = 1436495105198659246
```


```python
# update station's id with name of 'Western & 28th - Velasquez Institute Vaccination Site'
filt_j1 = (bt_202101['end_station_name'] == 'Western & 28th - Velasquez Institute Vaccination Site')
bt_202101.loc[filt_j1, 'end_station_id'] = 446
```


```python
# update station's id with name of 'W Washington Blvd & N Peoria St'
filt_k1 = (bt_202101['end_station_name'] == 'W Washington Blvd & N Peoria St')
bt_202101.loc[filt_k1, 'end_station_id'] = 1436495109493626544
```


```python
# update station's id with name of 'Avenue L & 114th St'
filt_l1 = (bt_202101['end_station_name'] == 'Avenue L & 114th St')
bt_202101.loc[filt_l1, 'end_station_id'] = 1448642175142467184
```

<h4 style="color:green;"> (2-11) dataset: bike trips of Feburary 2021 </h4>


```python
bt_202102.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ride_id</th>
      <th>rideable_type</th>
      <th>started_at</th>
      <th>ended_at</th>
      <th>start_station_name</th>
      <th>start_station_id</th>
      <th>end_station_name</th>
      <th>end_station_id</th>
      <th>start_lat</th>
      <th>start_lng</th>
      <th>end_lat</th>
      <th>end_lng</th>
      <th>member_casual</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>89E7AA6C29227EFF</td>
      <td>classic_bike</td>
      <td>2021-02-12 16:14:56</td>
      <td>2021-02-12 16:21:43</td>
      <td>Glenwood Ave &amp; Touhy Ave</td>
      <td>525</td>
      <td>Sheridan Rd &amp; Columbia Ave</td>
      <td>660</td>
      <td>42.012701</td>
      <td>-87.666058</td>
      <td>42.004583</td>
      <td>-87.661406</td>
      <td>member</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0FEFDE2603568365</td>
      <td>classic_bike</td>
      <td>2021-02-14 17:52:38</td>
      <td>2021-02-14 18:12:09</td>
      <td>Glenwood Ave &amp; Touhy Ave</td>
      <td>525</td>
      <td>Bosworth Ave &amp; Howard St</td>
      <td>16806</td>
      <td>42.012701</td>
      <td>-87.666058</td>
      <td>42.019537</td>
      <td>-87.669563</td>
      <td>casual</td>
    </tr>
    <tr>
      <th>2</th>
      <td>E6159D746B2DBB91</td>
      <td>electric_bike</td>
      <td>2021-02-09 19:10:18</td>
      <td>2021-02-09 19:19:10</td>
      <td>Clark St &amp; Lake St</td>
      <td>KA1503000012</td>
      <td>State St &amp; Randolph St</td>
      <td>TA1305000029</td>
      <td>41.885795</td>
      <td>-87.631101</td>
      <td>41.884866</td>
      <td>-87.627498</td>
      <td>member</td>
    </tr>
    <tr>
      <th>3</th>
      <td>B32D3199F1C2E75B</td>
      <td>classic_bike</td>
      <td>2021-02-02 17:49:41</td>
      <td>2021-02-02 17:54:06</td>
      <td>Wood St &amp; Chicago Ave</td>
      <td>637</td>
      <td>Honore St &amp; Division St</td>
      <td>TA1305000034</td>
      <td>41.895634</td>
      <td>-87.672069</td>
      <td>41.903119</td>
      <td>-87.673935</td>
      <td>member</td>
    </tr>
    <tr>
      <th>4</th>
      <td>83E463F23575F4BF</td>
      <td>electric_bike</td>
      <td>2021-02-23 15:07:23</td>
      <td>2021-02-23 15:22:37</td>
      <td>State St &amp; 33rd St</td>
      <td>13216</td>
      <td>Emerald Ave &amp; 31st St</td>
      <td>TA1309000055</td>
      <td>41.834733</td>
      <td>-87.625827</td>
      <td>41.838163</td>
      <td>-87.645123</td>
      <td>member</td>
    </tr>
  </tbody>
</table>
</div>




```python
bt_202102.dtypes
```




    ride_id                object
    rideable_type          object
    started_at             object
    ended_at               object
    start_station_name     object
    start_station_id       object
    end_station_name       object
    end_station_id         object
    start_lat             float64
    start_lng             float64
    end_lat               float64
    end_lng               float64
    member_casual          object
    dtype: object




```python
bt_202102.isna().sum()
```




    ride_id                  0
    rideable_type            0
    started_at               0
    ended_at                 0
    start_station_name    4046
    start_station_id      4046
    end_station_name      5358
    end_station_id        5358
    start_lat                0
    start_lng                0
    end_lat                214
    end_lng                214
    member_casual            0
    dtype: int64




```python
# drop all NAN values in bt_202102
bt_202102.dropna(inplace=True)
```

<h4 style="color:red;"> After examinging the 'start_station_id' column and 'end_station_id' in this dataset, I found the same inconsistency issue between station ids and their corresponding names as before. </h4>
    
<h4 style="color:blue;"> Therefore, I will re-run the whole process of validating station names with corresponding ids as before using: </h4>

- <p style="color:blue;"> the official stations information dataset from Chicago Data Portral website;</p>
- <p style="color:blue;"> the dictionary "station_id" of all stations and ids existed in the previous 8 datasets;</p>
- <p style="color:blue;"> the function "correct_station_name_id" to either update ids or catch exceptions;</p>
- <p style="color:blue;"> the function "get_correct_id" to grab the correct ids for exceptions.</p>


```python
# reset the not_changed list to empty
not_changed = []

# update stations' ids in bt_202102 or catch stations that're not existed from previous 8 datasets
correct_station_name_id(bt_202102)
```

    These stations below are not existed in the previous 8 datasets:





    ['W Armitage Ave & N Sheffield Ave',
     'Malcolm X College Vaccination Site',
     'W Washington Blvd & N Peoria St',
     'W Oakdale Ave & N Broadway',
     'Base - 2132 W Hubbard Warehouse',
     'N Paulina St & Lincoln Ave',
     'Broadway & Wilson - Truman College Vaccination Site',
     'Western & 28th - Velasquez Institute Vaccination Site',
     'N Green St & W Lake St',
     'N Sheffield Ave & W Wellington Ave',
     'N Hampden Ct & W Diversey Ave',
     'N Carpenter St & W Lake St']




```python
# get the correct ids of exceptional stations in list not_changed
get_correct_id()
```

    W Armitage Ave & N Sheffield Ave :  1436495105198659242
    
    Malcolm X College Vaccination Site :  631
    
    W Washington Blvd & N Peoria St :  1436495109493626544
    
    W Oakdale Ave & N Broadway :  1436495100903691938
    
    N Paulina St & Lincoln Ave :  1436495122378528446
    
    Broadway & Wilson - Truman College Vaccination Site :  293
    
    Western & 28th - Velasquez Institute Vaccination Site :  446
    
    N Green St & W Lake St :  1436495109493626546
    
    N Sheffield Ave & W Wellington Ave :  1436495118083561146
    
    N Carpenter St & W Lake St :  1436495105198659246
    
    These stations below cannot be found in the official stations information dataset:





    ['Base - 2132 W Hubbard Warehouse', 'N Hampden Ct & W Diversey Ave']



<h4 style="color:red;"> The stations 'Base - 2132 W Hubbard Warehouse' and 'N Hampden Ct & W Diversey Ave' cannot be found in the official station information dataset. Due to lack of information, I will drop these records. </h4>


```python
# drop records with start_station_name as 'Base - 2132 W Hubbard Warehouse'
bt_202102.drop(bt_202102[bt_202102['start_station_name'] == 'Base - 2132 W Hubbard Warehouse'].index, inplace=True)

# drop records with end_station_name as 'Base - 2132 W Hubbard Warehouse'
bt_202102.drop(bt_202102[bt_202102['end_station_name'] == 'Base - 2132 W Hubbard Warehouse'].index, inplace=True)

# drop records with start_station_name as 'N Hampden Ct & W Diversey Ave'
bt_202102.drop(bt_202102[bt_202102['start_station_name'] == 'N Hampden Ct & W Diversey Ave'].index, inplace=True)

# drop records with end_station_name as 'N Hampden Ct & W Diversey Ave'
bt_202102.drop(bt_202102[bt_202102['end_station_name'] == 'N Hampden Ct & W Diversey Ave'].index, inplace=True)
```

<h4 style="color:blue;"> For the other 10 stations, I will manually update the ids in bt_202102 </h4>


```python
# update station's id with name of 'Malcolm X College Vaccination Site'
filt_a1 = (bt_202102['start_station_name'] == 'Malcolm X College Vaccination Site')
bt_202102.loc[filt_a1, 'start_station_id'] = 631

filt_a2 = (bt_202102['end_station_name'] == 'Malcolm X College Vaccination Site')
bt_202102.loc[filt_a2, 'end_station_id'] = 631
```


```python
# update station's id with name of 'N Paulina St & Lincoln Ave'
filt_b1 = (bt_202102['start_station_name'] == 'N Paulina St & Lincoln Ave')
bt_202102.loc[filt_b1, 'start_station_id'] = 1436495122378528446

filt_b2 = (bt_202102['end_station_name'] == 'N Paulina St & Lincoln Ave')
bt_202102.loc[filt_b2, 'end_station_id'] = 1436495122378528446
```


```python
# update station's id with name of 'W Oakdale Ave & N Broadway'
filt_c1 = (bt_202102['start_station_name'] == 'W Oakdale Ave & N Broadway')
bt_202102.loc[filt_c1, 'start_station_id'] = 1436495100903691938

filt_c2 = (bt_202102['end_station_name'] == 'W Oakdale Ave & N Broadway')
bt_202102.loc[filt_c2, 'end_station_id'] = 1436495100903691938
```


```python
# update station's id with name of 'W Washington Blvd & N Peoria St'
filt_d1 = (bt_202102['start_station_name'] == 'W Washington Blvd & N Peoria St')
bt_202102.loc[filt_d1, 'start_station_id'] = 1436495109493626544

filt_d2 = (bt_202102['end_station_name'] == 'W Washington Blvd & N Peoria St')
bt_202102.loc[filt_d2, 'end_station_id'] = 1436495109493626544
```


```python
# update station's id with name of 'W Armitage Ave & N Sheffield Ave'
filt_e1 = (bt_202102['start_station_name'] == 'W Armitage Ave & N Sheffield Ave')
bt_202102.loc[filt_e1, 'start_station_id'] = 1436495105198659242

filt_e2 = (bt_202102['end_station_name'] == 'W Armitage Ave & N Sheffield Ave')
bt_202102.loc[filt_e2, 'end_station_id'] = 1436495105198659242
```


```python
# update station's id with name of 'Broadway & Wilson - Truman College Vaccination Site'
filt_f1 = (bt_202102['start_station_name'] == 'Broadway & Wilson - Truman College Vaccination Site')
bt_202102.loc[filt_f1, 'start_station_id'] = 293

filt_f2 = (bt_202102['end_station_name'] == 'Broadway & Wilson - Truman College Vaccination Site')
bt_202102.loc[filt_f2, 'end_station_id'] = 293
```


```python
# update station's id with name of 'N Carpenter St & W Lake St'
filt_g1 = (bt_202102['end_station_name'] == 'N Carpenter St & W Lake St')
bt_202102.loc[filt_g1, 'end_station_id'] = 1436495105198659246
```


```python
# update station's id with name of 'Western & 28th - Velasquez Institute Vaccination Site'
filt_h1 = (bt_202102['end_station_name'] == 'Western & 28th - Velasquez Institute Vaccination Site')
bt_202102.loc[filt_h1, 'end_station_id'] = 446
```


```python
# update station's id with name of 'N Sheffield Ave & W Wellington Ave'
filt_i1 = (bt_202102['end_station_name'] == 'N Sheffield Ave & W Wellington Ave')
bt_202102.loc[filt_i1, 'end_station_id'] = 1436495118083561146
```


```python
# update station's id with name of 'N Green St & W Lake St'
filt_j1 = (bt_202102['end_station_name'] == 'N Green St & W Lake St')
bt_202102.loc[filt_j1, 'end_station_id'] = 1436495109493626546
```

<h4 style="color:green;"> (2-12) dataset: bike trips of March 2021 </h4> 


```python
bt_202103.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ride_id</th>
      <th>rideable_type</th>
      <th>started_at</th>
      <th>ended_at</th>
      <th>start_station_name</th>
      <th>start_station_id</th>
      <th>end_station_name</th>
      <th>end_station_id</th>
      <th>start_lat</th>
      <th>start_lng</th>
      <th>end_lat</th>
      <th>end_lng</th>
      <th>member_casual</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>CFA86D4455AA1030</td>
      <td>classic_bike</td>
      <td>2021-03-16 08:32:30</td>
      <td>2021-03-16 08:36:34</td>
      <td>Humboldt Blvd &amp; Armitage Ave</td>
      <td>15651</td>
      <td>Stave St &amp; Armitage Ave</td>
      <td>13266</td>
      <td>41.917513</td>
      <td>-87.701809</td>
      <td>41.917741</td>
      <td>-87.691392</td>
      <td>casual</td>
    </tr>
    <tr>
      <th>1</th>
      <td>30D9DC61227D1AF3</td>
      <td>classic_bike</td>
      <td>2021-03-28 01:26:28</td>
      <td>2021-03-28 01:36:55</td>
      <td>Humboldt Blvd &amp; Armitage Ave</td>
      <td>15651</td>
      <td>Central Park Ave &amp; Bloomingdale Ave</td>
      <td>18017</td>
      <td>41.917513</td>
      <td>-87.701809</td>
      <td>41.914166</td>
      <td>-87.716755</td>
      <td>casual</td>
    </tr>
    <tr>
      <th>2</th>
      <td>846D87A15682A284</td>
      <td>classic_bike</td>
      <td>2021-03-11 21:17:29</td>
      <td>2021-03-11 21:33:53</td>
      <td>Shields Ave &amp; 28th Pl</td>
      <td>15443</td>
      <td>Halsted St &amp; 35th St</td>
      <td>TA1308000043</td>
      <td>41.842733</td>
      <td>-87.635491</td>
      <td>41.830661</td>
      <td>-87.647172</td>
      <td>casual</td>
    </tr>
    <tr>
      <th>3</th>
      <td>994D05AA75A168F2</td>
      <td>classic_bike</td>
      <td>2021-03-11 13:26:42</td>
      <td>2021-03-11 13:55:41</td>
      <td>Winthrop Ave &amp; Lawrence Ave</td>
      <td>TA1308000021</td>
      <td>Broadway &amp; Sheridan Rd</td>
      <td>13323</td>
      <td>41.968812</td>
      <td>-87.657659</td>
      <td>41.952833</td>
      <td>-87.649993</td>
      <td>casual</td>
    </tr>
    <tr>
      <th>4</th>
      <td>DF7464FBE92D8308</td>
      <td>classic_bike</td>
      <td>2021-03-21 09:09:37</td>
      <td>2021-03-21 09:27:33</td>
      <td>Glenwood Ave &amp; Touhy Ave</td>
      <td>525</td>
      <td>Chicago Ave &amp; Sheridan Rd</td>
      <td>E008</td>
      <td>42.012701</td>
      <td>-87.666058</td>
      <td>42.050491</td>
      <td>-87.677821</td>
      <td>casual</td>
    </tr>
  </tbody>
</table>
</div>




```python
bt_202103.dtypes
```




    ride_id                object
    rideable_type          object
    started_at             object
    ended_at               object
    start_station_name     object
    start_station_id       object
    end_station_name       object
    end_station_id         object
    start_lat             float64
    start_lng             float64
    end_lat               float64
    end_lng               float64
    member_casual          object
    dtype: object




```python
bt_202103.isna().sum()
```




    ride_id                   0
    rideable_type             0
    started_at                0
    ended_at                  0
    start_station_name    14848
    start_station_id      14848
    end_station_name      16727
    end_station_id        16727
    start_lat                 0
    start_lng                 0
    end_lat                 167
    end_lng                 167
    member_casual             0
    dtype: int64




```python
# drop all NAN values in bt_202103
bt_202103.dropna(inplace=True)
```

<h4 style="color:red;"> After examinging the 'start_station_id' column and 'end_station_id' in this dataset, I found the same inconsistency issue between station ids and their corresponding names as before. </h4>
    
<h4 style="color:blue;"> Therefore, I will re-run the whole process of validating station names with corresponding ids as before using: </h4>

- <p style="color:blue;"> the official stations information dataset from Chicago Data Portral website;</p>
- <p style="color:blue;"> the dictionary "station_id" of all stations and ids existed in the previous 8 datasets;</p>
- <p style="color:blue;"> the function "correct_station_name_id" to either update ids or catch exceptions;</p>
- <p style="color:blue;"> the function "get_correct_id" to grab the correct ids for exceptions.</p>


```python
# reset the not_changed list to empty
not_changed = []

# update stations' ids in bt_202103 or catch stations that're not existed from previous 8 datasets
correct_station_name_id(bt_202103)
```

    These stations below are not existed in the previous 8 datasets:





    ['Chicago State University',
     'Western & 28th - Velasquez Institute Vaccination Site',
     'N Green St & W Lake St',
     'W Armitage Ave & N Sheffield Ave',
     'N Southport Ave & W Newport Ave',
     'Kedzie Ave & 110th St',
     'Damen Ave & Wabansia Ave',
     'N Sheffield Ave & W Wellington Ave',
     'N Hampden Ct & W Diversey Ave',
     'Malcolm X College Vaccination Site',
     'W Washington Blvd & N Peoria St',
     'W Oakdale Ave & N Broadway',
     'Base - 2132 W Hubbard Warehouse',
     'N Paulina St & Lincoln Ave',
     'N Carpenter St & W Lake St',
     'Broadway & Wilson - Truman College Vaccination Site',
     'Halsted & 63rd - Kennedy-King Vaccination Site',
     'N Damen Ave & W Wabansia St']




```python
# get the correct ids of exceptional stations in list not_changed
get_correct_id()
```

    Chicago State University :  737
    
    Western & 28th - Velasquez Institute Vaccination Site :  446
    
    N Green St & W Lake St :  1436495109493626546
    
    W Armitage Ave & N Sheffield Ave :  1436495105198659242
    
    N Southport Ave & W Newport Ave :  1436495115557663136
    
    Kedzie Ave & 110th St :  736
    
    Damen Ave & Wabansia Ave :  1521686986436309688
    
    N Sheffield Ave & W Wellington Ave :  1436495118083561146
    
    Malcolm X College Vaccination Site :  631
    
    W Washington Blvd & N Peoria St :  1436495109493626544
    
    W Oakdale Ave & N Broadway :  1436495100903691938
    
    N Paulina St & Lincoln Ave :  1436495122378528446
    
    N Carpenter St & W Lake St :  1436495105198659246
    
    Broadway & Wilson - Truman College Vaccination Site :  293
    
    Halsted & 63rd - Kennedy-King Vaccination Site :  388
    
    These stations below cannot be found in the official stations information dataset:





    ['N Hampden Ct & W Diversey Ave',
     'Base - 2132 W Hubbard Warehouse',
     'N Damen Ave & W Wabansia St']



<h4 style="color:red;"> The stations 'Base - 2132 W Hubbard Warehouse', 'N Hampden Ct & W Diversey Ave', and 'N Damen Ave & W Wabansia St' cannot be found in the official station information dataset. Due to lack of information, I will drop these records. </h4>


```python
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
```

<h4 style="color:blue;"> For the other 15 stations, I will manually update the ids in bt_202102 </h4>


```python
# update station's id with name of 'Broadway & Wilson - Truman College Vaccination Site'
filt_a1 = (bt_202103['start_station_name'] == 'Broadway & Wilson - Truman College Vaccination Site')
bt_202103.loc[filt_a1, 'start_station_id'] = 293

filt_a2 = (bt_202103['end_station_name'] == 'Broadway & Wilson - Truman College Vaccination Site')
bt_202103.loc[filt_a2, 'end_station_id'] = 293
```


```python
# update station's id with name of 'Damen Ave & Wabansia Ave'
filt_b1 = (bt_202103['start_station_name'] == 'Damen Ave & Wabansia Ave')
bt_202103.loc[filt_b1, 'start_station_id'] = 1521686986436309688

filt_b2 = (bt_202103['end_station_name'] == 'Damen Ave & Wabansia Ave')
bt_202103.loc[filt_b2, 'end_station_id'] = 1521686986436309688
```


```python
# update station's id with name of 'Western & 28th - Velasquez Institute Vaccination Site'
filt_c1 = (bt_202103['start_station_name'] == 'Western & 28th - Velasquez Institute Vaccination Site')
bt_202103.loc[filt_c1, 'start_station_id'] = 446

filt_c2 = (bt_202103['end_station_name'] == 'Western & 28th - Velasquez Institute Vaccination Site')
bt_202103.loc[filt_c2, 'end_station_id'] = 446
```


```python
# update station's id with name of 'Chicago State University'
filt_d1 = (bt_202103['start_station_name'] == 'Chicago State University')
bt_202103.loc[filt_d1, 'start_station_id'] = 737

filt_d2 = (bt_202103['end_station_name'] == 'Chicago State University')
bt_202103.loc[filt_d2, 'end_station_id'] = 737
```


```python
# update station's id with name of 'W Armitage Ave & N Sheffield Ave'
filt_e1 = (bt_202103['start_station_name'] == 'W Armitage Ave & N Sheffield Ave')
bt_202103.loc[filt_e1, 'start_station_id'] = 1436495105198659242

filt_e2 = (bt_202103['end_station_name'] == 'W Armitage Ave & N Sheffield Ave')
bt_202103.loc[filt_e2, 'end_station_id'] = 1436495105198659242
```


```python
# update station's id with name of 'W Washington Blvd & N Peoria St'
filt_f1 = (bt_202103['start_station_name'] == 'W Washington Blvd & N Peoria St')
bt_202103.loc[filt_f1, 'start_station_id'] = 1436495109493626544

filt_f2 = (bt_202103['end_station_name'] == 'W Washington Blvd & N Peoria St')
bt_202103.loc[filt_f2, 'end_station_id'] = 1436495109493626544
```


```python
# update station's id with name of 'N Paulina St & Lincoln Ave'
filt_g1 = (bt_202103['start_station_name'] == 'N Paulina St & Lincoln Ave')
bt_202103.loc[filt_g1, 'start_station_id'] = 1436495122378528446
              
filt_g2 = (bt_202103['end_station_name'] == 'N Paulina St & Lincoln Ave')
bt_202103.loc[filt_g2, 'end_station_id'] = 1436495122378528446
```


```python
# update station's id with name of 'Halsted & 63rd - Kennedy-King Vaccination Site'
filt_h1 = (bt_202103['start_station_name'] == 'Halsted & 63rd - Kennedy-King Vaccination Site')
bt_202103.loc[filt_h1, 'start_station_id'] = 388

filt_h2 = (bt_202103['end_station_name'] == 'Halsted & 63rd - Kennedy-King Vaccination Site')
bt_202103.loc[filt_h2, 'end_station_id'] = 388
```


```python
# update station's id with name of 'Kedzie Ave & 110th St'
filt_i1 = (bt_202103['start_station_name'] == 'Kedzie Ave & 110th St')
bt_202103.loc[filt_i1, 'start_station_id'] = 736

filt_i2 = (bt_202103['end_station_name'] == 'Kedzie Ave & 110th St')
bt_202103.loc[filt_i2, 'end_station_id'] = 736
```


```python
# update station's id with name of 'N Carpenter St & W Lake St'
filt_j1 = (bt_202103['start_station_name'] == 'N Carpenter St & W Lake St')
bt_202103.loc[filt_j1, 'start_station_id'] = 1436495105198659246

filt_j2 = (bt_202103['end_station_name'] == 'N Carpenter St & W Lake St')
bt_202103.loc[filt_j2, 'end_station_id'] = 1436495105198659246
```


```python
# update station's id with name of 'Malcolm X College Vaccination Site'
filt_k1 = (bt_202103['start_station_name'] == 'Malcolm X College Vaccination Site')
bt_202103.loc[filt_k1, 'start_station_id'] = 631

filt_k2 = (bt_202103['end_station_name'] == 'Malcolm X College Vaccination Site')
bt_202103.loc[filt_k2, 'end_station_id'] = 631
```


```python
# update station's id with name of 'N Sheffield Ave & W Wellington Ave'
filt_l1 = (bt_202103['start_station_name'] == 'N Sheffield Ave & W Wellington Ave')
bt_202103.loc[filt_l1, 'start_station_id'] = 1436495118083561146

filt_l2 = (bt_202103['end_station_name'] == 'N Sheffield Ave & W Wellington Ave')
bt_202103.loc[filt_l2, 'end_station_id'] = 1436495118083561146
```


```python
# update station's id with name of 'W Oakdale Ave & N Broadway'
filt_m1 = (bt_202103['start_station_name'] == 'W Oakdale Ave & N Broadway')
bt_202103.loc[filt_m1, 'start_station_id'] = 1436495100903691938

filt_m2 = (bt_202103['end_station_name'] == 'W Oakdale Ave & N Broadway')
bt_202103.loc[filt_m2, 'end_station_id'] = 1436495100903691938
```


```python
# update station's id with name of 'N Southport Ave & W Newport Ave'
filt_n1 = (bt_202103['start_station_name'] == 'N Southport Ave & W Newport Ave')
bt_202103.loc[filt_n1, 'start_station_id'] = 1436495115557663136

filt_n2 = (bt_202103['end_station_name'] == 'N Southport Ave & W Newport Ave')
bt_202103.loc[filt_n2, 'end_station_id'] = 1436495115557663136
```


```python
# update station's id with name of 'N Green St & W Lake St'
filt_o1 = (bt_202103['start_station_name'] == 'N Green St & W Lake St')
bt_202103.loc[filt_o1, 'start_station_id'] = 1436495109493626546

filt_o2 = (bt_202103['end_station_name'] == 'N Green St & W Lake St')
bt_202103.loc[filt_o2, 'end_station_id'] = 1436495109493626546
```

### 3. Save cleaned datasets


```python
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
```


```python

```
