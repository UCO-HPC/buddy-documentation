Cluster Usage: Guidelines and Etiquette
=======================================

General Etiquette
-----------------
The cluster is a shared resource which we hope will be heavily utilized by anyone who could make use of it. We encourage our users to take advantage of this resource while using judgment to avoid inconveniencing other users, damaging the cluster, or abusing it.

Guidelines
----------


1. Avoid running scripts directly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   Buddy uses slurm to schedule jobs and allocate resources. This allows us to ensure every user has enough resources for their application and everyone has the ability to uilize the cluster. Try to work within slurm to allow us to 

2. Avoid running jobs on the head node
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   If you are accessing buddy via a terminal and not using slurm (see guideline 1) you will initially be working on the head node (hostname buddy). The head node is meant to manage the cluster while compute nodes handle the workload. Please ssh into a compute node (hostname buddy-01,buddy-02,etc.).

3. Run jobs in an appropriate partition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


4. Avoid allocating unnecessary recources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   Feel free to allocate enough resources for your application but try not to allocate resources you are not going to need. If you require a large quantity of resources use the appropriate partition or contact administration

5. Avoid running unnessary jobs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   Prefer running multiple tasks within one job over spawning multiple jobs when possible

6. Avoid queueing an extreme number of jobs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   Try to allow enough room in the queue for other users to run their jobs. If you have an application that requires a large number of jobs use the appropriate partition or contact administration
