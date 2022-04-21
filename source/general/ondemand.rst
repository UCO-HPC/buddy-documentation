Open OnDemand
=============

Open OnDemand is our new and improved interface for accessing HPC resources on Buddy. Open OnDemand is developed and maintained by Ohio Supercomputing Center. You can access it by visiting https://buddy.uco.edu. This document describes how to access and use OnDemand and it's services.

.. image:: /_static/img/ondemand_home.png
  :width: 100%
  :alt: Buddy OnDemand Home Page

Access and Login
****************

OnDemand can be accessed by visiting https://buddy.uco.edu. You will login using the credentials provided by CREIC. If you do not already have an account, or you require a password reset, please email hpc@uco.edu for assistance. Please note that while the username may match yours at uco, this account is not connected to your UCO credentials.

.. image:: /_static/img/ondemand_login.png
  :width: 50%
  :align: center
  :alt: Buddy OnDemand Login Box 

|

Interactive Applications
************************

Buddy has a number of interactive applications available for use. You can access them via the interactive apps tab, or by clicking "My Interactive Sessions"

.. image:: /_static/img/ondemand_nav_interactive.png
  :width: 50%
  :align: center
  :alt: Buddy OnDemand Nav Interactive Apps

As an example, we will access Jupyter. Below is what the application will most likely look like. We will touch on each of the available options, including the advanced tab. 
 
.. image:: /_static/img/ondemand_buddy_jupyter.png
  :width: 75%
  :align: center
  :alt: Buddy OnDemand Nav Interactivie Apps

Queue
^^^^^

Allows you to select the queue your application will run on. General is typical for most jobs. GPU and High Memory are available for specialized work loads, but there are a limited number of nodes with these resources.

Number of Hours
^^^^^^^^^^^^^^^

This is the number of hours your interactive application will run for. Please note there is a 48 hour limit on all interactive app jobs. If you require longer runtimes, please utilize a SLURM script.

.. #TODO: Add link to SLURM script section 

Number of Cores
^^^^^^^^^^^^^^^

Number of cores for your job. You can reserve up to 20, but only use the minimum required. Two is typically best for classroom jobs, and most research jobs. Twenty will reserve the entire node for just that application. This should only be done when absolutely needed. 

Version
^^^^^^^

This selects the version of the application you wish to run. Most often, you will want to pick the latest version, unless you have some need that requires an older revision.

Additonal Modules
^^^^^^^^^^^^^^^^^

Additional modules can be added here. This utilizes LMOD, and will automatically load the user supplied list of modules. Please be sure your modules toolchain version matches the toolchain of your software version. You can read more in the module section about toolchains.

.. #TODO: Add a link to the module section

Other Options
^^^^^^^^^^^^^

Certain applications contain other options. For example, Jupyter let's you choose between a Lab or Notebook session. Jupyter also offers ready to select 

File Browser and Text Editor
****************************

Terminal Access
***************

Job Management
**************

Job Composer
************


