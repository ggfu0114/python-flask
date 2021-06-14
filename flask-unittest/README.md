# 02-flask-unittest

## Describe

To execute the test function in the folder `test`, we have to import the source code folder into python system. Otherwise, the `ModuleNotFoundError` exception happened because the runtime system does't know the source folder.  Therefore, we add folder path import function in the `__init__` file, the path will be included every time we import the test module.

## Usage
### Running a single test module
```sh
python -m unittest test.test_main
```
### Running all tests
In the `codes` directory, runs command:
```sh
$ python -m unittest -s test
```