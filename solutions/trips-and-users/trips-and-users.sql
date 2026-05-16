select t.request_at as Day, round( 
    sum(case 
    when t.status != "completed" then 1
    else 0
    end )/count(*),
    2 
    ) as "Cancellation Rate" 
from Trips t
join users u1
on t.client_id=u1.users_id

join users as u2
on t.driver_id=u2.users_id

where 
    u1.banned="No" and u2.banned="No"
    and t.request_at between "2013-10-01" and "2013-10-03"
 
group by t.request_at
order by t.request_at;


 