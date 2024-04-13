-- script that updates the score
SELECT score, name FROM second_table ORDER BY score DESC;
UPDATE second_table SET score = 10 WHERE score = 14;
