Slurm
=====

Terminology
---------------

Tasks
^^^^^
A task is a command which is run in parallel by slurm using srun. Tasks can be used to run more than one command at the same time instead of one after the other, increasing performance

Partitions
^^^^^^^^^^
Partitions are an organizational structure in slurm which allows nodes to be grouped together and for certain options and restrictions to be placed on them. We have a few partitions on Buddy:

.. note::
   this information can be found using the sinfo command in the terminal

=============    ==============    ===============================================================
    Name          Time limit                             Description
=============    ==============    ===============================================================
general          5 days            Used for most jobs
general-long     30 days           Used for jobs that are expected to run for a long time
high-mem         5 days            Used for jobs which are expected to have high memory usage
high-mem-long    30 days           Used for long jobs which are expected to have high memory usage
gpu              5 days            Used for gpu jobs
gpu-long         30 days           Used for gpu jobs which are expected to run for a long time
testing          2 days            Reserved for our internal testing
=============    ==============    ===============================================================

We recommend that you use the partition that is most appropriate to your application. 

Cores
^^^^^
Each node has 20 cores so the product of --tasks-per-node and --cpus-per-task should not exceed 20

Commands
--------
sbatch          used allocate resource and run the given script using slurm
srun            used withing an sbatch file to run a command as a parallel task
smap            displays the jobs currently running on the cluster
sinfo           displays information about down and running nodes aswell as partition information

Sbatch Parameters
-----------------
Sbatch parameters are used to control the way jobs are submitted and run on buddy

Common sbatch parameters
^^^^^^^^^^^^^^^^^^^^^^^^

+-------------------+---------------------------+---------------------------------+------------------------------------------------------+
|      Name         |   Environment variables   |             Default             |                    Description                       |
+===================+===========================+=================================+======================================================+
| -J,--job-name     | SLURM_JOB_NAME            | script name or "sbatch"         | the name of your job                                 |
+-------------------+---------------------------+---------------------------------+------------------------------------------------------+
| -o,--output       | N/A                       | "slurm-%j.out"                  | file to dump standard output of program              |
+-------------------+---------------------------+---------------------------------+------------------------------------------------------+
| -e,--error        | N/A                       | "slurm-%j.out"                  | file to dump standard error of program               |
+-------------------+---------------------------+---------------------------------+------------------------------------------------------+
| -n,--ntasks       | N/A                       | 1 unless --cpus-per task is set | the maximum number of tasks sbatch should allocate   |
|                   |                           |                                 | resources for                                        |
+-------------------+---------------------------+---------------------------------+------------------------------------------------------+
| -N,--nodes        | SLURM_JOB_NUM_NODES       | enough nodes to satisfy the -n  | the number of nodes to allocate. A minimum and       |
|                   |                           | and -c options                  | maximum can also be set like: --nodes=10-12          |
+-------------------+---------------------------+---------------------------------+------------------------------------------------------+
| -c,--cpus-per-task| SLURM_CPUS_PER_TASK       | one processor per task          | the number of cpus to allocate for each task         |
+-------------------+---------------------------+---------------------------------+------------------------------------------------------+
| --ntasks-per-node | SLURM_TASKS_PER_NODE      | ?                               | the number of tasks to allocate for on each node     |
+-------------------+---------------------------+---------------------------------+------------------------------------------------------+
| -p,--partition    | SBATCH_PARTITION          | general                         | the partition to run the job in                      |
+-------------------+---------------------------+---------------------------------+------------------------------------------------------+
| -t,--time         | SBATCH_TIMELIMIT          | max time for partition          | the maximum amount of time the job is allowed to run |
+-------------------+---------------------------+---------------------------------+------------------------------------------------------+

