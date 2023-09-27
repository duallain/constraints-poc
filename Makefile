.ONESHELL:


pre-commit: format doc-gen unittests
	@printf '\nfinished running precommit actions\n'

format:
	@printf '\nformatting python files with black\n'
	black .


doc-gen:
	@printf '\nmaking docs\n'
	sphinx-apidoc -T -f -o ./docs/source practical_project_examples tests

unittests:
	@printf '\nrunning unittests\n'
	python3 -m unittest tests/*_test.py 