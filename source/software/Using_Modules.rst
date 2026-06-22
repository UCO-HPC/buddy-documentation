Using Modules
=============

The Buddy software environment is split into two parts: preloaded software 
(available immediately upon login) and modular software (which must be 
explicitly loaded).

To manage conflicts that arise from different applications requiring different 
versions of libraries, Buddy uses the `Lmod Environment Module System <https://lmod.readthedocs.io/en/latest/>`_.

Finding Software
----------------

To check if software is currently loaded, use ``which``.
``which <appName>`` looks for the application ``appName`` on your ``$PATH``, 
and returns the full path to the executable.

Search Available Modules
------------------------

If ``which`` doesn't find the application, use ``module spider`` to search 
all available modules.

.. code-block:: bash

   module spider <moduleName>

Module Commands
---------------

Commonly used module commands include:

.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - Command
     - Action
   * - ``module avail``
     - Lists all modules available to your current environment.
   * - ``module spider <name>``
     - Searches for all modules, even those currently hidden.
   * - ``module load <name>``
     - Loads the default version of the module.
   * - ``module load <name>/<version>``
     - Loads a specific version of the software.
   * - ``module unload <name>``
     - Removes the software and its environment settings.
   * - ``module list``
     - Shows all modules currently loaded.
   * - ``module purge``
     - Unloads all currently loaded modules.
   * - ``module show <name>``
     - Displays module environment variables, paths, and settings.

Default Versions
----------------

``module avail <name>`` or ``module spider <name>`` typically indicates the 
default version with a marker (``(D)``, ``(default)``, or ``*``).

Running ``module load`` without specifying a version loads the default. To 
load a different version, specify the complete module name:

.. code-block:: bash

   module load python/3.9.7

Tips for Batch Scripts
----------------------

Follow these best practices to avoid conflicts between modules and ensure 
reliable execution:

* Use ``module purge`` first.
* Load only what is necessary.
* Specify full module versions.

!!! Be careful when loading modules in ``.bashrc`` — loading modules in your 
  ``~/.bashrc`` can cause software conflicts, and even prevent login.