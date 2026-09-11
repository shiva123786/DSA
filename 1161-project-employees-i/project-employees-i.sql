# Write your MySQL query statement below
SELECT 
    PROJECT.project_id, ROUND(AVG(EMPLOYEE.EXPERIENCE_YEARS),2)
AS 
    average_years
    FROM
        PROJECT PROJECT
    JOIN  
        EMPLOYEE EMPLOYEE 
        ON 
            EMPLOYEE.EMPLOYEE_ID=PROJECT.EMPLOYEE_ID 
            GROUP BY
            PROJECT.PROJECT_ID ;