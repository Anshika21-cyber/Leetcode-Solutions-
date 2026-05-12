-- # Write your MySQL query statement below
select c.name as Customers from Customers c
left join Orders o
on c.id=o.customerId
where o.customerId is null;

-- SELECT name as Customers
-- FROM Customers
-- WHERE id NOT IN (
--     SELECT customerId FROM Orders
-- );