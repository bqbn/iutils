build: clean
	pipenv run python -m build --wheel

clean:
	find . -type d -name __pycache__ -print0 | xargs rm -rfv
	find . -type d -name \*\.egg-info -print0 | xargs rm -rfv
	rm -rfv build/ dist/

publish: build
	pipenv run twine upload dist/*

tests:
	pipenv run python -m unittest iutils/tests/test_*.py
