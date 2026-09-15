Python Environments with uv
===========================

`uv <https://docs.astral.sh/uv/>`_ is a fast Python package and project manager.
On Buddy it is the recommended way to manage your own Python packages: it
creates ordinary virtual environments, resolves dependencies in seconds, and can
record an exact, reproducible set of versions in a ``uv.lock`` file that you
commit alongside your code.

.. note::

   uv replaces the Anaconda/conda workflow previously documented here. If you
   have an existing conda environment, ``uv`` can read a ``requirements.txt``
   exported from it (``uv pip install -r requirements.txt``) to get you started.

Before you reach for uv, check whether Buddy already has what you need as a
module — see :doc:`Using_Modules`. Buddy's modules are compiled for Buddy's
hardware, which matters a great deal for anything that touches MPI, BLAS or the
GPUs. uv is for the packages that are *not* available as modules.

Getting uv
----------

Use the module
~~~~~~~~~~~~~~

uv is available as a module. Find the current name with:

.. code-block:: bash

   module spider uv

then load it:

.. code-block:: bash

   module load uv

Check it works:

.. code-block:: bash

   uv --version

Installing your own copy
~~~~~~~~~~~~~~~~~~~~~~~~

If you need a newer uv than the module provides, you can install one into your
home directory. Buddy's login and compute nodes both have outbound internet
access, so the standalone installer works directly:

.. code-block:: bash

   curl -LsSf https://astral.sh/uv/install.sh | sh

This installs ``uv`` to ``~/.local/bin``. Add that directory to your ``PATH``
— the installer offers to edit your shell profile for you, or you can add this
line to ``~/.bashrc`` yourself:

.. code-block:: bash

   export PATH="$HOME/.local/bin:$PATH"

Open a new shell (or run ``source ~/.bashrc``) and confirm with ``uv --version``.

Update a self-installed uv with ``uv self update``. This does **not** work on the
module-provided uv, which is updated by HPC staff.

.. warning::

   Do not both load the module and install your own copy without deciding which
   one you want on your ``PATH``. Run ``which uv`` if you are unsure which one
   you are using.

Creating and Activating an Environment
--------------------------------------

The quickest way to get a working environment is ``uv venv``:

.. code-block:: bash

   cd ~/my-project

   # Create a virtual environment in ./.venv
   uv venv

   # Activate it
   source .venv/bin/activate

Once activated, your shell prompt is prefixed with the environment name and
``python`` refers to the environment's interpreter. Install packages into it
with ``uv pip install``:

.. code-block:: bash

   uv pip install numpy pandas matplotlib

Leave the environment with:

.. code-block:: bash

   deactivate

The environment is just a directory. Delete ``.venv`` to throw it away, and
recreate it whenever you need to; with uv this takes seconds rather than
minutes, so treat environments as disposable.

.. note::

   You do not strictly have to activate the environment. ``uv run <command>``
   runs a command inside the project's environment without activating anything,
   which is often more convenient in scripts. Activation is still the clearest
   approach for interactive work and is what the OnDemand Jupyter app needs —
   see :ref:`jupyter-uv`.

Choosing the Python Version
---------------------------

Letting uv provide Python
~~~~~~~~~~~~~~~~~~~~~~~~~

By default uv will download and manage a Python interpreter for you, entirely
independent of Buddy's module tree:

.. code-block:: bash

   # See what is available and what is already installed
   uv python list

   # Install a specific version
   uv python install 3.13

   # Build an environment on it
   uv venv --python 3.13

This is the simplest option and is a good default for pure-Python work.

Using a Python from the module tree
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If your environment needs to work alongside Buddy's modules — anything built
against Buddy's MPI, BLAS or CUDA — build it on a module-provided Python
instead, so the versions match:

.. code-block:: bash

   module load Python/3.13.5-GCCcore-14.3.0
   uv venv --python "$(which python3)"

Use ``module spider Python`` to see the versions available. Whichever Python you
pick, load the same module again whenever you use the environment, so the
interpreter the environment points at still exists on the ``PATH``.

Projects: ``pyproject.toml`` and ``uv.lock``
--------------------------------------------

``uv pip install`` is fine for quick experiments, but for anything you want to
reproduce later — or run on a compute node, or share with a collaborator — use
uv's project workflow. It records what you asked for in ``pyproject.toml`` and
the exact resolved versions of everything, direct and transitive, in
``uv.lock``.

Starting a project
~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   mkdir ~/my-project && cd ~/my-project
   uv init

``uv init`` creates a ``pyproject.toml``, a ``.python-version`` file and a stub
``main.py``. If you already have a directory of code, run ``uv init`` inside it.

Adding and removing packages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Add dependencies. This creates .venv if needed, resolves, installs,
   # and updates both pyproject.toml and uv.lock.
   uv add numpy pandas matplotlib

   # Pin a version, or a range
   uv add "scipy>=1.16"

   # Development-only dependencies
   uv add --dev pytest

   # Remove one
   uv remove matplotlib

You rarely need to call ``uv lock`` yourself — ``uv add``, ``uv remove``,
``uv sync`` and ``uv run`` all keep the lock file current. Call it explicitly
when you want to re-resolve without changing your requirements:

.. code-block:: bash

   # Re-resolve everything within the constraints in pyproject.toml
   uv lock --upgrade

   # Re-resolve just one package
   uv lock --upgrade-package numpy

Syncing an environment from the lock file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``uv sync`` makes ``.venv`` match ``uv.lock`` exactly — installing what is
missing and **removing anything that is not in the lock file**:

.. code-block:: bash

   # Bring .venv in line with uv.lock, updating the lock file first if
   # pyproject.toml has changed
   uv sync

   # Use uv.lock exactly as it stands; fail rather than re-resolve
   uv sync --frozen

Use ``--frozen`` anywhere you want the lock file treated as the source of truth
— in Slurm jobs, in a session you are trying to reproduce, and any time a
surprise version bump would be unwelcome.

To recreate the environment on another machine, or after deleting ``.venv``,
copy ``pyproject.toml`` and ``uv.lock`` across and run ``uv sync``. You will get
the identical set of versions.

.. tip::

   Commit ``pyproject.toml`` and ``uv.lock`` to :doc:`git </advanced/git>`.
   Do **not** commit ``.venv`` — ``uv init`` adds it to ``.gitignore`` for you.

Running code in the environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``uv run`` syncs the environment if needed and then runs a command inside it,
without activating anything:

.. code-block:: bash

   uv run python my_script.py
   uv run pytest

Using uv in a Shell or Slurm Script
-----------------------------------

The pattern in a batch script is the same as at the terminal, with two
additions: load the uv module explicitly (batch jobs do not read your
interactive shell setup the way you might expect), and ``cd`` to your project
directory.

With a project and a lock file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the recommended form. ``uv run --frozen`` guarantees the job runs the
exact versions in ``uv.lock``:

.. code-block:: slurm_bash
  :caption: ~/my-project/job.sh

   #!/bin/bash
   #SBATCH --job-name=my-uv-job
   #SBATCH --output=%j-my-uv-job.out
   #SBATCH --nodes=1
   #SBATCH --cpus-per-task=8
   #SBATCH --partition=general

   ### USAGE: sbatch job.sh
   ### Replace the project path and script name below.

   ### Set up uv
   module purge
   module load uv

   ### Move to the project (the directory holding pyproject.toml and uv.lock)
   cd "$SLURM_SUBMIT_DIR"

   ### Bring .venv in line with the lock file, without re-resolving.
   ### Safe to run every time; it is a no-op when nothing has changed.
   uv sync --frozen

   ### Run. The -u option forces unbuffered output, so print() lands in
   ### the .out file immediately instead of at the end of the job.
   uv run --frozen python -u my_script.py

   echo Finished

Submit it from the project directory with ``sbatch job.sh``.

With a plain virtual environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you built the environment with ``uv venv`` and have no lock file, activate it
by absolute path:

.. code-block:: slurm_bash
  :caption: ~/scripts/job.sh

   #!/bin/bash
   #SBATCH --job-name=my-uv-job
   #SBATCH --output=%j-my-uv-job.out
   #SBATCH --nodes=1
   #SBATCH --partition=general

   module purge
   module load uv

   source ~/my-project/.venv/bin/activate

   python -u ~/my-project/my_script.py

   echo Finished

Passing the script in as an argument
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As with any Slurm script, you can make the job generic and pass the Python file
in on the command line — see :doc:`/general/tips`:

.. code-block:: slurm_bash

   script=$1

   module purge
   module load uv
   cd "$SLURM_SUBMIT_DIR"
   uv run --frozen python -u "$script"

Then submit with ``sbatch job.sh my_script.py``.

.. _uv-advanced-modules:

Advanced: Layering uv on a Buddy Module
---------------------------------------

.. note::

   Most users do not need this. If you want PyTorch in a notebook, the OnDemand
   Jupyter app has a **PyTorch / Deep Learning** environment that already
   provides a build matched to Buddy's GPUs — see :doc:`jupyter_python`. Reach
   for the recipe below only when you need to add packages *on top of* a module
   that has no equivalent on PyPI.

Some of Buddy's GPUs are older cards, and modules such as PyTorch are built
specifically to support them. A PyTorch installed from PyPI by uv may refuse to
run on those cards. When you need extra packages alongside such a module, do not
reinstall the module's software — layer a virtual environment on top of it with
``--system-site-packages``, so the module's packages stay visible and uv only
adds what is missing:

.. code-block:: bash

   # Load the module stack you want to build on
   module purge
   module load PyTorch/2.7.1-foss-2024a-CUDA-12.8.0

   # Create an environment on that module's Python that can still see it
   uv venv --system-site-packages --python "$(which python3)"
   source .venv/bin/activate

   # Add only what the module does not provide
   uv pip install some-extra-package

   # Confirm you are still getting the module's PyTorch
   python -c "import torch; print(torch.__file__, torch.cuda.is_available())"

Two things to keep in mind:

* **Load the same modules every time.** The environment depends on them. Put the
  ``module load`` lines in your Slurm script or Jupyter launch commands right
  before you activate the environment.
* **Use** ``uv pip install`` **, not** ``uv add`` **/** ``uv sync`` **here.**
  ``uv sync`` manages ``.venv`` as a self-contained project environment and may
  rebuild it, dropping the link to the module's packages. The project workflow
  and the layering workflow do not mix well; pick one per environment.

Housekeeping
------------

uv keeps a download cache in ``~/.cache/uv`` so that repeated installs are near
instant. It grows over time. To see and manage it:

.. code-block:: bash

   uv cache dir      # where it lives
   uv cache prune    # remove entries no longer in use
   uv cache clean    # empty it entirely

To put the cache somewhere else, set ``UV_CACHE_DIR``. Keep it on the same
filesystem as your environments — uv hardlinks from the cache into ``.venv``,
which is what makes installs fast.

Common Commands
---------------

.. list-table::
   :widths: 45 55
   :header-rows: 1

   * - Command
     - Action
   * - ``uv venv``
     - Create a virtual environment in ``./.venv``.
   * - ``uv venv --python 3.13``
     - Create one on a specific Python version.
   * - ``source .venv/bin/activate``
     - Activate an environment in the current shell.
   * - ``deactivate``
     - Leave the active environment.
   * - ``uv pip install <pkg>``
     - Install into the active environment (no lock file).
   * - ``uv init``
     - Start a project: ``pyproject.toml``, ``.python-version``.
   * - ``uv add <pkg>``
     - Add a dependency; updates ``pyproject.toml``, ``uv.lock`` and ``.venv``.
   * - ``uv remove <pkg>``
     - Remove a dependency.
   * - ``uv lock --upgrade``
     - Re-resolve the lock file within your declared constraints.
   * - ``uv sync``
     - Make ``.venv`` match ``uv.lock``.
   * - ``uv sync --frozen``
     - Same, but never re-resolve; the lock file is authoritative.
   * - ``uv run <cmd>``
     - Run a command in the project environment without activating it.
   * - ``uv python list``
     - List available and installed Python versions.
   * - ``uv tree``
     - Show the project's dependency tree.
   * - ``uv cache prune``
     - Clean unused entries out of the download cache.

Further Reading
---------------

* `uv documentation <https://docs.astral.sh/uv/>`_
* `Working on projects <https://docs.astral.sh/uv/guides/projects/>`_
* `Locking and syncing <https://docs.astral.sh/uv/concepts/projects/sync/>`_
