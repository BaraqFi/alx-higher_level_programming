-- Lists all records in table with content.
SELECT `score`, `name` FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC;
