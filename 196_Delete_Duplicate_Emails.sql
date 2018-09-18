-- Write a SQL query to delete all duplicate email entries in a table named Person, keeping only unique emails based on its smallest Id.

-- +----+------------------+
-- | Id | Email            |
-- +----+------------------+
-- | 1  | john@example.com |
-- | 2  | bob@example.com  |
-- | 3  | john@example.com |
-- +----+------------------+
-- Id is the primary key column for this table.
-- For example, after running your query, the above Person table should have the following rows:

-- +----+------------------+
-- | Id | Email            |
-- +----+------------------+
-- | 1  | john@example.com |
-- | 2  | bob@example.com  |
-- +----+------------------+
-- Note:

-- Your output is the whole Person table after executing your sql. Use delete statement.
-- https://leetcode.com/problems/delete-duplicate-emails/description/

# 1) use three-layer SELECT, ORDER BY and GROUP BY
# GROUP BY removes the duplicate
# In MySQL, you can't modify the same table which you use in the SELECT part.

DELETE
FROM Person
WHERE Id NOT IN
(
    SELECT MIN(Id) FROM
    (
    SELECT *
    FROM Person
    ORDER BY Id, Email
    ) as c1
    GROUP BY Email
)

# 2) Use Table join and alias
DELETE p1 FROM Person p1,
    Person p2
WHERE
    p1.Email = p2.Email AND p1.Id > p2.Id

# 3) variant of 1)
DELETE
From Person
WHERE Id NOT IN
(
    SELECT * FROM
    (
    SELECT MIN(p1.Id)
    FROM Person p1
    GROUP BY p1.Email
    )
    AS tmp
);
