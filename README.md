# logs analysis project
an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.
## Requirments
1. bring the virtual machine back online
2. download the data from https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip. You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.
3. To load the data, cd into the vagrant directory and use the command psql -d news -f newsdata.sql.
4. create the follwing view that count the amount of access for each article (create or replace view articlesaccesscount as select count(*) as count,REPLACE(path,'/article/','') as article from log where path <>'/' group by path;
)
5. create the follwing view that combine each author with his article (create or replace view authorwitharticle as select authors.name,articles.slug as title from authors ,articles where authors.id=articles.author)
6. create the follwing view that count the amount of views for each author (create or replace view authorarticlscount as SELECT articlesaccesscount.count,authorwitharticle.name  FROM authorwitharticle, articlesaccesscount  WHERE authorwitharticle.title = articlesaccesscount.article)
7. create the follwing view that count the amount of requset error happened each day ( create view countrequestwitherror as select count(*),date(time) as date from log where status like '%404%' group by date(time))
8. create the follwing view that count requsets per day (create view requestberday as SELECT DISTINCT date(log."time") AS date, count(log.id) AS count   FROM log  GROUP BY (date(log."time")))
9. run the command python newsdb_solved.py

