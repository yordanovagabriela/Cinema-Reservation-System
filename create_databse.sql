-- PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS movies;

CREATE TABLE IF NOT EXISTS movies (
    movie_id INTEGER PRIMARY KEY,
    name TEXT,
    rating NUMERIC DEFAULT 0
        );

INSERT INTO movies VALUES(null, 'The Hunger Games: Catching Fire', 7.9);
INSERT INTO movies VALUES(null, 'Wreck-It Ralph', 7.8);
INSERT INTO movies VALUES(null, 'Her', 8.3);

DROP TABLE IF EXISTS projections;

CREATE TABLE IF NOT EXISTS projections (
    projection_id INTEGER PRIMARY KEY,
    movie_id INTEGER,
    type TEXT,
    date_projection DATE,
    time TEXT,
    FOREIGN KEY(movie_id) REFERENCES movies(movie_id)
        );

INSERT INTO projections VALUES(null, 1, '3D', '2014-04-01', '19:10');
INSERT INTO projections VALUES(null, 1, '2D', '2014-04-01', '19:00');
INSERT INTO projections VALUES(null, 1, '4DX', '2014-04-02', '21:00');
INSERT INTO projections VALUES(null, 3, '2D', '2014-04-05', '20:20');
INSERT INTO projections VALUES(null, 2, '3D', '2014-04-02', '22:00');
INSERT INTO projections VALUES(null, 2, '2D', '2014-04-02', '19:30');

DROP TABLE IF EXISTS reservations;

CREATE TABLE IF NOT EXISTS reservations (
    reservation_id INTEGER PRIMARY KEY,
    username TEXT,
    projection_id INTEGER,
    row INTEGER,
    col INTEGER,
    FOREIGN KEY(projection_id) REFERENCES projections(projection_id)
    );

INSERT INTO reservations VALUES(null, 'RadoRado', 1, 2, 1);
INSERT INTO reservations VALUES(null, 'RadoRado', 1, 3, 5);
INSERT INTO reservations VALUES(null, 'RadoRado', 1, 7, 8);
INSERT INTO reservations VALUES(null, 'Ivo', 3, 1,1);
INSERT INTO reservations VALUES(null, 'Ivo', 3, 1,2);
INSERT INTO reservations VALUES(null, 'Mysterious', 5, 2, 3);
INSERT INTO reservations VALUES(null, 'Mysterious', 5, 2, 4);

DROP TABLE IF EXISTS reserved_seats;

CREATE TABLE IF NOT EXISTS reserved_seats (
	projection_id INTEGER DEFAULT 100,
	seats INTEGER,
	FOREIGN KEY(projection_id) REFERENCES projections(projection_id)
    );

INSERT INTO reserved_seats VALUES(1, 3);
INSERT INTO reserved_seats VALUES(2, 0);
INSERT INTO reserved_seats VALUES(3, 2);
INSERT INTO reserved_seats VALUES(4, 0);
INSERT INTO reserved_seats VALUES(5, 2);
INSERT INTO reserved_seats VALUES(6, 0);


-- import sqlite3
-- import sys

-- db_name = sys.argv[1]
-- sql_file = sys.argv[2]

-- conn = sqlite3.coonect(db_name)
-- with open(sql_file, 'r') as f:
--     conn.exectutescript(f.read())
--     conn.commit()

-- settings.py
-- DB_NAME = "nn.db"
-- SQL_NAME = 'nn.sql'
