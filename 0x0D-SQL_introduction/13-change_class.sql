-- removes all records with a score <= 5 in the table second_table of htbn_0c_0 of MySQL server
DELETE FROM second_table WHERE score <= 5 ORDER BY score DESC;
