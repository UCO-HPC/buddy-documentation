# Documentation for UCO's Buddy cluster
Documentation built with Sphinx and run on ReadTheDocs at [Buddy Docs](https://buddy-docs.readthedocs.io/en/latest/)

## Development

### Local development
1. Clone the repository
2. Install requirements.txt
3. Edit files in the docs directory
4. From the docs directory run `` make clean && make html `` to rebuild docs
5. View changes with firefox with `` firefox _build/html/index.html & ``

### Apply changes
1. Make sure generated docs reflect the most recent changes `` make clean && make html ``
2. Commit and push to github
3. Changes will be reflected in [Buddy Docs](https://buddy-docs.readthedocs.io/en/latest/) between 2 and 20 miutes

### Project structure
1. index.rst is the home page
2. The quickstart, general, and software directors correspond to sections in the table of contents. Adding .rst pages to these directories will add new pages to that section
3. \_templates holds snippits of html which can be inserted into pages

## Future Topics:
- Edicate/Rules/Operating procedures
  - Don’t run long jobs on head node
- Buddy structure
  - Types and numbers of nodes
- Classes on buddy
