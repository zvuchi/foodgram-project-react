# praktikum_new_diplom

# start
из папки /foodgram-project-react/infra
docker-compose -f docker-compose.yml up -d

# service
docker compose exec backend python manage.py makemigrations
docker compose exec backend python manage.py migrate
docker compose exec backend python manage.py collectstatic --no-input
docker-compose exec backend python manage.py load_ingredients
docker compose exec backend python manage.py createsuperuser

# rebuild 
docker-compose up -d --no-deps --build
