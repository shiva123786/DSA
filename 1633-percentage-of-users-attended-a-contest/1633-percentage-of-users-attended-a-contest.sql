# Write your MySQL query statement below
SELECT 
r.contest_id, ROUND(
    COUNT(r.user_id)*100 / (select COUNT(*) from Users),2) as percentage
from register r
GROUP BY r.contest_id
ORDER BY percentage DESC, r.contest_id