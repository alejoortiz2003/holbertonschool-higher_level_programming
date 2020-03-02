-- creates a table called first_table
-- first_table description: id and name
-- The database name will be passed as an argument of the mysql command
-- If the table first_table already exists, your script should not fail
-- Not use SELECT or SHOW

CREATE TABLE IF NOT EXISTS first_table(
       id INT,
       name VARCHAR(256)
);
