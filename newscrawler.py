import datetime
import psycopg2

DBNAME = "news"


def most_popular_articles():
    """What are the most popular three articles of all time?"""
    db = psycopg2.connect(database=DBNAME)
    cur = db.cursor()
    cur.execute('select title,count(log.id) '
                'from articles join log on slug=substring(log.path,10) '
                'group by title order by count(log.id) desc limit 3;')
    posts = cur.fetchall()
    print(posts)
    db.close()


def most_popular_authors():
    """Who are the most popular article authors of all time?"""
    db = psycopg2.connect(database=DBNAME)
    cur = db.cursor()
    cur.execute('select name, count(log.id) '
                'from authors left join articles '
                'on authors.id=articles.author left join '
                'log on articles.slug=substring(log.path,10) '
                'group by name order by count(log.id) desc limit 1;')
    posts = cur.fetchall()
    print(posts)
    db.close()


def high_error_days():
    """On which days did more than 1% of requests lead to errors?"""
    db = psycopg2.connect(database=DBNAME)
    cur = db.cursor()
    cur.execute("select date from dailyerrors where errors>1;")
    posts = cur.fetchall()
    print(posts)
    db.close()


most_popular_articles()
most_popular_authors()
high_error_days()
