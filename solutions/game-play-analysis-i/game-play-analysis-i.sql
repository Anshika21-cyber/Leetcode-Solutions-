# Write your MySQL query statement below
select player_id, first_login 
from (
    select 
    player_id,
    event_date as first_login,
    dense_rank()over(
        partition by player_id
        order by event_date asc 
    ) as rnk
    from Activity 
)as t
 where rnk <=1