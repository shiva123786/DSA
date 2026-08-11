# Write your MySQL query statement below
select employee_id,
case 
    when employee_id%2=1  and name Not like "M%"
    then salary
    else 0

END as bonus
from employees
order by employee_id;

