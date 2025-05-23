import sqlite3

conn = sqlite3.connect('f1.db')
cur = conn.cursor()

# Habilita foreign keys no SQLite
cur.execute('PRAGMA foreign_keys = ON;')

# circuits
cur.execute('''
CREATE TABLE IF NOT EXISTS circuits (
    circuitId INTEGER PRIMARY KEY,
    circuitRef TEXT,
    name TEXT,
    location TEXT,
    country TEXT,
    lat REAL,
    lng REAL,
    alt REAL,
    url TEXT
);
''')

# constructors
cur.execute('''
CREATE TABLE IF NOT EXISTS constructors (
    constructorId INTEGER PRIMARY KEY,
    constructorRef TEXT,
    name TEXT,
    nationality TEXT,
    url TEXT
);
''')

# constructor_results
cur.execute('''
CREATE TABLE IF NOT EXISTS constructor_results (
    constructorResultsId INTEGER PRIMARY KEY,
    raceId INTEGER,
    constructorId INTEGER,
    points REAL,
    status TEXT,
    FOREIGN KEY(raceId) REFERENCES races(raceId),
    FOREIGN KEY(constructorId) REFERENCES constructors(constructorId)
);
''')

# constructor_standings
cur.execute('''
CREATE TABLE IF NOT EXISTS constructor_standings (
    constructorStandingsId INTEGER PRIMARY KEY,
    raceId INTEGER,
    constructorId INTEGER,
    points REAL,
    position INTEGER,
    positionText TEXT,
    wins INTEGER,
    FOREIGN KEY(raceId) REFERENCES races(raceId),
    FOREIGN KEY(constructorId) REFERENCES constructors(constructorId)
);
''')

# drivers
cur.execute('''
CREATE TABLE IF NOT EXISTS drivers (
    driverId INTEGER PRIMARY KEY,
    driverRef TEXT,
    number INTEGER,
    code TEXT,
    forename TEXT,
    surname TEXT,
    dob TEXT,
    nationality TEXT,
    url TEXT
);
''')

# driver_standings
cur.execute('''
CREATE TABLE IF NOT EXISTS driver_standings (
    driverStandingsId INTEGER PRIMARY KEY,
    raceId INTEGER,
    driverId INTEGER,
    points REAL,
    position INTEGER,
    positionText TEXT,
    wins INTEGER,
    FOREIGN KEY(raceId) REFERENCES races(raceId),
    FOREIGN KEY(driverId) REFERENCES drivers(driverId)
);
''')

# lap_times
cur.execute('''
CREATE TABLE IF NOT EXISTS lap_times (
    raceId INTEGER,
    driverId INTEGER,
    lap INTEGER,
    position INTEGER,
    time TEXT,
    milliseconds INTEGER,
    PRIMARY KEY(raceId, driverId, lap),
    FOREIGN KEY(raceId) REFERENCES races(raceId),
    FOREIGN KEY(driverId) REFERENCES drivers(driverId)
);
''')

# pit_stops
cur.execute('''
CREATE TABLE IF NOT EXISTS pit_stops (
    raceId INTEGER,
    driverId INTEGER,
    stop INTEGER,
    lap INTEGER,
    time TEXT,
    duration TEXT,
    milliseconds INTEGER,
    PRIMARY KEY(raceId, driverId, stop),
    FOREIGN KEY(raceId) REFERENCES races(raceId),
    FOREIGN KEY(driverId) REFERENCES drivers(driverId)
);
''')

# qualifying
cur.execute('''
CREATE TABLE IF NOT EXISTS qualifying (
    qualifyId INTEGER PRIMARY KEY,
    raceId INTEGER,
    driverId INTEGER,
    constructorId INTEGER,
    number INTEGER,
    position INTEGER,
    q1 TEXT,
    q2 TEXT,
    q3 TEXT,
    FOREIGN KEY(raceId) REFERENCES races(raceId),
    FOREIGN KEY(driverId) REFERENCES drivers(driverId),
    FOREIGN KEY(constructorId) REFERENCES constructors(constructorId)
);
''')

# races
cur.execute('''
CREATE TABLE IF NOT EXISTS races (
    raceId INTEGER PRIMARY KEY,
    year INTEGER,
    round INTEGER,
    circuitId INTEGER,
    name TEXT,
    date TEXT,
    time TEXT,
    url TEXT,
    fp1_date TEXT,
    fp1_time TEXT,
    fp2_date TEXT,
    fp2_time TEXT,
    fp3_date TEXT,
    fp3_time TEXT,
    quali_date TEXT,
    quali_time TEXT,
    sprint_date TEXT,
    sprint_time TEXT,
    FOREIGN KEY(circuitId) REFERENCES circuits(circuitId)
);
''')

# results
cur.execute('''
CREATE TABLE IF NOT EXISTS results (
    resultId INTEGER PRIMARY KEY,
    raceId INTEGER,
    driverId INTEGER,
    constructorId INTEGER,
    number INTEGER,
    grid INTEGER,
    position INTEGER,
    positionText TEXT,
    positionOrder INTEGER,
    points REAL,
    laps INTEGER,
    time TEXT,
    milliseconds INTEGER,
    fastestLap INTEGER,
    rank INTEGER,
    fastestLapTime TEXT,
    fastestLapSpeed TEXT,
    statusId INTEGER,
    FOREIGN KEY(raceId) REFERENCES races(raceId),
    FOREIGN KEY(driverId) REFERENCES drivers(driverId),
    FOREIGN KEY(constructorId) REFERENCES constructors(constructorId),
    FOREIGN KEY(statusId) REFERENCES status(statusId)
);
''')

# seasons
cur.execute('''
CREATE TABLE IF NOT EXISTS seasons (
    year INTEGER PRIMARY KEY,
    url TEXT
);
''')

# sprint_results
cur.execute('''
CREATE TABLE IF NOT EXISTS sprint_results (
    resultId INTEGER PRIMARY KEY,
    raceId INTEGER,
    driverId INTEGER,
    constructorId INTEGER,
    number INTEGER,
    grid INTEGER,
    position INTEGER,
    positionText TEXT,
    positionOrder INTEGER,
    points REAL,
    laps INTEGER,
    time TEXT,
    milliseconds INTEGER,
    fastestLap INTEGER,
    fastestLapTime TEXT,
    statusId INTEGER,
    FOREIGN KEY(raceId) REFERENCES races(raceId),
    FOREIGN KEY(driverId) REFERENCES drivers(driverId),
    FOREIGN KEY(constructorId) REFERENCES constructors(constructorId),
    FOREIGN KEY(statusId) REFERENCES status(statusId)
);
''')

# status
cur.execute('''
CREATE TABLE IF NOT EXISTS status (
    statusId INTEGER PRIMARY KEY,
    status TEXT
);
''')

conn.commit()
conn.close()
print("Tabelas criadas com sucesso!")
