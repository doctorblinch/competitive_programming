# [176. Second Highest Salary](https://leetcode.com/problems/second-highest-salary)

Difficulty: **Medium**

Feels like: **Medium**

Language: **SQL**

## Problem description

Table: **Employee**

+-------------+------+\
| Column Name | Type |\
+-------------+------+\
| id          | int  |\
| salary      | int  |\
+-------------+------+

id is the primary key column for this table.

Each row of this table contains information about the salary of an employee.

Write an SQL query to report the second highest salary from the Employee table. If there is no second highest salary, the query should report *null*.

The query result format is in the following example.

## Solution idea

In order to get employees ranked by salary we have a subquery with a window function. After that we select $2^{nd}$ salary, max function is not obligatory in the query but is needed to meet the *null* requirement.

```sql
SELECT max(ranked_salaries.salary) as SecondHighestSalary FROM 
    (SELECT salary, DENSE_RANK() OVER(order by salary DESC) rk FROM employee) ranked_salaries
WHERE rk = 2
```
