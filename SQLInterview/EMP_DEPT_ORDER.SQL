CREATE TABLE emp (
  emp_id INT,
  emp_name VARCHAR(20),
  department_id INT,
  salary INT,
  manager_id INT,
  emp_age INT
);

INSERT INTO emp VALUES (1, 'Ankit', 100,10000, 4, 39);
INSERT INTO emp VALUES (2, 'Mohit', 100, 15000, 5, 48);
INSERT INTO emp VALUES (3, 'Vikas', 100, 10000,4,37);
INSERT INTO emp VALUES (4, 'Rohit', 100, 5000, 2, 16);
INSERT INTO emp VALUES (5, 'Mudit', 200, 12000, 6,55);
INSERT INTO emp VALUES (6, 'Agam', 200, 12000,2, 14);
INSERT INTO emp VALUES (7, 'Sanjay', 200, 9000, 2,13);
INSERT INTO emp VALUES (8, 'Ashish', 200,5000,2,12);
INSERT INTO emp VALUES (9, 'Mukesh',300,6000,6,51);
INSERT INTO emp VALUES (10, 'Rakesh',300,7000,6,50);

CREATE TABLE department(

 dept_id INT,
 dept_name VARCHAR(10)
 );

INSERT INTO department values(100,'Analytics');
INSERT INTO department values(300,'IT');

CREATE TABLE orders(
 customer_name CHAR(10),
 order_date DATE,
 order_amount INT,
 customer_gender CHAR(6)
 );

INSERT INTO orders values('Shilpa','2020-01-01',10000,'Female');
INSERT INTO orders values('Rahul','2020-01-02',12000,'Male');
INSERT INTO orders values('PRADEEP','2020-01-02',12000,'Female');
INSERT INTO orders values('Rohit','2020-01-03',15000,'Male');
INSERT INTO orders values('pradeep','2020-01-03',14000,'Female');

INSERT INTO department values(100,'Analytics');
INSERT INTO department values(300,'IT');


--  QUESTIONS ----
Q 1 : How to find duplicates in a given table?
SELECT
    emp_id, COUNT(*)
FROM
    emp
GROUP BY emp_id
HAVING COUNT(*) > 1;

-- How to delete duplicates?
WITH cte AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY emp_id ORDER BY emp_id) AS rn
    FROM emp
)
DELETE FROM cte WHERE rn > 1;

WITH MY_CTE AS (
    SELECT *,ROW_NUmber() over (Partition by emp_id order by emp_id) as row_number_col
)
delete from MY_CTE where row_number_col > 1

--  Employees who are not present in department table?
SELECT
    *
FROM
    emp AS e
        LEFT JOIN
    department AS d ON e.department_id = d.dept_id
WHERE d.dept_id IS NULL;


-- Second highest salary in each department?
-- Similar can be used for student who gor 2nd highest marks in class
SELECT *
FROM (
    SELECT
        emp_name,
        salary,
        department_id,
        DENSE_RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS rn
    FROM emp
) AS a
WHERE rn = 2;

--  Self Join, manager salary > employee salary?
SELECT
    e1.emp_id,
    e1.emp_name,
    e2.emp_name AS manager_name,
    e1.salary,
    e2.salary AS manager_salary
FROM
    emp AS e1
INNER JOIN
    emp AS e2 ON e1.manager_id = e2.emp_id
WHERE e2.salary > e1.salary;


-- Update query to swap gender?
UPDATE orders
SET
    customer_gender = CASE
        WHEN customer_gender = 'Male' THEN 'Female'
        WHEN customer_gender = 'Female' THEN 'Male'
    END


-- Consider a table EmployeeAttendance with columns – AttendanceID, EmployeeID, Date, Status. Write a query to find employees with more than 5 absences in a month.
-- This query filters the records for absent status, groups them by EmployeeID and month, and counts absences, filtering for more than 5 absences.
--
SELECT EmployeeID,
 MONTH(Date) AS Month,
 COUNT(*) AS Absences
 FROM EmployeeAttendance
    WHERE Status = 'Absent'
    GROUP BY EmployeeID, MONTH(Date)
    HAVING COUNT(*) > 5;