# Rising temperature

SELECT e1.id
FROM Weather e1
JOIN Weather e2
    ON DATEDIFF(e1.recordDate, e2.recordDate) = 1
AND e1.temperature > e2.temperature