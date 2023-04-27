# Demo FastAPI App

## build & run
```
# up, and specify build if you need to rebuild your images
docker compose up --build

# down
docker compose down
```
http://localhost:3001

You can change the exposed ports in `doker-compose.yml`

## Database, migrations
This app uses SQLAlchemy as an ORM with Alembic for migrations.
```
# shell into app container (in src dir)
docker container exec -it fastapi-demo-demo-app-1 bash

# run migrations (need to do this on your first build)
alembic upgrade head

# make new migrations
alembic revision --autogenerate -m "{Description of migration}"
```
You can also access the postgres db directly
```
# shell into db container
docker exec -it fastapi-demo-demo-db-1 bash -c 'psql -U user -d demo-db'

# see tables
\dt
```

## generated docs
http://localhost:3001/docs
