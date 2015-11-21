#-----------------------------------------------------------------------
# Pylint in Makefile: http://stackoverflow.com/a/23140239/1914233
#-----------------------------------------------------------------------
serve: setup
	@python webserver.py

lint:
	@for py in */*.py; \
	do \
		echo "Linting File: $$py";\
		pylint --rcfile=config.pylintrc $$py; \
	done

setup: ;
	@python restaurant
	@echo "Restaurant setup complete."

delete_db: ;
	@rm -f restaurant/restaurantmenu.db
	@echo "Database removed."
