Creating a Basic Job
====================

.. code-block:: slurm_bash

    #!/bin/bash
    #SBATCH --job-name=myjob #name of job
    
    # The relative path output and error files. %j is replaced with job number
    #SBATCH --output=%j-myjob.out
    #SBATCH --error=%j-myjob.err
    
    #SBATCH --partition=general
    #SBATCH --nodes=1
    #SBATCH --cpus-per-task=10
    #SBATCH --ntasks=20
    #SBATCH --ntasks-per-node=20
    #SBATCH --time=48:00:00 # the maximum amount of time this job is allowed to run
    
    ###Load wanted modules herescikit-learn/0.20.3-foss-2019a
    # use "module spider [package]" in the terminal to search for available modules
    # it is usually a good idea to unload all modules first with: module purge
    # eg. :
    # module purge
    # module load scikit-learn/0.20.3-foss-2019a
    
    ###Your exectuable here
    # eg. python hello_world.py
    
    echo "Hello World"

