# Write your MySQL query statement below
SELECT 
    CASE 
        WHEN c.cnt > 1 THEN NULL
        ELSE eu.unique_id
    END AS unique_id,
    e.name
FROM Employees e
LEFT JOIN EmployeeUNI eu
    ON e.id = eu.id
JOIN (
    SELECT id, COUNT(*) AS cnt
    FROM Employees
    GROUP BY id
) c
ON e.id = c.id;