# Newscrawler App

The purpose of this app is to query a postgreSQL database.

#### Questions Answered by the app:
1. What are the 3 most popular articles of all time?
2. Who are the most popular authors?
3. On what days did more than 1% of requests lead to errors?

### Important: Custom View Creation

**for the app to run you must create a custom view in the database**

open up the news database with postgreSQL and run the following code:


```
CREATE VIEW dailyerrors AS 
SELECT sum(case when status = '404 NOT FOUND' then 1 else 0 end)/ count(status) ::decimal *100 AS "errors",
 date(time) FROM log GROUP BY date(time);
 ```
 
 this creates the view "dailyerrors" for the last question to select from.

