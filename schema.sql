-- create tables for GPSStore
-- Users: a movement subject
-- Tracks: GPS Tracks
-- TrackPoints: GPS Points

CREATE TABLE Users (
    userid INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    birthdate TEXT,
    gender TEXT,
    area TEXT
);

CREATE TABLE Tracks (
    trkid INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    userid INTEGER NOT NULL,
    rtype INTEGER NOT NULL,
    timestamp_start TEXT NOT NULL,
    timestamp_end TEXT NOT NULL,
    timespan_sec REAL NOT NULL,
    length_m REAL NOT NULL,
    avg_speed_km REAL NOT NULL,
    avg_pacer REAL,
    calory REAL,
    avg_cadence INTEGER,
    avg_heartrate INTEGER,
    max_heartrate INTEGER,
    FOREIGN KEY (userid)
    REFERENCES Users (userid) ON DELETE CASCADE ON UPDATE CASCADE,
    UNIQUE (trkid, userid)
);

SELECT AddGeometryColumn('Tracks', 'geom', 4326, 'LINESTRING', "XY", 1);
SELECT CreateSpatialIndex('Tracks', 'geom');

CREATE TABLE TrackPoints (
    trkpt_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    trkid INTEGER NOT NULL,
    timestamp TEXT NOT NULL,
    elevation REAL NOT NULL,
    speed REAL,
    cadence INTEGER,
    heartrate INTEGER,
    FOREIGN KEY (trkid)
    REFERENCES Tracks (trkid) ON DELETE CASCADE on UPDATE CASCADE,
    UNIQUE (trkpt_id, trkid)
);

SELECT AddGeometryColumn('TrackPoints', 'geom', 4326, 'POINT', "XY", 1);
SELECT CreateSpatialIndex('TrackPoints', 'geom');

