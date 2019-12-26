git push heroku master
heroku ps:scale web=1
heroku ps -a
start heroku logs --tail
heroku open
