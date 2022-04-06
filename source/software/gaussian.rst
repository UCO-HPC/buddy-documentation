Gaussian
========

Example Script
^^^^^^^^^^^^^^

.. code-block:: slurm_bash

   #!/bin/bash
   #SBATCH --job-name=g16
   #SBATCH --nodes=2
   #SBATCH --cpus-per-task=20
   #SBATCH --output=g16-%j.out
   #SBATCH --partition=general
   
   ### Of the batch options, it is only recommnded to change "--job-name", "--nodes", and
   ### "--output". Any other modifications may result in an error.
   
   ### It is only recommneded to change the input file in the Gaussian command. If needed
   ### more g16 options can be added.
   
   ### If using the job composer, you will need to upload your input files to the job 
   ### script's folder. You can do this by clicking on "edit files" and then uploading
   ### your com file. 
   
   #Load Gaussian module
   module load Gaussian/g16
   
   #Gaussian scratch directory.
   export GAUSS_SCRDIR=/home/$USER/.gaustmp/$SLURM_JOBID
   mkdir -p $GAUSS_SCRDIR
   
   #Stop OpenMP from interfering with Gaussian's thread mechanism.
   export OMP_NUM_THREADS=1

   #Prepare node list for Linda
   for n in `scontrol show hostname | sort -u`; do
   echo ${n}
   done | paste -s -d, > snodes.$SLURM_JOBID
   
   #Run Gaussian. It is recommended to only change the input file here. If needed you can
   #raise the memory up to 60GB, but doing so may result in an error.
   g16 -m=40gb -p=${SLURM_CPUS_PER_TASK} -w=`cat snodes.$SLURM_JOBID` your_file_name.com

   #Clean up nodes list
   rm snodes.$SLURM_JOBID

