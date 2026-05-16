-- # Write your MySQL query statement below
-- select w1.id 
-- from weather w1
-- join weather w2
-- on datediff(w1.recordDate, w2.recordDate)=1
-- where w1.temperature >w2.temperature ;

select id
from(
    select id,recordDate, temperature ,
    lag(recordDate) over (order by recordDate ) as prev_day,
    lag(temperature) over (order by recordDate ) as prev_temp
    from Weather 
) t
where temperature>prev_temp
and datediff(recordDate, prev_day)=1;