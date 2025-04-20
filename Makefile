django_path:
	python -c "import django; print(django.__path__)"

create_Project:
	python -m django startproject inventory .

runserver:
	python manage.py runserver

startapp:
	python manage.py startapp items

makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

createsuper:
	python manage.py createsuperuser

shell:
	python manage.py shell

debugsqlshell:
	python manage.py debugsqlshell

test:
	python manage.py test polls

coverage:
	coverage run --source='.' manage.py test polls
	coverage report

production:
	docker-compose -f docker-compose.prod.yml build
	docker-compose -f docker-compose.prod.yml up -d
