PYTHON ?= 3.11
ENV_NAME ?= virtual-env

install:
	echo "Creating virtual environment"
	conda create -n $(ENV_NAME) python=$(PYTHON) --no-default-packages -y
