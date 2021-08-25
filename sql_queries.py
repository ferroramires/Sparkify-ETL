# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS song_play"
user_table_drop = "DROP TABLE IF EXISTS user_table"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time_table"

# CREATE TABLES
# FACT TABLE
songplay_table_create = ("""CREATE TABLE IF NOT EXISTS song_play (
    songplay_id VARCHAR PRIMARY KEY, 
    start_time BIGINT,
    user_id VARCHAR, 
    level VARCHAR,
    song_id VARCHAR,
    artist_id VARCHAR,
    session_id VARCHAR,
    location VARCHAR,
    user_agent VARCHAR 
    );
""")

# DIMENSION TABLES
# MALES = 0, FEMALES = 1
user_table_create = ("""CREATE TABLE IF NOT EXISTS user_table (
    user_id VARCHAR PRIMARY KEY,
    first_name VARCHAR,
    last_name VARCHAR,
    gender VARCHAR,
    level VARCHAR
    );
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (
    song_id VARCHAR PRIMARY KEY,
    title VARCHAR,
    artist_id VARCHAR,
    year INT,
    duration INT
    );
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (
    artist_id VARCHAR PRIMARY KEY,
    name VARCHAR,
    location VARCHAR,
    latitude REAL,
    longitude REAL
    );
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time_table (
    start_time timestamp PRIMARY KEY,
    hour INT,
    day INT,
    week INT,
    month INT,
    year INT,
    weekday INT
    );
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO song_play(songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
    VALUES
    (%s, %s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""INSERT INTO user_table(user_id, first_name, last_name, gender, level)
    VALUES
    (%s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING
""")

song_table_insert = ("""INSERT INTO songs(song_id, title, artist_id, year, duration)
    VALUES
    (%s, %s, %s, %s, %s)
""")

artist_table_insert = ("""INSERT INTO artists(artist_id, name, location, latitude, longitude)
    VALUES
    (%s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING;
""")


time_table_insert = ("""INSERT INTO time_table(start_time, hour, day, week, month, year, weekday)
    VALUES
    (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING;
""")

# FIND SONGS

song_select = ("""SELECT s.song_id, a.artist_id
FROM songs AS s
JOIN artists as a
ON s.artist_id=a.artist_id;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]