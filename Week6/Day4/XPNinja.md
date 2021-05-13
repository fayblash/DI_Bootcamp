<!-- Subqueries
Write a query to find the first_name, last_name and salaries of the employees who have a higher salary than the employee whose last_name is Bull. -->
select first_name,last_name,salary from employees
where salary>(select salary from employees where last_name='Grant')

<!-- Write a SQL subquery to find the first_name and last_name of the employees under a manager who works for a department based in the United States.
Hint : Write single-row and multiple-row subqueries -->
select first_name,last_name from employees
inner join departments on employees.department_id=departments_department_id
where manager_id (select employees.department_id where departments.location_id=
US')

Write a SQL subquery to find the first_name and last_name of the employees who are working as managers.

Write a SQL subquery to find the employee(s) first_name and last_name, which salary is greater than the average salary of the employees.

Write a SQL subquery to find the employee(s) first_name and last_name, which salary is equal to the minimum salary for this post, he/she is working on.

Write a query to find the names (first_name, last_name) of the employees who are not supervisors.

Write a SQL subquery to find the employee(s) ID, first name, last name and salary of all employees whose salary is above the average salary for their departments.

Write a subquery to find the 5th maximum salary of all salaries.

Write a subquery to find the 4th minimum salary of all the salaries.

Write a query to list the department name and number, of all the departments in which there are no employees.

Write a query to get nth max salaries of employees.
Joins
Write a query to find the addresses (location_id, street_address, city, state_province, country_name) of all the departments.

Write a query to make a join with employees and departments table to find the name of the employee, including first_name and last name, department ID and name of departments.

Write a SQL query to make a join with three tables: employees, departments and locations to find the name, including first_name and last_name, jobs, department name and ID, of the employees working in London.

Write a query to make a join with two tables to find the employee id, last_name as Employee along with their manager_id and last name as Manager.

Write a query to make a join with two tables employees and departments, to get the employees working in each department (retrieve the employees details, and the department name and number).

Write a query to make a join to find the employees who worked in a department which ID is 90 (retrieve the employee ID, job title and number of days the employee worked).

Write a query to make a join with three tables departments, employees, and locations to display the department name, manager name, and city.

Write a query to make a join with two tables employees and jobs to display the job title and average salary of the employees.

Write a query to make a join with two tables employees and departments to display department name, first_name and last_name, hire date and salary for all the managers who achieved a working experience of more than 15 years.

String Function
Write a query to update phone_number records. If the the substring ‘124’ was found in that column, update the phone_number to ‘999’.

Write a query to find the details of the employees who contain eight or more characters in their first name.

Write a query to join in uppercase, the first letter of the first_name, with the last_name, with '@example.com‘ in the email column.

  **Sample Output :**
  EMAIL
  --------------------

  JDOE@example.com (where first_name is John, and last_name is Doe)


Write a query to get the employee id, email but discard the last three characters of the email.


Write a query to display the first word in the job title, if the job title contains more than one words.

Write a query that displays the first name and the length of the first name for all employees whose name starts with the letters ‘A’, ‘J’ or ‘M’. Give each column an appropriate label. Sort the results by the employees’ first names.

Write a query to display the first name and salary for all employees. Display the salary with the $ symbol. Label the column as SALARY.


