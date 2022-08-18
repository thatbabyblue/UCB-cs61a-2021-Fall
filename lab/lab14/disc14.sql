SELECT quarter FROM scoring GROUP BY quarter HAVING SUM(points) > 10;

SELECT b.team, sum(a.points) FROM scoring AS a, players AS b WHERE a.player = b.name GROUP BY team;