/*
Given two tables as below, write a query to display the comparison result (higher/lower/same) of the average salary of employees in a department to the company's average salary.
 
Table: salary
| id | employee_id | amount | pay_date   |
|----|-------------|--------|------------|
| 1  | 1           | 9000   | 2017-03-31 |
| 2  | 2           | 6000   | 2017-03-31 |
| 3  | 3           | 10000  | 2017-03-31 |
| 4  | 1           | 7000   | 2017-02-28 |
| 5  | 2           | 6000   | 2017-02-28 |
| 6  | 3           | 8000   | 2017-02-28 |
 
The employee_id column refers to the employee_id in the following table employee.
 
Table employee
| employee_id | department_id |
|-------------|---------------|
| 1           | 1             |
| 2           | 2             |
| 3           | 2             |
 
So for the sample data above, the result is:
| pay_month | department_id | comparison  |
|-----------|---------------|-------------|
| 2017-03   | 1             | higher      |
| 2017-03   | 2             | lower       |
| 2017-02   | 1             | same        |
| 2017-02   | 2             | same        |
*/


SELECT t1.pay_month, 
        t1.department_id,
        CASE WHEN t1.d_avg_amt < t2.c_avg_amt THEN "lower"
        WHEN t1.d_avg_amt = t2.c_avg_amt THEN "same"
        ELSE "higher" END AS comparison
FROM
    (SELECT e.department_id, LEFT(s.pay_date, 7) pay_month, AVG(s.amount) d_avg_amt
    FROM salary s
    INNER JOIN employee e
    ON s.employee_id = e.employee_id
    GROUP BY e.department_id, LEFT(s.pay_date, 7)) t1
INNER JOIN
    (SELECT LEFT(ss.pay_date, 7) pay_month, AVG(ss.amount) c_avg_amt
     FROM salary ss
     GROUP BY LEFT(ss.pay_date, 7)
    ) t2
ON t1.pay_month = t2.pay_month
ORDER BY t1.pay_month DESC, t1.department_id;
