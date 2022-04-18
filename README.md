# Documentation for UCO's Buddy cluster
Documentation built with Sphinx and run on ReadTheDocs at [Buddy Docs](https://buddy-docs.readthedocs.io/en/latest/)

## Development

### Local development
1. Clone the repository
2. Install requirements.txt
3. From the project directory run `` make clean html `` to rebuild docs
4. View changes with firefox with `` firefox build/html/index.html & ``

### Apply changes
1. Make sure generated docs reflect the most recent changes `` make clean html ``
2. Commit and push to github
3. Changes will be reflected in [Buddy Docs](https://buddy-docs.readthedocs.io/en/latest/) between 2 and 20 miutes

### Project structure
1. index.rst is the home page
2. The quickstart, general, and software directors correspond to sections in the table of contents. Adding .rst pages to these directories will add new pages to that section
3. source/\_templates holds snippits of html which can be inserted into pages
