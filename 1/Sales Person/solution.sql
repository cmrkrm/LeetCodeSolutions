-- Write an SQL query to report the names of all the salespersons who did not have any orders related to the company with the name "RED".
-- Return the result table in any order.

-- Solution 1
SELECT SalesPerson.name FROM SalesPerson 
WHERE SalesPerson.name NOT IN ( 
    SELECT SalesPerson.name FROM SalesPerson
        LEFT JOIN Orders ON SalesPerson.sales_id = Orders.sales_id
        LEFT JOIN Company ON Company.com_id = Orders.com_id
    WHERE Company.name = 'RED'
)

-- Solution 2
SELECT SalesPerson.name FROM SalesPerson
WHERE SalesPerson.name NOT IN (
    SELECT SalesPerson.name FROM SalesPerson
    WHERE sales_id IN (
        SELECT sales_id FROM Orders 
        WHERE com_id = (
            SELECT com_id FROM Company
            WHERE name = 'RED'
        )
    )
)