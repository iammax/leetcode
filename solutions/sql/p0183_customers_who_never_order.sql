# Write your MySQL query statement below


select Customers.Name as Customers from Customers  where Customers.Id not in  (
select Customers.Id from Customers, Orders where Customers.Id=Orders.CustomerId
)
