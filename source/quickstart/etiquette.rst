Cluster Usage: Rules and Guidelines
===============================================

General Etiquette
-----------------
The cluster is a shared resource, and we encourage all who can benefit from it to make full use of it. At the same time, we ask users to be mindful by avoiding unnecessary strain, disruption to others, or misuse so that the system can remain reliable and accessible for everyone.

Rules
-----
There are a few rules that must be followed while using the cluster:

1. Do not store sensitive information on the cluster
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   Buddy is not yet HIPAA compliant. Do not store student grades, individually identifiable health information, or other such sensitive information on the cluster at this time.

2. Do not abuse cluster resources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   Buddy is intended to support research and learning. Do not use the cluster to mine cryptocurrency, crack passwords, spam emails, or other such intensive and inappropriate activity. We'll know...


Guidelines
----------
We have outlined some best practices and general guidelines when it comes to running jobs on the cluster. If you have any questions, please contact hpc@uco.edu.

1. Avoid running scripts directly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   Buddy uses slurm to schedule jobs and allocate resources. This allows us to ensure every user has enough resources for their application and everyone has the ability to uilize the cluster. Try to work within slurm to allow us to keep buddy healthy and usable for everyone.

2. Avoid running jobs on the ssh nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   If you are accessing buddy via a terminal and not using slurm (see guideline 1) you will initially be working on one of the ssh nodes (hostname ssh1 or ssh2). The ssh nodes act as an entry point to the cluster while compute nodes handle the submitted workloads.

3. (Coming Soon) Use globus to transfer large files onto the cluster
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   While it is acceptable to use open ondemand, sftp, or scp to transfer data onto the cluster, if the data is over a certain size these methods can overburden the cluster causing a slowdown for all other users. For large files, be sure to utilize our DTNs and Globus. See the :doc:`data transfer </general/data_transfer>` section for more information.

4. Run jobs in an appropriate partition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   Slurms jobs on Buddy are run within partitions that are optimized for different use cases. For most applications the general partition is appropriate, however, if your job requires a lot of memory use a high-mem partition or if you exptect your job will need to run for longer than 5 days use a long partition. See :doc:`slurm partitions </general/slurm>` for more information.

5. Avoid allocating unnecessary recources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   Feel free to allocate enough resources for your application but try not to allocate resources you are not going to need. A good rule of thumb is to use a maximum of half the available nodes in any partition. If you require a large quantity of resources use the appropriate partition or contact hpc@uco.edu.

6. Avoid running unnessary jobs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   Prefer running multiple tasks within one job over spawning multiple jobs when possible.

7. Avoid queueing an extreme number of jobs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   Try to allow enough room in the queue for other users to run their jobs. If you have an application that requires a large number of jobs use the appropriate partition or contact hpc@uco.edu.

8. Be aware of software licenses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   Some software on Buddy requires a software license, such as COMSOL. There are only so many licenses which means only a few users can access that software at a time. Keep this in mind and try to give others an opportunity to access the software as well.
