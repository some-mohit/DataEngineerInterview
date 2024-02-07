--Question 1: SQL Query to find the second highest salary of Employee
--Answer: There are many ways to find the second highest salary of an Employee in SQL,
--you can either use SQL Join or Subquery to solve this problem. Here is an SQL query using Subquery:


SELECT MAX(Salary)
FROM Employee
WHERE Salary NOT IN (
select MAX(Salary) from Employee );

Mohit,IT,3000
Rupali,CS,4000
Sumit,EC,6000
Rekha,EE,3500
SELECT MAX(Salary)
FROM Employee
WHERE Salary NOT IN (
6000);

-- Question 2: SQL Query to find Max Salary from each department.
-- Answer: You can find the maximum salary for each department by grouping all records by DeptId and
-- then using MAX() function to calculate the maximum salary in each group or each department.

SELECT DeptID, MAX(Salary)
FROM Employee
GROUP BY DeptID.

-- These questions become more interesting if the Interviewer will ask you to
-- print the department name instead of the department id, in that case, you need to join the Employee table with Department using the foreign key DeptID,
-- make sure you do LEFT or RIGHT OUTER JOIN to include departments without any employee as well.


SELECT DeptName, MAX(Salary)
FROM Employee e RIGHT JOIN Department d
ON e.DeptId = d.DeptID
GROUP BY DeptName;


--Question 4: Write an SQL Query to check whether the date passed to Query is the date of the given format or not?
-- Answer: SQL has IsDate() function which is used to check passed value is a date or not of specified format,
-- it returns 1(true) or 0(false) accordingly. Remember the ISDATE() is an MSSQL function and it may not work on Oracle, MySQL, or any other database but there would be something similar.

SELECT  ISDATE('1/08/13') AS "MM/DD/YY";


-- Question 5: Write an SQL Query to print the name of the distinct employee whose DOB is between 01/01/1960 to 31/12/1975.
-- Answer: This SQL query is tricky, but you can use BETWEEN clause to get all records whose dates fall between two dates.
SELECT DISTINCT EmpName
FROM Employees
WHERE DOB BETWEEN ‘01/01/1960’ AND ‘31/12/1975’;

-- Question 6: Write an SQL Query to find the number of employees according to gender whose DOB is between 01/01/1960 to 31/12/1975.
Answer :
SELECT COUNT(*), sex
FROM Employees
WHERE DOB BETWEEN '01/01/1960' AND '31/12/1975'
GROUP BY sex;
