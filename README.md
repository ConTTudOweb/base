# Base Project

Base project for the main system.

[![Build Status](https://travis-ci.org/ConTTudOweb/base.svg?branch=master)](https://travis-ci.org/ConTTudOweb/base)
[![Code Health](https://landscape.io/github/ConTTudOweb/base/master/landscape.svg?style=flat)](https://landscape.io/github/ConTTudOweb/base/master)
[![Coverage Status](https://coveralls.io/repos/github/ConTTudOweb/base/badge.svg?branch=master)](https://coveralls.io/github/ConTTudOweb/base?branch=master)
[![Maintainability](https://api.codeclimate.com/v1/badges/3c44b09f7d30c31f5c39/maintainability)](https://codeclimate.com/github/ConTTudOweb/base/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/3c44b09f7d30c31f5c39/test_coverage)](https://codeclimate.com/github/ConTTudOweb/base/test_coverage)

## How to develop?

1. Clone the repository;
2. Create a "virtualenv" with Python 3.6;
3. Activate the "virtualenv";
4. Upgrade the "pip";
5. Install the dependencies;
6. Configure the instance with the ".env";
7. Run the tests;

```console
git clone git@github.com:ConTTudOweb/base.git
cd base
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```
