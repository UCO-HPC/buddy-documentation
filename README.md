# Documentation for UCO's Buddy cluster
Documentation built with Sphinx and run on ReadTheDocs at [Buddy Docs](https://buddy-docs.readthedocs.io/en/latest/)

## Development

### Local development
1. Clone the repository
2. Edit files in the docs directory
3. From the docs directory run `` make clean && make html `` to rebuild docs
4. View changes with firefox with `` firefox _build/html/index.html & ``

### Apply changes
1. Make sure generated docs reflect the most recent changes `` make clean && make html ``
2. Commit and push to github
3. Changes will be reflected in [Buddy Docs](https://buddy-docs.readthedocs.io/en/latest/) between 2 and 20 miutes

## Future Topics:
- Edicate/Rules/Operating procedures
  - Don’t run long jobs on head node
- Buddy structure
  - Types and numbers of nodes
- running on different nodes
  - ssh
  - slurm job
  - open ondemand?
- Github on buddy
  - copy ~/.ssh/cluster.pub add to github ssh keys
- Conda on buddy
  - Installation
  - Basic usage
    - Activate Anaconda3 module
  - Example slurm script 
- Classes on buddy
