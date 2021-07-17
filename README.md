<h2 align='center'> Cyclistic: a bike-share program </h2>
<h6 aligh='left'> * This is a case study for the Google Data Analytics Certificate. (For a complete instruction, check __[here](Case-Study-1_instructions.pdf)__ </h6>

### Introduction:

In this case study, you will perform many real-world tasks of a junior data analyst. In order to answer the key business questions, you will follow the steps of the data analysis process:
- ***[Ask](#step-1-ask)***
- ***[Prepare](#step-2-prepare)***
- ***[Process](#step-3-process)***
- ***[Analyze](#step-4-analyze)***
- ***[Share](#step-5-share)***
- ***[Act](#step-6-act)***

### Scenario:
    
You are a junior data analyst working in the marketing analyst team at Cyclistic, a bike-share company in Chicago. The director of marketing believes the company's future success depends on maximizing the number of annual memberships. Therefore, your team wants to understand how casual riders and annual members use Cyclistic bikes differently. 

From these insights, your team will design a new marketing strategy to convert casual riders into annual members. But first, Cyclistic executives must approve your recommendations, so they must be backed up with compelling data insights and professional data visualizations.

### Characters and teams:

- **Cyclistic:**
    A bike-share program that features more than 5,800 bicycles and 600 docking stations. Cyclistic sets itself apart by also offering reclining bikes, hand tricycles, and cargo bikes, making bike-share more inclusive to people  with disabilities and riders who can't use a standard two-wheeled bike. The majority of riders opt for traditional bikes; about 8% of riders use the assistive options. Cyclistic users are more likely to rider for leisure, but about 30% use them to commute to work each day.

- **Lily Moreno:**
    The director of marketing and your manager. Moreno is reponsible for the development of campaigns and initiatives to promote the bike-share program. These may include mail, social media, and other channels.

- **Cyclistic marketing analytics team:**
    A team of data analysts who are responsible for collecting, analyzing, and reporting data that helps guide Cyclistic marketing strategy. You joined this team six months ago and have been busy learning about Cyclistic's mission and business goals -- as well as how you, as a junior data analyst, can help Cyclistic achieve them.

- **Cyclistic executive team:**
    The notoriously detail-oriented executive team will decide whether to approve the recommended marketing program.

## Step 1: Ask

#### Business task:
> Analyze Cyclistic's historical bike trip data from April 2020 to March 2021 to identify trends on how members and casual riders use Cyclistic bikes differently; Then, generate 3 recommendations based on this analysis for the Cyclistic's marketing team to design marketing strategies for converting casual riders into members.

#### Key stakeholders:

- Lily Moreno -- the director of Cyclistic marketing team
- Cyclistic marketing analytics team
- Cyclistic executive team

## Step 2: Prepare

#### The data I used in this case study can be downloaded from __[here.](https://divvy-tripdata.s3.amazonaws.com/index.html)__

- **Note:** the datasets have a different name because Cyclistic is a fictional company. For the purpose of this case study, the datasets are appropriate and will enable to answer the business questions. 

#### The data contains 12 datasets in total:

Each dataset contains bike trip data of a month from April 2020 to March 2021, and it is consisted of 13 columns described as below:

|Column|This column measures|
| :---: | :---: |
| *ride_id* | unique id of each bike ride initiated |
| *rideable_type* | 3 types of bikes used by Cycslistic |
| *started_at* | start date and time of each bike ride |
| *ended_at* | end date and time of each bike ride |
| *start_station_name* | bike station name where each bike ride starts |
| *start_station_id* | bike station id where each bike ride starts |
| *end_station_name* | bike station name where each bike ride ends |
| *end_station_id* | bike station id where each bike ride ends |
| *start_lat* | latitude of bike station where each bike ride starts |
| *start_lng* | longitude of biek station where each bike ride starts |
| *end_lat* | latitude of bike station where each bike ride ends |
| *end_lng* | longitude of bike station where each bike ride ends |
| *member_casual* | whether a bike rider is a member of Cyclistic program or not |

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
> From April 2020 to March 2021, 41% of Cyclistic bike users were casual riders. Therefore, it is essential for Cyclistic to design marketing strategies targeted at maximally converting casual riders into annual members.

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
