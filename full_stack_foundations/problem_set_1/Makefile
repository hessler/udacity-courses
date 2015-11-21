#-----------------------------------------------------------------------
# Pylint in Makefile: http://stackoverflow.com/a/23140239/1914233
#-----------------------------------------------------------------------
run: ;
	@python puppy_shelter

delete_db: ;
	@rm -f puppy_shelter/puppies.db
	@echo "Database removed."

fetch_puppies_alphabetical: puppy_shelter;
	@python -c 'from puppy_shelter.puppies import fetch_all_puppies_alphabetical; fetch_all_puppies_alphabetical()'

fetch_puppies_age: puppy_shelter;
	@python -c 'from puppy_shelter.puppies import fetch_puppies_age; fetch_puppies_age()'

fetch_puppies_weight: puppy_shelter;
	@python -c 'from puppy_shelter.puppies import fetch_puppies_weight; fetch_puppies_weight()'

fetch_puppies_by_shelter: puppy_shelter;
	@python -c 'from puppy_shelter.puppies import fetch_puppies_by_shelter; fetch_puppies_by_shelter()'

lint:
	@for py in */*.py; \
	do \
		echo "Linting File: $$py";\
		pylint --rcfile=config.pylintrc $$py; \
	done
