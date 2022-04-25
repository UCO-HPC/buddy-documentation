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

Ondemand offers a built in file browser. You can access it by going to Files>Home Directory. The file browser has options to upload files, edit text files, general file management, and more all within the web browser! Applications like Filezilla are no longer needed to move data to and from Buddy. 

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

File Options
^^^^^^^^^^^^

* **Save**: Saves your currently open file
* **Path**: Shows the name and location of the file you currently have open

Editor Options
^^^^^^^^^^^^^^

* **Key Bindings**: Allows for special key bindings
  
   * **Default**: This option is best for most users as this is the standard set of key bindings to which desktop users are accustom.  
   * **Vim**: VIM types bindings, including common modes such as command, insert, replace, and block. This mode is not recommended unless you use VIM. 
   * **Emacs**: Emacs type bindings. This mode is not recommended unless you use Emacs.

* **Font Size**: Size of font displayed within the editor
* **Mode**: This is typically automatically selected based on your file extension. The mode controls syntax highlighting and can help to discern elements when performing tasks like writing a script.
* **Theme**: Changes how your text editor looks. Both light and dark themes are available.
* **Word Wrap**: Marks whether to wrap words. This prevents having to scroll horizontally for extremely long lines. 

Terminal Access
***************

A terminal can be accessed by going to Clusters>Buddy Shell Access. This terminal is web based will open a terminal in a new window. This means that applications like Putty are no longer needed to access Buddy.

.. image:: /_static/img/ondemand_terminal.png
  :width: 100%
  :align: center
  :alt: Buddy OnDemand Terminal

|

Much like the text editor, the terminal also has a theme option. To learn more about bash and common Linux commands, see our guide on the terminal and Slurm. 

.. #TODO: Add a link to the "Using The Terminal" and "Slurm" section.

Job Management
**************

Jobs Management can be accessed by going to Jobs>Active Jobs. This allows users to manage their slurm jobs, as well as see jobs from other users running on the cluster. Please see our Slurm section for more information about jobs. Please note that this application is paginated, and you may need to mark to show more entires or click through available pages using the navigation at the bottom.

.. #TODO: Add a link to "Slurm Jobs"

.. image:: /_static/img/ondemand_active_jobs.png
  :width: 100%
  :align: center
  :alt: Buddy OnDemand Active Jobs

|

View Options
^^^^^^^^^^^^

There are a few options to adjust your current view within the Active Jobs application.

.. image:: /_static/img/ondemand_active_jobs_view.png
  :width: 100%
  :align: center
  :alt: Buddy OnDemand Active Jobs View Options

|

* **Your Jobs/All Jobs**: Toggles wether you want to view only your jobs, or all jobs on the cluster
* **All Clusters/Buddy**: Chooses which cluster's active jobs will show. Since there is only one cluster, Buddy, this option is currently irrelevant.
* **Filter**: Filter displayed jobs via keywords
* **Show ## Entries**: Change the number of entries to show on a single page

Job Context Menu
^^^^^^^^^^^^^^^^

All jobs have an associated context menu that can be seen be clicking the arrow next to the job. Note the below screenshot is what will be seen for self owned jobs. Jobs owned by other users will be lacking many of these options as you don't have permission to modify them.

.. image:: /_static/img/ondemand_active_jobs_context.png
  :width: 100%
  :align: center
  :alt: Buddy OnDemand Active Jobs Context Menu

|

* **Red Trash Bin**: Cancel your current job
* **Job Status**: Status of your current Slurm job. Possible states include Running, Pending, Completing, and Cancelled. Please see our page on Slurm for more information. 
* **Open in File Manager**: Opens the job working directory in the OnDemand file browser. This makes tasks such as viewing job output more convienent. 
* **Open in Terminal**: Opens the job working directory in the OnDemand terminal
* **Delete**: Cancels the job selected

.. #TODO: Add links to slurm documentation references

Job Composer
************

The Job Composer can be accessed by going to Jobs>Job Composer and open in a new tab. Job Composer allows for creating and running slurm jobs from within your browser. Some users may find this more convienent than using the terminal to run slurm jobs. 

Overview
^^^^^^^^

.. image:: /_static/img/ondemand_composer.png
  :width: 100%
  :align: center
  :alt: Buddy OnDemand Job Composer

|


The Job Composer's main screen offers a number of options.

* **+New Job**: Create a new job from one of the following

   * **From Default Template**: Creates a new job from the default template
   * **From Template**: Creates a new job from a pre-defined template
   * **From Specified Path**: Creates a new job from files within a specified directory
   * **From Selected Jobs**: Copies the currently selected job into a new job.

* **Create Template**: Create a new template from the current job. There are a few options that need set.

  * **Path**: Path of folder to be used to generate the template
  * **Name**: Name of the job template
  * **Cluster**: Name of the cluster the job will run on by default. Buddy is the only cluster, so this option is irrelevant. 
  * **Notes**: Notes for the job written in HTMl markup.

* **Edit Files**: Open the currently selected job in the file browser to edit and manage job files. You can use this to upload new inoput files or modify job scripts
* **Job Options**: Opens a dialogue within your current window to set various job options

   * **Name**: Name of your job
   * **Cluster**: Name of the cluster your job will run on. Since we only have one cluster, Buddy, this option is irrelevant. 
   * **Specify Job Script**: Specify the name of the script to be executed when the submit button is pressed within the job composer.
   * **Account**: We do not currently use accounting. Please leave this field blank. 
   * **Job Array Specification**: Please see Advanced Slurm topics for more information on configuring arrays.

* **Open Terminal**: Open the current job's folder in the the terminal. This is a faster option for managing job files for those familiar with bash.
* **Submit**: Submit the selected job to the cluster
* **Stop**: Cancel the running of a selected job
* **Delete**: Delete the current job from job composer
* **Job Details**: Details regarding the current job. Use the "Job Options" button to modify these fields. 
* **Submit Script**: Details of the script being used. Options in this field include

   * **Open Editor**: Opens the job script in the file editor
   * **Open Terminal**: Opens the job folder in the terminal
   * **Open Dir**: Opens the job folder in the file browser

Creating Job From Template
^^^^^^^^^^^^^^^^^^^^^^^^^^

Here we will look at creating a job from a template. The process is roughly the same for a default template as well. This example will use Gaussian. Please see the Software and Slurm sections of the documentation for details on writing Slurm scripts and how to use your desired application. 

1. Select "From Template" from the "New Job" menu.
 
.. image:: /_static/img/ondemand_composer_create_01.png
  :width: 25%
  :align: center
  :alt: Buddy OnDemand Job Composer Create

|

2. From the template screen, select the desired template and click "Create New Job" from the right hand pane. For this example, we will select the Gaussian template. Be sure to also set the desired job name. We will ignore the Cluster option, as Buddy is currently the only available cluster. 

 
.. image:: /_static/img/ondemand_composer_create_02.png
  :width: 100%
  :align: center
  :alt: Buddy OnDemand Job Composer Create

|

3. We will now need to make some modifications to our script and upload the input file we want. Select your job and click "Edit Files" on the left side. This will open the file browser in a new window. Upload your input files and edit the Slurm script accordingly. Please see the File Browser and File Editor section of the documentation. Please also see the Slurm documentation for writing your script. 
 
.. image:: /_static/img/ondemand_composer_create_03.png
  :width: 75%
  :align: center
  :alt: Buddy OnDemand Job Composer

|

4. Once everything is setup, we can click submit job. If everything goes as expected, you should see the job pass through several states, eventually reaching completion. To stop a job, simply press the stop button. Output can be viewed by pressing the "Open Dir" button in the bottom right, or using the edit button in the upper left. Should a job not complete as expected.

Modifying Job Options
^^^^^^^^^^^^^^^^^^^^^

Certain job options can be modifying by selecting the desired job and clicking "Job Options".

.. image:: /_static/img/ondemand_job_options_01.png
  :width: 70%
  :align: center
  :alt: Buddy OnDemand Job Composer

|

Job options will be opened within your current window. 

.. image:: /_static/img/ondemand_job_options_02.png
  :width: 100%
  :align: center
  :alt: Buddy OnDemand Job Composer

|

* **Name**: Name of your job
* **Cluster**: Name of the cluster your job will run on. Since we only have one cluster, Buddy, this option is irrelevant. 
* **Specify Job Script**: Specify the name of the script to be executed when the submit button is pressed within the job composer.
* **Account**: We do not currently use accounting. Please leave this field blank. 
* **Job Array Specification**: Please see Advanced Slurm topics for more information on configuring arrays.

You can reset any changes made with the reset button, or by clicking back.

Saving and Managing Templates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

User's can save and manage Templates under the "Templates" tab of the Job Composer. System provided Job Composer templates are only available for a limited number of software. We are currently working to add more to OnDemand. Generic Slurm templates are available under the Slurm section and specific templates are available in the SOFTWARE section.


.. image:: /_static/img/ondemand_template_tab.png
  :width: 75%
  :align: center
  :alt: Buddy OnDemand Templates

|

New templates can be created either by starting one from scratch or by copying a current template. Template files can aslo be modified from this view.

.. image:: /_static/img/ondemand_template_view.png
  :width: 100%
  :align: center
  :alt: Buddy OnDemand Templates

|

.. note::
  The scope of this section is **extremely** limited. A more in depth walk through of utilizing the template feature will eventually be provided under the ADVANCED section of this documentation. 

* **New Template/Copy Template**: Create or copy a template for use.

  * **Path**: Path that contains your desired default tmeplate files. They should include a runtime script, relative input files, and manifest.yml. Please note the manifest.yml, while important, is nopt covered in this document. Please view another templates folder to see how this is constructed or email UCO's HPC support.
  * **Name**: Name of the template  
  * **Cluster**: Name of the cluster your job will run on. Since we only have one cluster, Buddy, this option is irrelevant.
  * **Notes**: Notes about the job script template.

* **Delete**: Delete a selected template. You may only delete user created templates as System Templates are managed by CREIC. 

.. #TODO: Add links to the referenced documentation

