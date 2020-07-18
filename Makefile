build: clean
	pipenv install && pipenv clean
	pipenv run python setup.py bdist_wheel
	pipenv run pipenv-setup sync --dev

clean:
	find . -name __pycache__ -type d -print0 | xargs rm -rf
	rm -rf build/ dist/ *.egg-info

publish: build
	pipenv run twine upload dist/*

tests:
	pipenv run python -m unittest iutils/tests/test_*.py
