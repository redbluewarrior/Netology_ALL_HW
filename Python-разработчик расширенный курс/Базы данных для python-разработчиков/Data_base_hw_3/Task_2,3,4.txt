-- Task 2

--1
SELECT name, MAX(duration) FROM tracks
GROUP BY name
ORDER BY MAX(duration) DESC
LIMIT 1;

--2
SELECT name FROM tracks
WHERE duration >= 210;

--3
SELECT name FROM collections
WHERE extract(year from date) BETWEEN 2018 and 2020;

--4
SELECT name FROM musicians
WHERE name NOT LIKE '% %';

--5
SELECT name FROM tracks
WHERE STRING_TO_ARRAY(LOWER(name), ' ') && array['my', 'мой']


--Task 3

--1
SELECT g.name, COUNT(*) FROM genre_and_musician gm
JOIN musical_genre g ON g.id = gm.genreid
GROUP BY genreid, name;

--2
SELECT COUNT(*) FROM tracks t
JOIN albums a ON t.albumid = a.id 
WHERE EXTRACT(YEAR FROM a.date) BETWEEN 2019 AND 2020;

--3
SELECT a.name, AVG(duration) FROM tracks t
JOIN albums a ON t.albumid = a.id 
GROUP BY a.name;

--4
SELECT DISTINCT  m.name
FROM musicians m
WHERE NOT EXISTS (
    SELECT * FROM musicians_albums ma
    JOIN albums a ON ma.albumid = a.id
    WHERE ma.musicianid = m.id AND EXTRACT(YEAR FROM a.date) = 2020
);

--5
SELECT DISTINCT c.name FROM collections c
JOIN collection_tracks ct ON c.id = ct.collectionid 
JOIN tracks t ON t.id = ct.trackid
JOIN albums a ON a.id = t.albumid
JOIN musicians_albums ma ON ma.albumid =  a.id
JOIN musicians m ON m.id = ma.musicianid 
WHERE m.name = 'Sabaton';

--Task 4

--1
SELECT a.name FROM albums a
JOIN musicians_albums ma ON a.id = ma.albumid 
JOIN musicians m ON m.id = ma.musicianid
JOIN genre_and_musician gm ON m.id = gm.musicianid 
JOIN musical_genre g ON gm.genreid = g.id  
GROUP BY a.name, gm.musicianid
HAVING COUNT(DISTINCT g.name) > 1;

--2
SELECT DISTINCT t.name FROM tracks t
LEFT JOIN collection_tracks ct ON ct.trackid = t.id
WHERE ct.trackid IS NULL;

--3
SELECT m.name FROM musicians m
JOIN musicians_albums ma ON m.id = ma.musicianid
JOIN tracks t ON ma.albumid = t.albumid
WHERE t.duration = (SELECT MIN(duration) FROM tracks)
ORDER BY m.name;

--4
SELECT a.name FROM albums a
JOIN tracks t ON a.id = t.albumid
GROUP BY a.name
HAVING COUNT(t.id) = (SELECT MIN(track_count) FROM ( SELECT COUNT(*) AS track_count FROM tracks
        GROUP BY albumid
    )
);
