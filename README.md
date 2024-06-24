# Gym Buddy Data Engineering


## Description

This is GymBuddy System! <br />
This project is to showcase my understanding of Data Engineering concepts.
<br />
The final goal of this project is to do analysis on the data, and to recommend a gym member for each gym members (hence the name GymBuddy) to accompany them to the gym.

## Concepts

### Front end development (HTML, CSS, JS)

* In this project, I have tried to developed a web application that takes input from the user and allows them to enter details such as 
Age, Gender, Height, Weight, Preferred Time etc, Gym Goals etc.. <br />
* Then the entered details are viewed for review before final submission. 
Once the submission is done, the details will added to the database. <br />
* The database used in this project is sqllite3 as it comes pre installed package in python.
I used Flask framework for deployment.
* Once the data is finally submitted, there is an option to download the data from the table as an excel so that analysis can be performed.

____

### Google Cloud Console

#### Features used in Google Cloud Console :
  - Creating a project
  - Compute Engine - To create a Virtual Machine Instance to host Mage
  - Cloud Storage - To store the Dataset (Flat files - ex. csv, xlsx files)
  - BigQuery - To do Analysis on the data
  - Looker Studio - To do Data visualization on the data

### MAGE (Python)
  
* Mage is an open-source data pipeline tool for transforming and integrating data. I used Mage in this project for building the data pipeline for ETL processes. 
* I loaded the raw data (flat file) from Google Cloud Storage and created [Load Data file](https://github.com/iam-venkat03/Gym-buddy-data-engineering/blob/main/Mage/data_loaders/playful_breeze.py) file.
* Once the data is laoded, I transformed the code by doing basic transformation columns and converting the flat file into database schema. Created ID columns in dimension table to reference to the fact table. ([Transform Data file](https://github.com/iam-venkat03/Gym-buddy-data-engineering/blob/main/Mage/transformers/datatransform_gymbuddy.py))
* After the data is transformed, the file is exported to Google Big Query where Data Analysis is done. ([Data Export file](https://github.com/iam-venkat03/Gym-buddy-data-engineering/blob/main/Mage/data_exporters/bigqueryload_gymbuddy.py))
* The reason why I chose Mage is new age tool where features such as connectivity is Google Big Query, AWS etc. are already in place.
* As much as its easy to use Mage, trying to run it in the Google VM Instance was bit difficult as it requires some high RAM level to run. I often faced the application got stuck because of lack of machine capacity.

### Google Big Query
  - ([Data Export file](https://github.com/iam-venkat03/Gym-buddy-data-engineering/blob/main/Mage/data_exporters/bigqueryload_gymbuddy.py)) would have created a dataset in Google BigQuery. Using the dataset, you can develop a series of SQL queries to analyse the data.
  - I did some basic querying to find average, total, count etc.. as part of analysis. Refer [SQL Queries](https://github.com/iam-venkat03/Gym-buddy-data-engineering/blob/main/Query_testing.sql) for more detail.
  - I also created a new table with column I need for Data Visualization using SQL query.

### Looker Studio

* In Looker Studio, we can connect to Big Query to fetch the table we needed.
* Using Looker, I created a report that would give Gender based Analysis, Preferred Time based Analysis etc.. You can view the report Here : [GymBuddy Report](https://lookerstudio.google.com/reporting/27e74745-1f7c-4264-9ab5-598c5779e042)
