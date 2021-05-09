<!-- Exercise 1 : Bootcamp
Instructions
Continuation of the Exercise XPGold

Select
For the following questions, you have to fetch the first_names, last_names and birth_dates of the students. -->


<!-- Fetch the first four students. You have to order the four students alphabetically by last_name. -->
SELECT * FROM students ORDER BY last_name ASC LIMIT 4

<!-- Fetch the details of the youngest student. -->

SELECT * FROM students ORDER BY birth_date DESC LIMIT 1


<!-- Fetch three students skipping the first two students. -->
SELECT * FROM students LIMIT 3 OFFSET 2

