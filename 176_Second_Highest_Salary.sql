-- Write a SQL query to get the second highest salary from the Employee table.

-- +----+--------+
-- | Id | Salary |
-- +----+--------+
-- | 1  | 100    |
-- | 2  | 200    |
-- | 3  | 300    |
-- +----+--------+
-- For example, given the above Employee table, the query should return 200 as the second highest salary. If there is no second highest salary, then the query should return null.

-- +---------------------+
-- | SecondHighestSalary |
-- +---------------------+
-- | 200                 |
-- +---------------------+

-- https://leetcode.com/problems/second-highest-salary/description/

# 1) Two Select and use < operator
# Write your MySQL query statement below
SELECT MAX(Salary) as SecondHighestSalary
FROM Employee
WHERE Salary < (select max(Salary) from Employee)

# 2) Use not in operator
SELECT MAX(Salary) as SecondHighestSalary
FROM Employee
WHERE Salary  NOT IN (select max(Salary) from Employee)

# 3) double select with LIMIT
# https://stackoverflow.com/questions/1106258/mysql-null-vs
select
(
SELECT DISTINCT Salary
FROM Employee
ORDER BY Salary DESC
LIMIT 1 OFFSET 1
) as SecondHighestSalary

# 4) IFNULL function
select
ifnull(
    (SELECT DISTINCT Salary
    FROM Employee
    ORDER BY Salary DESC
    LIMIT 1 OFFSET 1),
null) as SecondHighestSalary

# 5) Single select and union with NULL
SELECT distinct Salary AS SecondHighestSalary FROM Employee
UNION
SELECT NULL
ORDER BY SecondHighestSalary DESC LIMIT 1,1
