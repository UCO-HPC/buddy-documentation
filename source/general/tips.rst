Tips and Tricks
===============

Slurm
-----
Use ``%j-PROJECT.out`` for output files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When a slurm job is submitted, the job number is printed to the screen. With this naming scheme it is easy to see which outfile is which and if you're using a terminal you can copy the job number, paste it in the terminal window, and press tab to autofill the rest of the file name.

Create general scripts
~~~~~~~~~~~~~~~~~~~~~~
If you often run the same command with different input files as is common with python, create a general slurm script that takes in a file path and passes it  to that command. For example:

.. code-block:: slurm  
  :caption: PROJECT_DIR/scripts/job.sh 

  #!/bin/bash
  #SBATCH --job-name=autoencoder
  #SBATCH --nodes=1
  #SBATCH --cpus-per-task=16
  #SBATCH --output=script_outputs/%j-autoencoder.out
  #SBATCH --partition=general
  
  # script from commandline
  script=$1
  
  # load required packages
  module purge
  module load TensorFlow/2.6.0-foss-2021a
  module load scikit-learn/0.24.2-foss-2021a
  module load matplotlib/3.4.2-foss-2021a
  
  # run script
  python3 -u $script
  echo Finished

Then run ``sbatch scripts/job.sh PYTHON_SCRIPT`` from your project directory. This method can also be used to pass arguments to commands as anything after ``sbatch job.sh`` is passed to the script.

Python
------
Use the ``-u`` flag
~~~~~~~~~~~~~~~~~~~
By default python bufferes its outputs. If you use ``print()`` for debugging, it may be helpful to have output displayed imediately instead of being buffered
