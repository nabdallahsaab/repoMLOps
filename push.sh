docker build . -t mlflow_container
docker tag mlflow_container registry.heroku.com/isen-mlflow-nadine/web
docker push registry.heroku.com/isen-mlflow-nadine/web
heroku container:login
heroku container:release web -a isen-mlflow-nadine
heroku open -a isen-mlflow-nadine  
heroku logs --app=isen-mlflow-nadine --tail