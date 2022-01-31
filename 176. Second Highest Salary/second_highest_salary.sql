SELECT max(ranked_salaries.salary) as SecondHighestSalary FROM 
    (SELECT salary, DENSE_RANK() OVER(order by salary DESC) rk FROM employee) ranked_salaries
WHERE rk = 2
