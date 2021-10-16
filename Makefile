.PHONY: default test coverage docker-test docker-coverage
default: docker-test

test:
	pytest

mutation:
	mutmut run --paths-to-mutate coffee_machine || true
	mutmut html
	@echo "See the results in html/index.html"

coverage:
	coverage run --source=coffee_machine -m unittest
	coverage report
	coverage html
	@printf "To visualize the lines open the report at htmlcov/index.html\n"

docker-test:
	docker run --rm -v ${PWD}:/kata codiumteam/tdd-training-python make test

docker-coverage:
	@docker run --rm -v ${PWD}:/kata codiumteam/tdd-training-python make coverage

docker-mutation:
	@docker run --rm -v ${PWD}:/kata codiumteam/tdd-training-python make mutation