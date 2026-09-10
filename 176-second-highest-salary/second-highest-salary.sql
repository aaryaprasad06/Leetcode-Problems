# Write your MySQL query statement below
SELECT DISTINCT Max(salary) as SecondHighestSalary 
from Employee 
WHERE salary NOT IN (SELECT DISTINCT Max(salary)
from Employee ORDER BY salary DESC )
;