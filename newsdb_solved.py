# Database code for the DB news, full solution!

import psycopg2
import datetime

DBNAME = "news"


def get_popular_articles():
    """Return the most popular three articles of all time"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select * from articlesaccesscount order by count desc limit 3;")
    articles = c.fetchall()
    db.close()
    return articles


def get_popular_authors():
    """the most popular article authors of all time."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select articlesaccesscount.count,articlesaccesscount.article,authorwitharticle.name from authorwitharticle,articlesaccesscount where authorwitharticle.title=articlesaccesscount.article order by articlesaccesscount.count desc")  # noqa
    authors = c.fetchall()
    db.close()
    return authors


def get_days_request_error():
    """days did more than 1% of requests lead to errors."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select * from countrequestwitherror")
    days = c.fetchall()
    db.close()
    return days


def get_logs_count():
    """get number of logs in log table."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select count(*) from log")
    count = c.fetchall()
    db.close()
    return count

print("most popular three articles\n")
articles = get_popular_articles()
for article in articles:
    print(str(article[1]) + '  - ' + str(article[0]) + ' viwes \n')

print("\nmost popular authors\n")
authors = get_popular_authors()
for author in authors:
    print(str(author[2]) + '  - ' + str(author[0]) + ' viwes \n')

print("\ndays did more than 1% of requests lead to errors\n")
days = get_days_request_error()
count = get_logs_count()
for day in days:
    errorpercent = round(day[0] * 100.00 / count[0][0], 3)
    if(errorpercent > 0.01):
        print(day[1].strftime('%b %d,%Y') + '  - ' + str(errorpercent*100) + '% errors\n')  # noqa
