# Gym Buddy Data Engineering


## Description

Welcome to the GymBuddy System! <br> This project is designed to showcase my understanding of Data Engineering concepts. <br>
The ultimate goal is to analyze the data and recommend a gym buddy (hence the name GymBuddy) for each gym member based on their preferences and goals.

## Concepts

### Front end development (HTML, CSS, JS)
 
* In this project, I developed a web application that allows users to input details such as age, gender, height, weight, preferred gym time, and gym goals.
* The entered details can be reviewed before final submission.
* Once submitted, the details are added to the database.
* The database used is SQLite3, which comes pre-installed with Python.
* Flask was used for deployment.
* Once the data is finally submitted, there is an option to download the data from the table as an excel so that analysis can be performed.
____

### Google Cloud Console

#### Features used in Google Cloud Console :
  - Creating a project
  - Compute Engine - To create a Virtual Machine Instance to host Mage
  - Cloud Storage - To store the Dataset (Flat files - ex. csv, xlsx files)
  - BigQuery - To do Analysis on the data
  - Looker Studio - To do Data visualization on the data

### Mage (Python)

Mage.ai is an open-source data pipeline tool used for transforming and integrating data. In this project, Mage was used to build the ETL pipeline:

* Loaded raw data from Google Cloud Storage. [Load Data file](https://github.com/iam-venkat03/Gym-buddy-data-engineering/blob/main/Mage/data_loaders/playful_breeze.py)
* Performed basic data transformations and converted flat files into a database schema. ([Transform Data file](https://github.com/iam-venkat03/Gym-buddy-data-engineering/blob/main/Mage/transformers/datatransform_gymbuddy.py))
* Created ID columns in the dimension table to reference the fact table.
* Exported the transformed data to Google BigQuery for analysis. ([Data Export file](https://github.com/iam-venkat03/Gym-buddy-data-engineering/blob/main/Mage/data_exporters/bigqueryload_gymbuddy.py))
  
Mage was chosen for its ease of use and built-in connectivity to Google BigQuery and AWS. However, running Mage on Google VM Instance posed challenges due to high RAM requirements.

### Google Big Query
  - ([Data Export file](https://github.com/iam-venkat03/Gym-buddy-data-engineering/blob/main/Mage/data_exporters/bigqueryload_gymbuddy.py)) would have created a dataset in Google BigQuery. Using the dataset, developed a series of SQL queries to analyse the data.
  - Basic queries to find averages, totals, counts, etc., were executed as part of analysis. Refer [SQL Queries](https://github.com/iam-venkat03/Gym-buddy-data-engineering/blob/main/Query_testing.sql) for more detail.
  - A new table was also created for data visualization using SQL queries.

### Looker Studio

* Looker Studio was used to connect to BigQuery and fetch the required tables.
* A report was created in Looker Studio for gender-based analysis, preferred time analysis, etc. You can view the report here:  [GymBuddy Report](https://lookerstudio.google.com/reporting/27e74745-1f7c-4264-9ab5-598c5779e042)

###  Reference Video :
<a href="https://www.youtube.com/watch?v=WpQECq5Hx9g&list=PL84EAfzsRsnUzXcAbQsrrm6xia2pSRiO9"
target="_blank"><img src="https://t3.ftcdn.net/jpg/04/74/05/94/360_F_474059464_qldYuzxaUWEwNTtYBJ44VN89ARuFktHW.jpg" 
alt="Reference Youtube Video Link" width="240" height="180" border="10" /></a>


## THANKS!
