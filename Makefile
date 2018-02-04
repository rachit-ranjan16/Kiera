VERSION = 1.3.0

build:
	python setup.py sdist --format=gztar
	python setup.py bdist_wheel
clean:
	rm -rf dist/
	rm -rf build/
	rm -rf *.egg-info
	rm -rf dat_struct_py/__pycache__
	rm -rf dat_struct_py/blocks/__pycache__
	rm -rf dat_struct_py/tests/__pycache__
	rm -rf .coverage
	rm -rf htmlcov
test:
	coverage run setup.py test
	coverage html
