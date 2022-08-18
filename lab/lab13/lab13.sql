.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet FROM students where color = "blue" and pet = "dog";

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song FROM students where color = "blue" and pet = "dog";


CREATE TABLE smallest_int_having AS
  SELECT time, min(smallest) FROM students GROUP BY smallest HAVING count(smallest) = 1;


CREATE TABLE matchmaker AS
  SELECT a.pet, a.song, a.color, b.color FROM students AS a, students AS b WHERE a.time < b.time AND a.pet = b.pet AND a.song = b.song;


CREATE TABLE sevens AS
  SELECT seven FROM students, numbers WHERE students.time = numbers.time AND students.number = 7 AND numbers."7" = "True";


CREATE TABLE avg_difference AS
  SELECT round(avg(abs(number - smallest))) FROM students;

