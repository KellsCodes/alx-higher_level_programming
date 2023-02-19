-- lists all records of the table second_table of the db hbtn_0c_0 in MySQL server ignoring rows with no name value displaying the score and name in desc order
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score desc;
