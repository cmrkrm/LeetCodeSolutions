# Write your MySQL query statement below

#Solution-1
SELECT SalesPerson.name FROM SalesPerson
WHERE SalesPerson.sales_id NOT IN (SELECT Orders.sales_id FROM Orders WHERE Orders.com_id IN ( SELECT Company.com_id FROM Company WHERE Company.name = 'RED'))

#Solution-2
SELECT SalesPerson.name FROM SalesPerson
WHERE SalesPerson.sales_id NOT IN (SELECT Orders.sales_id FROM Orders INNER JOIN Company ON Orders.com_id = Company.com_id WHERE Company.name = 'RED')
