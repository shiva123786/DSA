# Write your MySQL query statement below
with fp as(
select patient_id,min(test_date) first_positive
from covid_tests
where result='Positive'
group by patient_id
),
fn as(
select c.patient_id,min(c.test_date) first_negative
from covid_tests c
join fp f
on c.patient_id=f.patient_id
and c.test_date>f.first_positive
where c.result='Negative'
group by c.patient_id
)
select p.patient_id,
p.patient_name,
p.age,
datediff(fn.first_negative,fp.first_positive) recovery_time
from patients p
join fp
on p.patient_id=fp.patient_id
join fn
on p.patient_id=fn.patient_id
order by recovery_time,patient_name;