# Write your MySQL query statement below
select 
    e.name
from 
    Employee e
JOIN 
    (SELECT MANAGERID
    FROM EMPLOYEE
    WHERE MANAGERID IS NOT NULL
    GROUP BY MANAGERID
    HAVING COUNT(*) >= 5
    ) AS MGR ON E.ID = MGR.MANAGERID ;