<h2 align='center'> Cyclistic: a bike-share program </h2>
###### This is a case study for the Google Data Analytics Certificate. For complete instructions about this case study, check __[here](instructions.ipynb)__

### In this case study, I will follow the steps of the Data Analysis Process:
1. ***[Ask](#step-1-ask)***
2. ***[Prepare](#step-2-prepare)***
3. ***[Process](#step-3-process)***
4. ***[Analyze](#step-4-analyze)***
5. ***[Share](#step-5-share)***
6. ***[Act](#step-6-act)***

## Step 1: Ask

#### The business task:
I analyze Cyclistic's historical bike trip data from April 2020 to March 2021 to identify trends on how members and casual riders use Cyclistic bikes differently; Then, I generate 3 recommendations based on this analysis for the Cyclistic's marketing team to design marketing strategies for converting casual riders into members.

## Step 2: Prepare

***Note:*** For more details of this part, check this Notebook __[here](p1_data_prepare_process.ipynb)__.

#### The data I used in this case study can be downloaded from __[here.](https://divvy-tripdata.s3.amazonaws.com/index.html)__

- **Note:** the datasets have a different name because Cyclistic is a fictional company. For the purpose of this case study, the datasets are appropriate and will enable to answer the business questions. 

#### The data contains 12 datasets in total:
Each dataset contains bike trip data of a month from April 2020 to March 2021, and it is consisted of 13 columns.

#### After examining the data, I believe the data meets the ROCCC standard:
The data is reliable, original, comprehensive, current, and cited:
- it has been made available under this __[license](https://www.divvybikes.com/data-license-agreement)__ by Motivate International Inc with permissions from the City of Chicago's Divvy bicycle sharing service; 
- it is owned by the City of Chicago; 
- it is updated by Motivate International Inc on a monthly basis.

#### The potential problems with the data:
The data is provided "as-is" by Motivated International Inc. Therefore, there are certain amount of invalid data in the data. As a result, the data requires some cleaning and transformation before it can be applied for further analysis.

## Step 3: Process

***Note:*** For more details of this part, check this Notebook __[here](p1_data_prepare_process.ipynb)__.

#### These original datasets are downloaded and stored:
- on Google Drive and locally on my computer

#### For each dataset, I perform these data cleaning and transformations:
- check the uniqueness of *ride_id*
- drop any null values in all columns
- check the data types of each column, and convert to the correct type if necessary
- check the consistency between *start_station_name* and *start_station_id*
- check the consistency between *end_station_name* and *end_station_id*
- drop irrelevant columns: *start_lat*, *start_lng*, *end_lat*, *end_lng*

## Step 4: Analyze

***Note:*** For more details of this part, check this Notebook __[here](p2_data_analysis_visualization.ipynb)__

#### After cleaning the original datasets, I store them on:
- Google Drive
- locally on my computer

#### Then, I concatenated these datasets into one dataset named *btrips*, and divide this dataframe into two sub-dataframes:
- ***m_btrips*** for members
- ***c_btrips*** for casual riders

#### Next, I perform these analysis using these two sub-dataframes:
- calculate the amount of members vs. casual riders have used Cyclistic bikes
- calculate the amount of members vs. casual riders used Cyclistic bikes by months
- discover the type of bikes members vs. casual riders perfer
- calculate the length of bike rides members vs. casual riders use
- discover which day in a week that members vs. casual riders start their bike rides
- calculate the average length of bike rides members vs. casual riders use based on days in a week
- discover the top 5 bike stations members vs. casual riders visited most frequently to start their bike rides

#### Finally, I identify these trends of how members and casual riders use Cyclistic bikes differently:
- 41% Cyclistic users are casual riders.
- The amount of Cyclistic bikes used by members and casual riders has been declining between August to January.
- 82% casual riders have used docked bikes.
- For bike rides within 12 hours, the amount of casual riders are more than members; For bike rides more than 12 hours, the amount of members are significantly more than casual riders.
- On weekdays, the amount of members use Cyclistic bikes are significantly more than casual riders, however, the amount gap is less wide on weekends.
- The average length of bike rides of casual riders is less than 20 minutes; Meanwhile, the average length of bike rides of members is over 40 minutes.
- The top 5 bike stations casual riders start their bike rides are different from the top 5 stations members usually start their bike rides.

## Step 5: Share

***Note:*** For more details of this part, check this PowerPoint __[here](p3_presentation.pdf)__

#### Based on my analysis, I summarize that annaul members and casual riders use Cyclistic bikes differently via:
- seasons
- bike types
- bike ride lengths
- weekdays vs. weekends
- bike stations

## Step 6: Act

***Note:*** For more details of this part, check this PowerPoint __[here](p3_presentation.pdf)__

#### The final conclusion based on my analysis:
From April 2020 to March 2021, 41% of Cyclistic bike users were casual riders. Therefore, it is essential for Cyclistic to design marketing strategies targeted at maximally converting casual riders into annual members.

#### Therefore, I generate 3 recommendations for the Marketing Team:
1. Offer fare discounts to casual riders using Cyclistic bikes shorter than 12 hours for each ride and/or on weekends.
1. Design promotions specifically targeted at casual riders between February to July.
1. Launch digital and non-digital ads at the 5 bike stations that casual riders used most, and put more docked bikes at these stations.

#### Next steps to take:
- Develop a deeper research on why and why not casual riders would buy Cyclistic annual memberships
- Generate a comprehensive analysis on how to use digital media to influence casual riders to become members

#### Additional data I could use to expand my findings:
- Cyclistic's historical bike fare data
- data from other peer competitors in the Chicago area; data should includes information such as their bike fares charged to members versus non-members and the amount of members purchased their annual memberships.
