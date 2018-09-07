# logs analysis project
an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.
## Requirments
1. bring the virtual machine back online
2. create the follwing view that count the amount of access for each article (create or replace view articlesaccesscount as select count(*) as count,REPLACE(path,'/article/','') as article from log where path <>'/' group by path;
)
3. create the follwing view that combine each author with his article (create or replace view authorwitharticle as select authors.name,articles.slug as title from authors ,articles where authors.id=articles.author)
4. create the follwing view that count the amount of requset error happened each day ( create view countrequestwitherror as select count(*),date(time) as date from log where status like '%404%' group by date(time))
5. run the command python newsdb_solved.py

