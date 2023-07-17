install: # установить зависимости
	poetry install

gendiff_: #запуск
	poetry run gendiff

build: #собрать пакет
	poetry build

publish: #публикация (не добавлять пакет в каталог PyPI)
	poetry publish --dry-run

package-install: #Для установки пакета из операционной системы
	python3 -m pip install --user dist/*.whl

reinstall: #Для переустановки пакета из операционной системы
	python3 -m pip install --force-reinstall dist/*.whl

lint: #запуск линтера
	poetry run flake8 gendiff

test: #запуск тестов
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

selfcheck:
	poetry check

check:
	selfcheck test lint
