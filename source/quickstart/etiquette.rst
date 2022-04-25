Cluster Usage: Rules and Guidelines
===============================================

General Etiquette
-----------------
The cluster is a shared resource which we hope will be heavily utilized by anyone who could make use of it. We encourage users to take advantage of this resource while using judgment to avoid inconveniencing other users, overburdening the cluster, or abusing it.


Rules
-----
There are a few rules that must be followed to prevent overburdening or abusing the cluster.

1. Do not store sensative information on the cluster
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   Buddy is not yet HIPAA compliant. Do not store student grades, individually identifiable health information, or other such sensative information on the cluster at this time.

2. Do not abuse cluster resources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   Buddy is intended to support research and learning. Do not use the cluster to mine cryptocurrency, crack passwords, spam emails, or other such intensive and inappropriate activity.


Guidelines
----------
Here are a few guidelines for being considereate on the cluster. If you have any questions please contact administration.

1. Avoid running scripts directly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   Buddy uses slurm to schedule jobs and allocate resources. This allows us to ensure every user has enough resources for their application and everyone has the ability to uilize the cluster. Try to work within slurm to allow us to keep buddy healthy and usable for everyone.

2. Avoid running jobs on the head node
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   If you are accessing buddy via a terminal and not using slurm (see guideline 1) you will initially be working on the head node (hostname buddy). The head node is meant to manage the cluster while compute nodes handle the workload. Please ssh into a compute node (hostname buddy-01,buddy-02,etc.).

3. Use globus to transfer large files onto the cluster
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   While it is acceptable to use open ondemand, sftp, or scp to transfer data onto the cluster, if the data is over a certain size these methods can overburden the cluster causing a slowdown for all other users. For large files, be sure to utilize our DTNs and Globus. See the :doc:`data transfer </general/data_transfer>` section for more information.

4. Run jobs in an appropriate partition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   Slurms jobs on Buddy are run within partitions that are optimized for different use cases. For most applications the general partition is appropriate, however, if your job requires a lot of memory use a high-mem partition or if you exptect your job will need to run for longer than 5 days use a long partition. See :doc:`slurm partitions </general/slurm>` for more information.

5. Avoid allocating unnecessary recources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   Feel free to allocate enough resources for your application but try not to allocate resources you are not going to need. If you require a large quantity of resources use the appropriate partition or contact administration.

6. Avoid running unnessary jobs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   Prefer running multiple tasks within one job over spawning multiple jobs when possible.

7. Avoid queueing an extreme number of jobs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   Try to allow enough room in the queue for other users to run their jobs. If you have an application that requires a large number of jobs use the appropriate partition or contact administration.

8. Be aware of software licenses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   Some software on buddy requires a software license such as COMSOL. There are only so many licenses which means only a few users can access that software at a time. Keep this in mind and try to give others an opportunity to access the software as well.
