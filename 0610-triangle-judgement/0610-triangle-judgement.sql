# Write your MySQL query statement below
SELECT X,Y,Z, CASE 
WHEN x + y > z AND x + z > y AND y + z > x THEN 'Yes'
ELSE 'No'
END AS triangle
FROM triangle ;

