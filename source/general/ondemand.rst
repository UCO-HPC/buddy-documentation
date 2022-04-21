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
  :alt: Buddy OnDemand Nav Interactive Apps

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

Certain applications contain other options. For example, Jupyter let's you choose between a Lab or Notebook session. Jupyter also offers ready to select module groups like "Data Science".  

File Browser
************

Ondemand offers a built in file browser. You can access it by going to Files>Home Directory. The file browser has options to upload files, edit text files, general file management, and more all within the web browser!

.. image:: /_static/img/ondemand_file_browser.png
  :width: 100%
  :align: center
  :alt: Buddy OnDemand File Browser

|

Top Menu
^^^^^^^^

Most file tasks can be performed via the menu in the upper left.

.. image:: /_static/img/ondemand_file_browser_top_menu.png
  :width: 100%
  :align: center
  :alt: Buddy OnDemand File Browser Top Menu

|

* **Open in Terminal**: Opens your current folder in a terminal via a new tab. The side arrow allows you to select the cluster you want to open the terminal on. At this time, there is only Buddy. So this option is not needed.
* **New File**: Opens a dialogue to create a new file in the current folder
* **New Directory**: Opens a dialogue to create a new folder in the current folder
* **Upload**: Opens a dialogue to upload desired files or folders
* **Download**: Downloads files or folders that have been selected
* **Copy/Move**: Opens a dialogue to copy or move files or folders that have been selected
* **Delete**: Deletes selected files or folders. 

.. warning::
  File deletion is permanent on Buddy, both in the file browser and terminal! There is no "trash". In addition, files cannot be recovered due to the nature of Buddy.

Navigation Menu
^^^^^^^^^^^^^^^

The navigation menu allows has additional navigation options that some users may find useful

.. image:: /_static/img/ondemand_file_browser_navigation_menu.png
  :width: 100%
  :align: center
  :alt: Buddy OnDemand File Browser Navigation Menu

|

* **Up Arrow**: Goes up a directory
* **Path Bar**: Shows the path to your present working directory
* **Change Directory**: Allows for navigation to a specific folder by providing a path
* **Copy Path**: Copies the path to your present working directory
* **Show Owner/Mode**: Shows file and folder permissions
* **Show dotfiles**: Shows hidden files and folders
* **Filter**: Filter current files and folders by name

File Context Menu
^^^^^^^^^^^^^^^^^

The file context menu provides a number of operations that mose users will find useful

.. image:: /_static/img/ondemand_file_browser_context_menu.png
  :width: 75%
  :align: center
  :alt: Buddy OnDemand File Browser Context Menu

|

* **View**: Opens text files for viewing in a new window
* **Edit**: Opens files in the OnDemand text editor in a new tab
* **Rename**: Opens a dialogue to rename files
* **Download**: Downloads the file

.. #TODO: Add a link to the text editor section

File Editor
***********

OnDemand has a built in file editor that you can use to modify any text based file. This is perfect for modifying scripts, input data, and a number of other tasks. 

.. image:: /_static/img/ondemand_file_editor.png
  :width: 100%
  :align: center
  :alt: Buddy OnDemand File Editor

|

There are a number of options available within the editor

* **Save**: Saves your currently open file
* **Path**: Shows the name and location of the file you currently have open
* **Key Bindings**: Allows for special key bindings
  - **Default**: This option is best for most users as this is the standard set of key bindings to which desktop users are accustom.
  - **Vim**: VIM types bindings, including common modes such as command, insert, replace, and block. This mode is not recommended unless you use VIM. 
  - **Emacs**: Emacs type bindings. This mode is not recommended unless you use Emacs.
* **Font Size**: Size of font displayed within the editor
* **Mode**: This is typically automatically selected based on your file extension. The mode controls syntax highlighting and can help to discern elements when performing tasks like writing a script.
* **Theme**: Changes how your text editor looks. Both light and dark themes are available.
* **Word Wrap**: Marks whether to wrap words. This prevents having to scroll horizontally for extremely long lines. 

Terminal Access
***************

Job Management
**************

Job Composer
************


