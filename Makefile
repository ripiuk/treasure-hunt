.PHONY: install-python-repo install-python venv-init

PYTHON=python3.7


# ========== Linux (Debian) ==========


# ----- Install -----

install-python-repo:
	sudo add-apt-repository -y ppa:deadsnakes/ppa
	sudo apt-get update

install-python:
	sudo apt-get install -y $(PYTHON) $(PYTHON)-dev $(PYTHON)-venv cython
	sudo apt-get install -y build-essential libssl-dev libffi-dev openssl


# ----- Virtualenv -----

venv-init:
	export XXHASH_FORCE_CFFI=1
	if [ ! -d "venv" ]; then $(PYTHON) -m venv venv ; fi;
	bash -c "source venv/bin/activate && \
		pip install --upgrade wheel pip && \
		pip install --upgrade --requirement requirements.txt"


# ----- Setup -----

setup: install-python-repo install-python venv-init


# ----- Update -----

update: venv-init


# ----- Tests -----

test: update
	  pytest treasure_hunt/tests/ -vv . --flake8

test-cov:
	pytest --cov-report html:.cov_html --cov-branch --cov=treasure_hunt/ --cov-report term -vv . --flake8
	@python -m webbrowser -t "file://`pwd`/.cov_html/index.html" &


# ----- Run -----

run:
	python run.py

run-oop:
	python run.py oop