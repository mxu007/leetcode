-- Given a Weather table, write a SQL query to find all dates' Ids with higher temperature compared to its previous (yesterday's) dates.

-- +---------+------------------+------------------+
-- | Id(INT) | RecordDate(DATE) | Temperature(INT) |
-- +---------+------------------+------------------+
-- |       1 |       2015-01-01 |               10 |
-- |       2 |       2015-01-02 |               25 |
-- |       3 |       2015-01-03 |               20 |
-- |       4 |       2015-01-04 |               30 |
-- +---------+------------------+------------------+
-- For example, return the following Ids for the above Weather table:

-- +----+
-- | Id |
-- +----+
-- |  2 |
-- |  4 |
-- +----+

-- https://leetcode.com/problems/rising-temperature/description/

# 1) two layer select
select Weather_Delta.Id
from
(SELECT day1.Id as Id, day1.RecordDate, day1.Temperature-day0.Temperature AS delta
FROM Weather day1
INNER JOIN Weather day0 on DATEDIFF(day1.RecordDate,day0.RecordDate)=1) Weather_Delta
where Weather_Delta.delta > 0

# 2) single layer select
SELECT
    Day1.id AS 'Id'
FROM
    Weather Day1
        JOIN
    Weather Day0 ON DATEDIFF(Day1.RecordDate, Day0.RecordDate) = 1
        AND Day1.Temperature > Day0.Temperature

# 3) use subdate
# https://www.w3schools.com/sql/func_mysql_subdate.asp
SELECT
    t1.Id
FROM
    Weather t1, Weather t2
WHERE
    t1.Temperature > t2.Temperature AND subdate(t1.RecordDate, 1) = t2.RecordDate
