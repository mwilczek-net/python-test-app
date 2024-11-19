# README python-test-app

Python Test APP which uses Python Test Library

## VENV
Poetry

Initialise VENV

```sh
poetry config virtualenvs.in-project true
poetry env use "$(which python3.11)"
```

Stard VENV

```sh
source .venv/bin/activate
```

Install dependencies (after venv activation)
```sh
poetry install
```

## New project

Creates new directory:

```sh
poetry new PROJECT-NAME
```

Inside current directory

```sh
poetry init --name="PROJECT-NAME"
```

## TESTS

```sh
python -m pytest
```

## Install dependencies

## Depencencies

```sh
poetry add git+ssh://git@github.mwilczek-net:mwilczek-net/python-test-lib.git#master
```

### DEV dependencies

```sh
poetry add pytest@latest --dev
poetry add pytest@8.3.3 --dev
```