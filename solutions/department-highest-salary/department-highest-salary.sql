# Write your MySQL query statement below
select Department, Employee, Salary 
from (
    select
        d.name as Department ,e.name as Employee, e.salary as Salary ,
        DENSE_RANK() over (
            partition by d.id
            order by e.salary desc
        ) as rnk
    from Employee e 
    join Department d
    ON e.departmentId=d.id
    ) t
where rnk<=1

