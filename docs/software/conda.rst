Anaconda 
========

Example Script
^^^^^^^^^^^^^^

.. code-block:: slurm_bash

    #!/bin/bash
    #SBATCH --job-name=my-conda-job
    #SBATCH --output=%j-my-conda-job.out
    #SBATCH --nodes=1
    
    ### USAGE:
    # 1. Replace your_environment and your_file 
    # 2. Submit job
    
    ### Load modules
    module purge # unload all modules
    module load Anaconda3/2020.11 # load anaconda
    
    ### Setup
    # setup and activate conda environment
    source ~/.bashrc # load .bashrc file to setup conda path
    conda activate your_environment # activate environment
    
    ### Run
    # The -u option forces python output to be unbuffered. Useful for debugging.
    python3 -u your_file


