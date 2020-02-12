
APP=api
ENV=development

help:
	@echo "init-dev";
	@echo "\tInitialize virtual env for development";
	@echo "run";
	@echo "\tStart local server (only use for dev or test)";

activate:
	source ./.venv/bin/activate

init:
	@virtualenv --python python3.7 .venv;
	$(MAKE) activate
ifdef env
ifeq (env, "dev")
	@pip install -r ./requirements/dev.txt
else
	@pip install -r ./requirements/base.txt
endif
else
	@pip install -r ./requirements/base.txt
endif

init-dev: init
	@pip install -r ./requirements/dev.txt

run: activate
	@export FLASK_APP=$(APP)
	@export FLASK_ENV=$(ENV)
	@flask run
