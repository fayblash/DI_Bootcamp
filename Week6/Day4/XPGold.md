<!-- Update Statement
Write a SQL statement to change the following details belonging all employes who’s department_id is 110:
email column should be: ‘not available’
commission_pct column should be: 0.10 -->

update employees
set email='not available'
where department_id=10

<!-- Write a SQL statement which will change the email column of all employees to ‘available’ whom work in the ‘Accounting’ department. -->

update employees
set email='available'
from departments
where  employees.department_id=departments.department_id
and departments.department_name='Accounting'

<!-- Write a SQL statement to change the salary of the employee whose ID is 105. If the existing salary is less than 5000, change it to 8000. -->

update employees
set salary=8000
where employee_id=105 and salary<5000;


<!-- Aggregate Functions
Write a query to find the number of jobs available in the employees table. -->
select count(*),job_id from employees
group by job_id

<!-- Write a query to get the number of employees working in each post. -->

<!-- Write a query to get the difference between the highest and lowest salaries. -->
select max(salary),min(salary),max(salary)-min(salary) as difference from employees

<!-- Write a query to find a manager ID and the salary of the lowest-paid employee under that manager. -->
select min(salary),manager_id from employees
group by manager_id

<!-- Write a query to get the average salary for each post excluding programmer. -->
select round(avg(salary),2),jobs.job_title from employees
inner join jobs on employees.job_id=jobs.job_id
where jobs.job_title!='Programmer'
group by jobs.job_title

<!-- Write a query to get the average salary for all departments that employ more than 10 employees. -->
select round(avg(salary),2),departments.department_name, count(*) from employees
inner join departments on employees.department_id=departments.department_id
group by departments.department_name

<!-- Alter Table Statement
Write a SQL statement to change the name of the column “state_province” to “state” in the locations table, keeping the same data type and size. -->

ALTER TABLE locations
  RENAME COLUMN state_province TO state;

<!-- Write a SQL statement to add a primary key to the “location_id” column in the locations table. -->

ALTER TABLE locations ADD PRIMARY KEY (location_id);


Create Tables
Some Review:

ON UPDATE CASCADE action allows you to perform the cross-table update
ON DELETE RESTRICT action rejects the deletion.
ON DELETE CASCADE action allows to delete records in the employees(child) table that refers to a record in the jobs(parent) table when the record in the parent table is deleted
ON DELETE SET NULL action will set the foreign key column values in the child table(employees) to NULL when the record in the parent table(jobs) is deleted, with a condition that the foreign key column in the child table must accept NULL values.
ON UPDATE SET NULL action resets the values in the rows in the child table(employees) to NULL values when the rows in the parent table(jobs) are updated.
The default action is ON DELETE RESTRICT.
ON DELETE NO ACTION and the ON UPDATE NO ACTION actions will reject the deletion and any updates.


You have to decide which constraint should be used in every question below:



<!-- Write a SQL statement to create a simple table “new_countries” including columns country_id and country_name.
make sure that no duplicate data is added to the country_id column (which data type should you use for the column country_id ?)
make sure that no countries except Italy, India and China will be entered in the table. -->

create table new_countries(
    country_id serial primary key,
    country_name varchar(50) check country_name in ('Italy','India','China')
)

<!-- Write a SQL statement to create a duplicate copy of the “new_countries” table including the structure and the data of the “new_countries” table. -->
CREATE TABLE duplicate_countries LIKE new_countries;
INSERT INTO duplicate_countries SELECT * FROM new_countries;

Write a SQL statement to create a table named “new_jobs” including columns job_id, job_title, min_salary, max_salary
make sure that max_salary amount won’t exceed 25000.
make sure that, the default value for job_title is blank, for min_salary is 8000 and for max_salary is NULL.

Write a SQL statement to create a table “new_employees” including columns employee_id, first_name, last_name, email, phone_number hire_date, job_id, salary,
make sure that, the employee_id column does not contain any duplicate value at the time of insertion,
make sure that the foreign key column job_id, references the column job_id of the “new_jobs” table.

Write a SQL statement to create a table “new_job_history” including columns employee_id, start_date, end_date, job_id
make sure that the foreign key employee_id references the column employee_id of the “new_employees” table
make sure that the foreign key column job_id contain only those values which exist in the “new_jobs” table.


<!-- Insert
Write a SQL statement to insert a record with your own value into the table “new_countries”. -->

insert new_countries(country_name)
values('Italy');

<!-- Write a SQL statement to insert 3 rows by a single insert statement. -->
insert new_countries(country_name)
values
('Italy'),
('Spain'),
('Portugal');

<!-- Write a SQL statement to insert rows from the “new_countries” table to the duplicate table. -->


Write a SQL statement to insert rows into the table “new_employees”, in which the column job_id contains the values which must exist into the table “new_jobs”.


