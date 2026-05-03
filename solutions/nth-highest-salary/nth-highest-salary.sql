-- CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
-- BEGIN
--   RETURN (
--     --  select  distinct salary as getNthHighestSalary
--     --  from Employee 
--     --  order by salary desc 
--     --  LIMIT 1 OFFSET N-1


--     select salary 
--     from 
--     (select salary ,
--         dense_rank () over (
--             order by salary desc
--         ) as rnk
--         from Employee
--     )t
--     where rnk =N
--   );
-- END

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
    SELECT max(salary)
    FROM (
      SELECT 
        salary,
        DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
      FROM Employee
    ) t
    WHERE rnk = N
  );
END