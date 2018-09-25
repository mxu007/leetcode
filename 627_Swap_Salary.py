# Given a table salary, such as the one below, that has m=male and f=female values. Swap all f and m values (i.e., change all f values to m and vice versa) with a single update query and no intermediate temp table.
# For example:
# | id | name | sex | salary |
# |----|------|-----|--------|
# | 1  | A    | m   | 2500   |
# | 2  | B    | f   | 1500   |
# | 3  | C    | m   | 5500   |
# | 4  | D    | f   | 500    |
# After running your query, the above salary table should have the following rows:
# | id | name | sex | salary |
# |----|------|-----|--------|
# | 1  | A    | f   | 2500   |
# | 2  | B    | m   | 1500   |
# | 3  | C    | f   | 5500   |
# | 4  | D    | m   | 500    |

# https://leetcode.com/problems/swap-salary/description/

# 1) use UPDATE, SET and IF
UPDATE salary
SET sex = IF (sex='m', 'f', 'm')

# 2) use UPDATE, SET and CASE
UPDATE salary
SET sex = CASE WHEN sex = 'f' THEN 'm'
    WHEN sex = 'm' THEN 'f'
    END

# 3) # Write your MySQL query statement below
# bitwise XOR
# ASCII() returns the number code of the first character in "CustomerName"
# CHAR() converts an int ASCII code to a character value
UPDATE salary SET sex = CHAR(ASCII('f') ^ ASCII('m') ^ ASCII(sex));

# 4) variant of 3)
UPDATE salary SET sex = CHAR(ASCII('f') + ASCII('m') - ASCII(sex));
