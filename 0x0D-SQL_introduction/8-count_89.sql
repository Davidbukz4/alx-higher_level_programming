-- displays the number of records with id = 89 in the table first_table
-- cat 8-count_89.sql | mysql -hlocalhost -uroot -p hbtn_0c_0 | tail -1 to use
SELECT COUNT(id) FROM first_table WHERE id=89;
