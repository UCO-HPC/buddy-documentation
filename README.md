# Buddy Documentation

[![GitHub Release](https://img.shields.io/github/v/release/UCO-HPC/buddy-documentation?style=flat-square)](https://github.com/UCO-HPC/buddy-documentation/blob/main/CHANGELOG.md)
[![GitHub License](https://img.shields.io/github/license/UCO-HPC/buddy-documentation?style=flat-square)](https://opensource.org/licenses/MIT)

A repository to host Buddy's source code for our [Read The Docs] page. Documentation is built with [Sphinx].

## Prerequisites

The following should be installed on your OS

- [Python 3]
- [pip] package manager
- Firefox or Chrome

Installing required Python packages with pip

``` pip install -r requirements.txt ```

[Python 3]: https://biodiversityinformatics.amnh.org/open_source/maxent/
[pip]: https://openjdk.java.net/

## Compiling documentation

The make command will be run from the project root directory. Resulting files will be placed in build

``` make clean html ``` 

Resulting web page can be opened from `` build/html/index.html ``

## Project Structure

```
Project Root
|  Makefile (Make file)
|  make.bat (Windows make file)
|  README.md (Project README)
|  requirements.txt (Names of required Python packages)
|
|--build (Built files)
|  | html (Generated HTML)
|  | doctrees (Binary RST Cache)
|
|--source (Source Files)
   | index.rst (Website index)
   | conf.py (Website configuration)

```
## License


* Please note that this application is specific to our university. Please feel free to copy and use as needed according to the associated license. Code, documentation, and content are licensed under MIT (see LICENSE.txt) at this time. License is subject to change without notice. 
* 
* [Read The Docs] and it's source code are copyrighted by Read The Docs Inc. and it's constributers

# Documentation for UCO's Buddy cluster
Documentation built with Sphinx and run on ReadTheDocs at [Buddy Docs](https://buddy-docs.readthedocs.io/en/latest/)




### Project structure
1. index.rst is the home page
2. The quickstart, general, and software directors correspond to sections in the table of contents. Adding .rst pages to these directories will add new pages to that section
3. source/\_templates holds snippits of html which can be inserted into pages
