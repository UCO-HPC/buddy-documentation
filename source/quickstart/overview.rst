Overview
========

.. Part of this page is adapted from another page-> https://www.uco.edu/cms/research-centers/creic/buddy-supercomputer

About
^^^^^ 
Buddy a 37-node supercomputer managed by `CREIC <https://www.uco.edu/cms/research-centers/creic/>`_ and funded by the National Science Foundation. You can see some details `on the NSF site <https://www.nsf.gov/awardsearch/showAward?AWD_ID=1429702>`_.

Buddy is being used for both research and education. Research includes projects on particle transport, micromixing, stochastic modeling, ecological modeling, bio-informatics and spread of disease.

Connecting to Buddy
^^^^^^^^^^^^^^^^^^^
If you are a faculty member or student working on a project at UCO (or with a UCO faculty member), you can access Buddy. Send an email to hpc@uco.edu to request an account.

Once you have an account, you can access Buddy from anywhere using a browser through https://buddy.uco.edu. We use the Open OnDemand software which makes it easy to setup jobs and use interactive graphical user interfaces. You can also access Buddy remotely through a terminal using something like ssh.

Linux on Buddy
^^^^^^^^^^^^^^
Buddy uses linux as its operating system. Many of the day to day operations are similar to other operating systems like Windows and MacOS. For more information see: :doc:`files` and :doc:`../general/terminal`.

What is a Slurm Job?
^^^^^^^^^^^^^^^^^^^^
A job is a convenient way to execute code on Buddy. A job script is created which sets up the environment, loads relevant modules, and executes one or several commands. When the job is run with slurm it is placed in a queue until the requested resources are available and then it is executed. For more information about SLURM jobs see: :doc:`basic_job`, :doc:`../general/slurm`, and :doc:`../general/modules`.
