.ONESHELL:


pre-commit: format lint doc-gen unittests
	@printf '\nfinished running precommit actions\n'

format:
	@printf '\nformatting python files with black\n'
	black .

lint:
	@printf '\nformatting then checking python files with ruff\n'
	ruff format .
	ruff check .

fix:
	@printf '\nfixing python files with ruff\n'
	ruff . --fix

doc-gen:
	@printf '\nmaking docs\n'
	sphinx-apidoc -T -f -o ./docs/source examples tests

unittests:
	@printf '\nrunning unittests\n'
	coverage run --source=. -m unittest tests/*_test.py tests/*/*_test.py
	coverage lcov 