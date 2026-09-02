Jupyter/Python
==============

The **Jupyter** interactive app launches a JupyterLab server on a Buddy compute
node and connects your browser to it. You reach it from OnDemand at
`ondemand.hpc.uco.edu <https://ondemand.hpc.uco.edu>`_ under *Interactive Apps* → *Programming* →
*Jupyter*.

You do not have to build a software stack yourself. The app is driven by an
**Environment** selector: each option loads a tested, mutually-compatible set of
Lmod modules, so there is no need to match FOSS/GCC/Python toolchains by hand.

.. image:: /_static/img/ondemand_jupyter_python.png
  :width: 100%
  :align: center
  :alt: The Buddy OnDemand Jupyter launch form, with the Python - Data Science environment selected

|

Launch Options
--------------

Queue
~~~~~

The queue your session will run on. ``general`` is right for most work. Pick a
**GPU queue** if you want the CUDA build of PyTorch — see
:ref:`jupyter-pytorch-gpu` below.

Cores and memory are set automatically from the queue you pick, so there is no
core count to choose. A GPU session is given one GPU plus a matching slice of
the node; a non-GPU session is given the whole node.

Number of hours
~~~~~~~~~~~~~~~

How long the session may run, from 1 to 48 hours. The session is killed when the
time runs out, so ask for a little more than you think you need. If you need
longer than 48 hours, use a Slurm batch script instead of an interactive
session.

Environment
~~~~~~~~~~~

The software stack to load. The available choices are:

.. list-table::
   :widths: 25 45 30
   :header-rows: 1

   * - Environment
     - What it loads
     - JupyterLab versions offered
   * - **Python**
     - JupyterLab and its Python, and nothing else.
     - all seven
   * - **Python — Data Science**
     - Adds ``Python-Data-Science``: NumPy, SciPy, pandas, matplotlib and SymPy,
       built for the same toolchain.
     - all except 4.0.5
   * - **PyTorch / Deep Learning**
     - Adds PyTorch. On a GPU queue this is the CUDA build; on any other queue
       it is the CPU build.
     - 4.0.5 and 4.2.5 on a GPU queue; those plus 4.2.0 on a CPU queue
   * - **R**
     - Adds ``IRkernel``, giving you an R kernel inside JupyterLab.
     - 3.5.0, 4.0.5, 4.2.5
   * - **C / C++**
     - Adds ``jupyter-c-kernel``, a C/C++ kernel.
     - 3.5.0
   * - **SageMath**
     - Adds SageMath 10.4 with its JupyterLab integration.
     - 4.2.0
   * - **Course Module**
     - One instructor-built course environment, loaded on its own. See
       :ref:`jupyter-course-modules`.
     - n/a — the module brings its own
   * - **Custom**
     - Nothing. Runs your own **Launch Commands** instead. See
       :ref:`jupyter-custom`.
     - n/a

Version
~~~~~~~

The JupyterLab build, which also fixes the Python version that comes with it:

.. list-table::
   :widths: 30 25 25
   :header-rows: 1

   * - JupyterLab
     - Python
     - GCCcore
   * - 4.4.9
     - 3.13.5
     - 14.3.0
   * - 4.4.4
     - 3.13.1
     - 14.2.0
   * - 4.2.5
     - 3.12.3
     - 13.3.0
   * - 4.2.0
     - 3.11.5
     - 13.2.0
   * - 4.0.5
     - 3.11.3
     - 12.3.0
   * - 3.5.0
     - 3.10.4
     - 11.3.0
   * - 3.0.16
     - 3.9.5
     - 10.3.0

The list is filtered to the versions that actually work with the environment
you picked (and, for PyTorch, with the queue you picked), so a combination that
cannot be built is simply not offered. Unless you have a reason to need an older
Python, take the newest version on offer.

Additional modules
~~~~~~~~~~~~~~~~~~

Optional. Extra modules to load on top of the chosen environment, separated by
spaces — for example ``scikit-learn/1.6.1-gfbf-2024a``. **Match the toolchain**
of the environment you selected; the *Currently Selected Modules* panel tells
you which toolchain that is. Loading a module from a different toolchain is the
most common cause of import errors in a session.

See :doc:`Using_Modules` for how to find module names with ``module spider``.

Currently Selected Modules
~~~~~~~~~~~~~~~~~~~~~~~~~~

Below the form is a live summary of exactly what your current selection will
load: the GCCcore and FOSS/GFBF toolchain, the Python and JupyterLab versions,
and the headline package versions (NumPy, SciPy, pandas, matplotlib, and any
R / PyTorch / CUDA / SageMath). Check it before launching — it is the quickest
way to confirm you are getting the versions you expect.

The panel is hidden for the **Custom** environment, because the app has no way
to know what your own commands will load.

Saved Settings
~~~~~~~~~~~~~~

Tick **Save settings**, give the configuration a name, and it appears in the
*Saved Settings* list on the left of the form. This is worth doing for any
setup you launch repeatedly — particularly a **Custom** configuration, so you
do not have to retype the launch commands each time.

.. _jupyter-pytorch-gpu:

Using a GPU
-----------

To get GPU-accelerated PyTorch:

1. Select a **GPU queue**.
2. Select the **PyTorch / Deep Learning** environment.
3. Select a version the GPU queue offers (4.2.5 or 4.0.5).

Selecting a GPU queue is what causes the CUDA build to be loaded; picking the
PyTorch environment on a non-GPU queue silently gives you the CPU build, which
will run but will not see a GPU. Confirm your choice in the *Currently Selected
Modules* panel — the CUDA version is listed there when the CUDA build is
selected.

The JupyterLab 4.2.5 CUDA build also loads ``torchvision``, ``diffusers``,
``Transformers`` and ``matplotlib`` alongside PyTorch.

Buddy's GPUs include some older cards, and Buddy's PyTorch modules are built
specifically to work with them. A PyTorch you install yourself from PyPI may
well refuse to run on those cards, so prefer this environment over installing
PyTorch into your own environment.

.. _jupyter-course-modules:

Course Modules
--------------

If your instructor has had a course environment built for your class, select
**Course Module** and pick it from the list. A course module is a single module
containing the complete stack for that course, including its own JupyterLab.

It is loaded **on its own** — no other JupyterLab, no environment extras, and
nothing from the *Additional modules* field. That is deliberate: it guarantees
every student in the class gets exactly the stack the instructor specified. The
Version and Additional modules fields are therefore hidden when Course Module is
selected.

.. image:: /_static/img/ondemand_jupyter_course.png
  :width: 85%
  :align: center
  :alt: The Jupyter form with a Course Module selected

|

Instructors: to have a course environment added to this list, email
hpc@uco.edu. The dropdown is built by scanning Buddy's module tree, so once the
module is published it appears on its own.

.. _jupyter-custom:

Custom Environments
-------------------

**Custom** is the escape hatch: instead of loading a curated stack, the app runs
whatever you put in the **Launch Commands** box, and then starts JupyterLab.

The one thing your commands must do is **put a** ``jupyter-lab`` **executable on
the** ``PATH``. If they do not, the session starts, fails to open its port, and
times out. The app runs ``module purge`` before your commands, so you are
starting from a clean environment.

.. image:: /_static/img/ondemand_jupyter_custom.png
  :width: 85%
  :align: center
  :alt: The Jupyter form with the Custom environment and Launch Commands

|

The two recipes below cover what most people need. The simpler one names a
combination of modules that no curated environment offers; the other, in
:ref:`jupyter-uv`, launches JupyterLab from one of your own uv environments.

A combination of modules
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   module load JupyterLab/4.2.5-GCCcore-13.3.0
   module load IRkernel/1.3.2-gfbf-2024a-R-4.4.2
   module load SciPy-bundle/2024a-gfbf-2024a

.. _jupyter-uv:

Launching JupyterLab from a uv environment
------------------------------------------

The most useful thing to do with **Custom** is to launch JupyterLab from one of
your own :doc:`uv <uv>` environments, so that your notebooks run against exactly
the packages your project pins.

**Your uv environment must contain the** ``jupyterlab`` **package.** This is the
step people miss. ``jupyterlab`` is what provides the ``jupyter-lab``
executable; without it in the environment, the session will never start.

Set the environment up once, from a terminal (either the OnDemand *Buddy
Terminal* app or an SSH session):

.. code-block:: bash

   module load uv

   cd ~/my-project

   # Add JupyterLab to the project alongside whatever else it needs.
   uv add jupyterlab

   # jupyterlab pulls in ipykernel, so the default "Python 3 (ipykernel)"
   # kernel in the session will be this project's environment.

Then, in the Jupyter app, select the **Custom** environment and put this in
**Launch Commands**:

.. code-block:: bash

   module load uv
   cd ~/my-project
   uv sync --frozen
   source .venv/bin/activate

Adjust ``~/my-project`` to your project's path. Line by line:

* ``module load uv`` makes ``uv`` available. (If you installed uv yourself
  rather than using the module, use ``export PATH="$HOME/.local/bin:$PATH"``
  instead.)
* ``uv sync --frozen`` brings ``.venv`` into line with your ``uv.lock`` without
  re-resolving it, so the session gets precisely the pinned versions. You can
  drop this line if you would rather manage the environment by hand.
* ``source .venv/bin/activate`` puts the environment's ``bin`` directory —
  including ``jupyter-lab`` — at the front of the ``PATH``. This is the line
  that makes the whole thing work.

If you are not using a project with a lock file, a plain virtual environment
works just as well; activate it by absolute path and skip the sync:

.. code-block:: bash

   module load uv
   source ~/envs/myenv/bin/activate

Save the configuration with **Save settings** so you can relaunch it in one
click.

A few things to know
~~~~~~~~~~~~~~~~~~~~

* **The file browser always opens at your home directory**, whatever your launch
  commands do. Navigate to your project folder from there.
* **Add packages from a terminal, not from a notebook.** Use ``uv add <package>``
  in a terminal (or a JupyterLab terminal, after activating the environment) and
  then restart the kernel. A ``!pip install`` inside a notebook cell will not go
  through uv and will not be recorded in your lock file.
* **Extra kernels are optional.** Because JupyterLab itself is running from your
  environment, the default kernel already *is* your environment. You only need
  ``ipykernel install`` if you want to offer several environments as separate
  kernels in one session.
* **Prefer the curated environments for GPU work.** A PyTorch installed by uv
  from PyPI is not built for Buddy's older GPUs. If you need a GPU, use the
  **PyTorch / Deep Learning** environment, or see the layering recipe in
  :ref:`uv-advanced-modules`.

Troubleshooting
---------------

**The session sits in "Starting" and then fails.**
  Most often the environment does not provide ``jupyter-lab``. With a uv
  environment, check that ``jupyterlab`` is in the project (``uv add
  jupyterlab``). Open the session card's output log in
  *My Interactive Sessions* to see the error.

**A package imports at the terminal but not in the notebook.**
  The kernel is not running the environment you think it is. In a notebook cell,
  run:

  .. code-block:: python

     import sys; print(sys.executable)

  and check that the path is the one you expect.

**Import errors after adding something to Additional modules.**
  The extra module's toolchain almost certainly does not match the
  environment's. Compare it against the toolchain shown in the *Currently
  Selected Modules* panel.
