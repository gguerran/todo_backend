prebuild:
	cp example.env .env
	cp example.db.env .db.env

dump_all:
	docker compose exec todo_django python manage.py dumpdata accounts core customer > fixtures/data.json

migrate:
	docker compose exec todo_django python manage.py migrate
zero_migrate:
	docker compose exec todo_django python manage.py migrate accounts zero
	docker compose exec todo_django python manage.py migrate core zero

makemigrations:
	docker compose exec todo_django python manage.py makemigrations

reset_migrations:
	docker compose exec todo_django find . -path "*/migrations/*.py" -not -name "__init__.py" -not -path "*/venv/*" -delete
	docker compose exec todo_django python manage.py makemigrations
	

delete_pycache:
	find . -path "*/__pycache__" | xargs rm -rf

load_data:
	docker compose exec todo_django python manage.py loaddata fixtures/*.json

load_user_data:
	docker compose exec todo_django  python manage.py loaddata users.json

test:
	docker compose exec todo_django python manage.py test

lint:
	black .
	flake8 . --extend-exclude=migrations,venv --max-line-length 120

runserver:
	docker compose up

build:
	docker compose up --build

deploy:
	ssh root@68.183.124.156 'cd /home/todo_backend/ && git pull origin main'

deploy_restart:
	ssh root@68.183.124.156 'cd /home/todo_backend/ && docker compose down && git pull origin main && docker compose up --build -d'

deploy_migrate:
	ssh root@68.183.124.156 'cd /home/todo_backend/ && git pull origin main && make migrate'
