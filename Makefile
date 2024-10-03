install:
	poetry install

brain-games:
	poetry run brain-games

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall

build:
	poetry build

publish:
	poetry publish --dry-run

make lint:
	poetry run flake8 brain_games
