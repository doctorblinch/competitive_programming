# [626. Exchange Seats](https://leetcode.com/problems/exchange-seats)

Difficulty: **Medium**

Feels like: **Medium**

Language: **SQL**

## Problem description

Table: **Seat**

+-------------+---------+\
| Column Name | Type    |\
+-------------+---------+\
| id          | int     |\
| name        | varchar |\
+-------------+---------+

id is the primary key column for this table.

Each row of this table indicates the name and the ID of a student.

id is a continuous increment.

Write an SQL query to swap the seat id of every two consecutive students. If the number of students is odd, the id of the last student is not swapped.

Return the result table ordered by id in ascending order.

The query result format is in the following example.

## Solution idea

The key idea is a self join where we either add or subtract 1 to get required ID, since last element should be left untouched we do a left join and check if *id is null* in *select* statement.

```sql
SELECT if(s0.id is not null, s0.id, s1.id) as id, s1.student
FROM seat s1
LEFT JOIN seat s0 ON s0.id = if(s0.id % 2 = 0, s1.id + 1, s1.id - 1)
ORDER BY id
```
