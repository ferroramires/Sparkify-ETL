
# Data Modeling with Postgres - DE-Project 1

### Introduction
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis, and bring you on the project. My role is to create a database schema and ETL pipeline for this analysis. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.

### Project Description

In this project, I've created an ETL pipeline for Sparkify's song a log data sets. 

The main file is `etl.py`, where all the ETL process is done. But for it to work, I created the `create_tables.py` file to create a basic star schema for the data sets.
And all the queries are in the `sql_queries.py` file. 
For test purposed we have the `test.ipynb`, so that we can check if the tables are being written on.

In summary, for it to work, you need to first run `create_tables.py` to create the database and connect to it, and then the 'etl.py'. And to further verify if everything is ok, we run the 'test.ipynb' file.

### Project files:

1.  `test.ipynb`  displays the first few rows of each table to let you check your database.
2.  `create_tables.py`  drops and creates your tables. 
4.  `etl.py`  reads and processes files from  `song_data`  and  `log_data`  and loads them into your tables.
5.  `sql_queries.py`  contains all your sql queries.

# Schema for Song Play Analysis

In this project we are using a star schema for the database. With 1 fact table and 4 dimension tables.

#### Fact Table

1.  **songplays**  - records in log data associated with song plays i.e. records with page  `NextSong`
    -   _songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent_

#### Dimension Tables

2.  **users**  - users in the app
    -   _user_id, first_name, last_name, gender, level_
3.  **songs**  - songs in music database
    -   _song_id, title, artist_id, year, duration_
4.  **artists**  - artists in music database
    -   _artist_id, name, location, latitude, longitude_
5.  **time**  - timestamps of records in  **songplays**  broken down into specific units
    -   _start_time, hour, day, week, month, year, weekday_
