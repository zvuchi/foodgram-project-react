# praktikum_new_diplom

1. start
из папки /foodgram-project-react/infra
```bash
docker-compose -f docker-compose.yml up -d
```

2. service
```bash
docker compose exec backend python manage.py makemigrations
docker compose exec backend python manage.py migrate
docker compose exec backend python manage.py collectstatic --no-input
docker-compose exec backend python manage.py load_ingredients
docker compose exec backend python manage.py createsuperuser
```

3. rebuild 
```bash
docker-compose up -d --no-deps --build {{app_name}}
```
