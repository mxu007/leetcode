-- There is a table World

-- +-----------------+------------+------------+--------------+---------------+
-- | name            | continent  | area       | population   | gdp           |
-- +-----------------+------------+------------+--------------+---------------+
-- | Afghanistan     | Asia       | 652230     | 25500100     | 20343000      |
-- | Albania         | Europe     | 28748      | 2831741      | 12960000      |
-- | Algeria         | Africa     | 2381741    | 37100000     | 188681000     |
-- | Andorra         | Europe     | 468        | 78115        | 3712000       |
-- | Angola          | Africa     | 1246700    | 20609294     | 100990000     |
-- +-----------------+------------+------------+--------------+---------------+
-- A country is big if it has an area of bigger than 3 million square km or a population of more than 25 million.

-- Write a SQL solution to output big countries' name, population and area.

-- For example, according to the above table, we should output:

-- +--------------+-------------+--------------+
-- | name         | population  | area         |
-- +--------------+-------------+--------------+
-- | Afghanistan  | 25500100    | 652230       |
-- | Algeria      | 37100000    | 2381741      |
-- +--------------+-------------+--------------+

# https://leetcode.com/problems/big-countries/description/

# 1) simple method
# Write your MySQL query statement below
SELECT name, population, area
FROM World
WHERE area > 3000000 OR population > 25000000

# 2) union distinct
# Write your MySQL query statement below
# https://leetcode.com/problems/big-countries/discuss/103561/Union-and-OR-and-the-Explanation

# The UNION operator is used to combine the result-set of two or more SELECT statements.
# Each SELECT statement within UNION must have the same number of columns
# The columns must also have similar data types
# The columns in each SELECT statement must also be in the same order
# The UNION operator selects only distinct values by default. To allow duplicate values, use UNION ALL:

select name, population, area
from World
where area > 3000000
Union distinct
select name, population, area
from World
where population > 25000000;
