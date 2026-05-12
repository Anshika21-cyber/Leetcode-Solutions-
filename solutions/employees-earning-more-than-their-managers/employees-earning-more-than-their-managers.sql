select e.name as Employee 
from Employee as e
join Employee m
on e.managerId=m.id
where e.salary>m.salary;