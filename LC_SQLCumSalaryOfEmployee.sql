 -- The Employee table holds the salary information in a year.

/*
Write a SQL to get the cumulative sum of an employee's salary over a period of 3 months but exclude the most recent month.
The result should be displayed by 'Id' ascending, and then by 'Month' descending.
Example
Input
| Id | Month | Salary |
|----|-------|--------|
| 1  | 1     | 20     |
| 2  | 1     | 20     |
| 1  | 2     | 30     |
| 2  | 2     | 30     |
| 3  | 2     | 40     |
| 1  | 3     | 40     |
| 3  | 3     | 60     |
| 1  | 4     | 60     |
| 3  | 4     | 70     |
Output
| Id | Month | Salary |
|----|-------|--------|
| 1  | 3     | 90     |
| 1  | 2     | 50     |
| 1  | 1     | 20     |
| 2  | 1     | 20     |
| 3  | 3     | 100    |
| 3  | 2     | 40     |
 
Explanation
Employee '1' has 3 salary records for the following 3 months except the most recent month '4': salary 40 for month '3', 30 for month '2' and 20 for month '1'
So the cumulative sum of salary of this employee over 3 months is 90(40+30+20), 50(30+20) and 20 respectively.
| Id | Month | Salary |
|----|-------|--------|
| 1  | 3     | 90     |
| 1  | 2     | 50     |
| 1  | 1     | 20     |
Employee '2' only has one salary record (month '1') except its most recent month '2'.
| Id | Month | Salary |
|----|-------|--------|
| 2  | 1     | 20     |
 
Employee '3' has two salary records except its most recent pay month '4': month '3' with 60 and month '2' with 40. So the cumulative salary is as following.
| Id | Month | Salary |
|----|-------|--------|
| 3  | 3     | 100    |
| 3  | 2     | 40     |
*/

SELECT t1.id, t1.month, t1.salary + coalesce(t2.salary, 0) + coalesce(t3.salary, 0) salary
FROM employee t1
LEFT JOIN employee t2
ON t1.id = t2.id AND t1.month = t2.month + 1
LEFT JOIN employee t3
ON t1.id = t3.id AND t1.month = t3.month + 2
INNER JOIN (SELECT id, max(month) m_month 
            FROM employee 
            GROUP BY id) t4
ON t1.id = t4.id and t1.month != t4.m_month
ORDER BY t1.id, t1.month DESC;