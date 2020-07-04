build: clean
	python setup.py bdist_wheel

clean:
	rm -rf build/ dist/ *.egg-info

publish:
	twine upload dist/*

tests:
	python -m unittest iutils/tests/test_*.py
