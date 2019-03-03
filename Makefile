re:
	@echo '-----------isort-----------'
	@isort  -rc .
	@echo '-----------flake8-----------'
	@flake8 --ignore=E501 ccas.py test_ccas.py
	@echo '-------------End------------'

test:
	@echo '-----------pytest-----------'
	@pytest -v test_ccas.py

mark:
	@echo '-----------benchmark-----------'
	@python3 benchmark.py