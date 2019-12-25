git push heroku master
heroku ps:scale web=1
start heroku logs --tail
heroku open
