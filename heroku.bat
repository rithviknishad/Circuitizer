git push heroku master
echo Done
heroku logs --tail
heroku ps:scale web=1
heroku open
