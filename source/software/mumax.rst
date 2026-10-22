.. _mumax:

mumax3 and mumax+
=================

mumax3 and mumax+ are programs for simulating magnetic materials (micromagnetics),
developed by the DyNaMat group at Ghent University. Both use a graphics card (GPU) to
run simulations quickly, so they only work on Buddy's GPU nodes, not on the login nodes.

.. list-table::
   :header-rows: 1
   :widths: 15 15 30 40

   * - Program
     - Version
     - You write simulations as
     - Module to load
   * - mumax3
     - 3.12
     - ``.mx3`` script files
     - ``mumax3/3.12-CUDA-12.6.0``
   * - mumax+
     - 1.2.1
     - Python scripts
     - ``mumaxplus/1.2.1-gfbf-2025a``

For more on loading software, see :doc:`/general/lmod`. For more on submitting jobs, see
:doc:`/general/slurm` and :doc:`/general/Job-Composer`.


mumax3 Example Script
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: slurm_bash

   #!/bin/bash
   #SBATCH --job-name=mumax3
   #SBATCH --partition=gpu
   #SBATCH --gres=gpu:1
   #SBATCH --cpus-per-task=10
   #SBATCH --time=02:00:00
   #SBATCH --output=mumax3-%j.out

   ### Of the batch options, it is only recommended to change "--job-name", "--time",
   ### and "--output". Any other modifications may result in an error.

   ### If using the job composer, you will need to upload your .mx3 file to the job
   ### script's folder. You can do this by clicking on "edit files" and then uploading
   ### your .mx3 file.

   #Load mumax3 module
   module load mumax3/3.12-CUDA-12.6.0

   #Run mumax3. Change "my_simulation.mx3" to the name of your input file.
   #-http "" turns off mumax3's browser interface, which can't be reached from a job.
   mumax3 -http "" my_simulation.mx3

   #Optional: turn the magnetization snapshots into PNG images.
   mumax3-convert -png my_simulation.out/*.ovf

Your results appear in a folder named after your input file, for example
``my_simulation.out/``. It contains:

- ``table.txt``: values recorded over time
- ``.ovf`` files: snapshots of the magnetization
- ``references.bib``: the papers to cite for your simulation


mumax+ Example Script
^^^^^^^^^^^^^^^^^^^^^

mumax+ simulations are Python scripts.

.. code-block:: slurm_bash

   #!/bin/bash
   #SBATCH --job-name=mumaxplus
   #SBATCH --partition=gpu
   #SBATCH --gres=gpu:1
   #SBATCH --cpus-per-task=10
   #SBATCH --time=02:00:00
   #SBATCH --output=mumaxplus-%j.out

   ### Of the batch options, it is only recommended to change "--job-name", "--time",
   ### and "--output". Any other modifications may result in an error.

   ### If using the job composer, you will need to upload your .py file to the job
   ### script's folder. You can do this by clicking on "edit files" and then uploading
   ### your .py file.

   #Load mumax+ module
   module load mumaxplus/1.2.1-gfbf-2025a

   #Jobs have no screen, so draw plots straight to files.
   export MPLBACKEND=Agg

   #Run mumax+. Change "my_simulation.py" to the name of your script.
   python my_simulation.py

.. tip::

   Save plots to files with ``plt.savefig("plot.png")`` instead of ``plt.show()``.

mumax+ can use single or double precision. See the
`mumax+ precision tutorial <https://mumax.github.io/plus/tutorial/precision.html>`__.


Learning More
^^^^^^^^^^^^^

- mumax3: `examples <https://mumax.github.io/examples.html>`__ and
  `API reference <https://mumax.github.io/api.html>`__
- mumax+: `tutorials <https://mumax.github.io/plus/tutorial.html>`__ and
  `examples <https://mumax.github.io/plus/examples.html>`__


Citing
^^^^^^

- **mumax3:** cite the papers listed in ``references.bib`` in your output folder.
- **mumax+:** cite
  `mumax+: extensible GPU-accelerated micromagnetics and beyond
  <https://www.nature.com/articles/s41524-025-01893-y>`__.

If a job fails or you need a different version, please email hpc@uco.edu.
