# Development Guide

### Add Flake8 linter to your `.git/hooks/pre-commit`
```bash
cd $(git rev-parse --show-toplevel)
./bin/flake8.sh
if [ "$?" != "0" ]
then
    echo "ERROR: Flake8 FAILED!"
    exit 99
fi
``` 

### Add Black linter/autocorrector to your `.git/hooks/pre-commit`
```bash
cd $(git rev-parse --show-toplevel)
./bin/black.sh
if [ "$?" != "0" ]
then
    echo "ERROR: Black FAILED!"
    exit 99
fi
``` 

### Add PyLint linter to your `.git/hooks/pre-commit`
```bash
cd $(git rev-parse --show-toplevel)
./bin/lint.sh
if [ "$?" != "0" ]
then
    echo "ERROR: PyLint FAILED!"
    exit 99
fi
``` 

### Add MyPy linter to your `.git/hooks/pre-commit`
```bash
cd $(git rev-parse --show-toplevel)
./bin/mypy.sh
if [ "$?" != "0" ]
then
    echo "ERROR: MyPy FAILED!"
    exit 99
fi
``` 

### Add iSort linter/autocorrector to your `.git/hooks/pre-commit`
```bash
cd $(git rev-parse --show-toplevel)
./bin/isort.sh
if [ "$?" != "0" ]
then
    echo "ERROR: isort FAILED!"
    exit 99
fi
``` 
