#-----------------------------------------------------------------------
# Pylint in Makefile: http://stackoverflow.com/a/23140239/1914233
#-----------------------------------------------------------------------

#-------------------
# Restaurant
#-------------------
serve_restaurant: setup_restaurant
	@python restaurant/project.py

setup_restaurant: ;
	@python restaurant
	@echo "Restaurant setup complete."

reset_restaurant: ;
	@rm -f restaurant/restaurantmenu.db
	@echo "Restaurant project reset and database removed."

#-------------------
# Puppy Shelter
#-------------------
serve_puppy_shelter: ;
	@python puppy_shelter/runserver.py

reset_puppy_shelter: ;
	@rm -f puppy_shelter/puppy_shelter/puppies.db
	@echo "Puppy Shelter project reset and database removed."

#-------------------
# General
#-------------------
lint:
	@for py in */*.py; \
	do \
		echo "Linting File: $$py";\
		pylint --rcfile=config.pylintrc $$py; \
	done
