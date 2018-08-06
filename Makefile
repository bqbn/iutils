build: clean
	python setup.py bdist_wheel

clean:
	rm -rf build/ dist/

publish:
	twine upload dist/*

tests:
	python -m unittest iutils/tests/test_utils.py
