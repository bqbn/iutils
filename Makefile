build: clean
	pipenv install && pipenv clean
	pipenv run python setup.py bdist_wheel
	pipenv run pipenv-setup sync --dev

clean:
	rm -rf build/ dist/ *.egg-info

publish:
	pipenv run twine upload dist/*

tests:
	pipenv run python -m unittest iutils/tests/test_*.py
