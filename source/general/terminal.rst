Using the Terminal
==================

The Linux command line is one of two methods for accessing Buddy resources. It's features, power, and flexibility are essential for those wishing to properly utilize the cluster. While the tvigation erminal may seem confusing, many of it's aspects are straightfoward.

Background
----------

When computer first came about, one of the first operating systems to arrive was Unix. It was designed to run as a multi-user system on mainframe computers, with users connecting to it remotely via individual terminals. These terminals were extremely simplistic and consisted primarily of a keyboard and screen. 

Compared to graphics, text is very light on resources. Becuase of this, older machines could run dozens of terminals even across the slowest of networks. Despite the nature of terminals, users were still able to interact with programs quickly and efficiently. The commands were also kept very short to reduce the number of keystrokes needed, which sped up the use of the terminal even more. This speed and efficiency is one reason why this text interface is still widely used today.

When logged into a Unix mainframe via a terminal users still had to manage the sort of file management tasks that you might now perform with a mouse and a couple of windows. Whether creating files, renaming them, putting them into subdirectories or moving them around on disk, users could do everything entirely with a textual interface.

Buddy utilizes an operating system called Linux. While it bears some similarities to Unix, it is most definitly not identical and has many major differences. Buddy's terminal operates using something called "Bash" for users to communicate via the command line. Bash is widely used on Linux systems, and is well documented. This page will cover some basic functions of Bash, including some simple scripting.

Accessing the Terminal
----------------------

The terminal can be accessed in one of two ways. One is via the web browser, and the other is via SSH. Upon opening, you will be greeted with a black screen and blinking cursor. 

Web browser Access
~~~~~~~~~~~~~~~~~~

The easiest way to access the terminal is via OnDemand. Once you are logged in, you can access the terminal by going to Clusters>Buddy Shell Access. This will open up a terminal for you in a new window.

.. image:: /_static/img/ondemand_buddy_terminal.png
  :width: 100%
  :align: center
  :alt: Buddy OnDemand Job Composer

|

You will see the terminal in your web browser once you are logged in

.. image:: /_static/img/ondemand_terminal.png
  :width: 100%
  :align: center
  :alt: Buddy OnDemand Job Composer

|


SSH Access
~~~~~~~~~~

SSH access is also available for users who desire to use a preffered terminal emulator. You can ssh into buddy by connecting to ``username@buddy.uco.edu``. There are few applications available to utilize SSH

.. note::
  Please read the associated documentation for each of these softwares if you desire to use them. Users uncomfortable with this method of access are recommended to use the built in OnDemand terminal mentioned above for SSH and the OnDemand file browser for uploading and downloading files to Buddy.

* **Windows**

  * `Powershell`_: Powershell is a built in Windows terminal emulator that uses the Powershell language. You can access it via your start menu and connect Buddy by using the command ``ssh username@buddy.uco.edu``
  * `Putty`_: Putty is a popular option for Windows and can be downloaded from the Putty website.
  * `MobaXTerm`_: MobaXTerm is another common software and can be downloaded form the Moba website.
  * `WinSCP`_: WinSCP is a software that is not for SSH, but rather file transfer over SCP.

* **OSX**

  * `Terminal`_: OSX has it's own built in terminal emulator. It can be accessed from your utility folder and you can connect to Buddy with the command ``ssh username@buddy.uco.edu``.
  * `Finder`_: Your file browser in Mac OS can be used to directly connect Buddy for file transfer. You will want to connect to ``sftp://username@buddy.uco.edu``.

.. warning::
  **Filezilla is no longer recommended** as it's installer comes bundled with other software! While the bundled offer is not malicious, this can be considered undesireable as the bundled application is installed in a deceptive manner and can interfere with your anti-virus.

.. _Powershell: https://docs.microsoft.com/en-us/powershell/scripting/learn/remoting/ssh-remoting-in-powershell-core?view=powershell-7.2
.. _Putty: https://www.putty.org/
.. _MobaXTerm: https://mobaxterm.mobatek.net/
.. _WinSCP: https://winscp.net/eng/index.php
.. _Terminal: https://www.servermania.com/kb/articles/ssh-mac/
.. _Finder: https://support.apple.com/guide/mac-help/connect-mac-shared-computers-servers-mchlp1140/mac

Terminal Basics
---------------

This section will teach everyday commands that will be used regularly in the terminal. On a terminal, you don't have a file browser, word, or any other "GUI" application. But that doesn't mean it is difficult to use. While there is a learning curve, once common commands are memorized, it's as easy as riding a bike.

Navigation
~~~~~~~~~~

Navigating files and folders is a fundamental aspect of using any computer. But within the terminal, we are not automatically shown what we want to see. We have to be more explicit. 

Let's start by viewing the contents of our current folder using the "LiSt" command. 

.. code-block:: console

  [skelting1@buddy ~]$ ls
  batchjob.sh  Data_Folder_01  Data Folder 02  slurm_output.txt

Let's pass a "List" option to our "LiSt" command.

.. code-block:: console

  [skelting1@buddy ~]$ ls -l
  total 4
  -rw-r--r-- 1 skelting1 skelting1 635 Apr 21 13:13 batchjob.sh
  drwxr-xr-x 2 skelting1 skelting1  10 Apr 21 11:37 Data_Folder_01
  drwxr-xr-x 2 skelting1 skelting1  10 Apr 21 11:37 Data Folder 02
  -rw-r--r-- 1 skelting1 skelting1   0 Apr 21 11:37 slurm_output.txt

There's a lot of information to unpack here. For now, we will share that the date and time shows when a file was modified last. 

This is all well and good, but where are we? Let's "Print (our) Working Directory"

.. code-block:: console

  [skelting1@buddy ~]$ pwd
  /home/skelting1/

This path is our home folder. The username will of course differ. Your home folder is where all of your files will be stored on Buddy. When you login, this is the first folder you will see. But what if we want to access our other folders? Let's "Change Directory"

.. code-block:: console
  
  [skelting1@buddy ~]$ cd Data_Folder_01
  [skelting1@buddy Data_Folder_01]$ pwd
  /home/skelting1/Data_Folder_01

.. warning::

  Linux is CaSe SeNsItIvE! Failure to match case will result in your commands not working. 

You'll notice our prompt changes to show our current folder. Looking even closer, you'll notice we started with a ~ as our current folder. This is because the ~ is a special symbol to represent our home folder. We can even get back into the home folder by changing our directory to it.

.. code-block:: console
 
  [skelting1@buddy Data_Folder_01]$ cd ~
  [skelting1@buddy ~]$ pwd
  /home/skelting1/

Neat! But what if we are several folders in and just want to go up a folder? Let's see how that would work.

.. code-block:: console
  
  [skelting1@buddy ~]$ ls
  batchjob.sh  Data_Folder_01  Data Folder 02  slurm_output.txt
  [skelting1@buddy ~]$ cd Data_Folder_01
  [skelting1@buddy Data_Folder_01]$ ls
  data-set-01.dat  data-set-02.dat  meta
  [skelting1@buddy Data_Folder_01]$ cd meta
  [skelting1@buddy meta]$ ls
  info.json
  [skelting1@buddy meta]$ pwd
  /home/skelting1/~/Data_Folder_01/meta

One option for going up a folder is to give our ``cd`` command the ``/home/skelting1/~/Data_Folder_01/`` path. But this is highly inefficient. Let's examine another special folder. We will need to add another option to our "LiSt" command to see what they are.

.. code-block:: console

  [skelting1@buddy meta]$ ls -a
  .  ..  info.json

The "All" option for ``ls`` shows us some directories we couldn't see before. One is a directory named ``.`` and the other is a directory named ``..``. ``.`` represents the current directory, and ``..`` represents the directory above it. Going up a directory is as easy as

.. code-block:: console

  [skelting1@buddy meta]$ cd ..
  [skelting1@buddy Data_Folder_01]$  

You'll notice if you try to change directory to ``.`` that nothing really happens. This is the intended behaviour as we are changing directory to our current directory. Which of course leaves us in the same place! Let's go back to our home folder and review a special case you will most likely encounter.

.. code-block:: console

  [skelting1@buddy ~]$ ls
  batchjob.sh  Data_Folder_01  Data Folder 02  slurm_output.txt

You'll notice that one of our folder names has spaces in it. This is generally not recommended froma convienence standpoint, but it happens often for one reason or another. If we try to cd into this folder, odd things happen.

.. code-block:: console
  
  [skelting1@buddy ~]$ cd Data Folder 02
  -bash: cd: Data: No such file or directory

Our ``cd`` command only wants to take the first argument. In order to read spaces, we have to use what's called an "Escape Character". This is simply a backslash ``\``, not to be confused with the forward-slash ``/`` we use for paths. So how is the escape character used?

.. code-block:: console

  [skelting1@buddy ~]$ cd Data\ Folder\ 02
  [skelting1@buddy Data Folder 02]$ 

This may not seem intuitive to some users, so there is also the option of putting the path in quotes.

.. code-block:: console

  [skelting1@buddy ~]$ cd "Data Folder 02"
  [skelting1@buddy Data Folder 02]$ 

.. note:: 

  You may find yourself annoyed by having to always type out these paths completely. Thankfully, you can use the ``Tab`` key to auto-complete. If you press tab and nothing happens, either there is nothing beginning with that name, there are more than one items starting with that particular set of charachters, or you've made a syntax error. You may try hitting ``Tab`` three times to show available options. Alternatively, backspace over your command and type ``ls`` and/or ``pwd`` to ensure you are in the right directory and the item is actually in there. 

Creating and Deleting Files and Directories
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Often, it is needed to make a new directory. To do this we use the "MaKe DIRectory" command. As previously discussed, it is suggested to not name directories with spaces.

.. code-block:: console

  [skelting1@buddy ~]$ mkdir Data_Folder_03
  [skelting1@buddy ~]$ ls
  batchjob.sh  Data_Folder_01  Data Folder 02  Data_Folder_03  slurm_output.txt

To delete a directory, we simply use the "ReMove DIRectory" command.

.. code-block:: console

  [skelting1@buddy ~]$ rmdir Data_Folder_03
  [skelting1@buddy ~]$ ls
  batchjob.sh  Data_Folder_01  Data Folder 02  slurm_output.txt

This isn't always the best option. Especially considering it fails to work of your directory contains file within it. For that reason, the "ReMove" command is generally recommended. This works for both files and directories. Notice that to remove a directory, we must pass a "Recursive" option, but a file doesn't require it.

.. code-block:: console
 
  [skelting1@buddy ~]$ ls
  batchjob.sh  Data_Folder_01  Data Folder 02  Data_Folder_03 slurm_output.txt  
  [skelting1@buddy ~]$ rm slurm_output.txt
  [skelting1@buddy ~]$ ls
  batchjob.sh  Data_Folder_01  Data Folder 02  Data_Folder_03
  [skelting1@buddy ~]$ rm -r Data_Folder_03
  [skelting1@buddy ~]$ ls
  batchjob.sh  Data_Folder_01  Data Folder 02
  
.. warning::

  The ``rm`` command is permanent!! There is no trashcan to restore files from, and data recovery is not possible. Please be careful when using this command. Remember, think twice, hit enter once.

You may notice that if the directory is filled with files, it may prompt you about deleting each and every file. If this is the case, we can use the "Force" option. 

.. code-block:: console
  
  [skelting1@buddy ~]$ rm -r -f Data_Folder_03

There may be instances when you want to create a blank file. Do do this, we use the touch command

.. code-block:: console
  
  [skelting1@buddy ~]$ touch script.sh
  [skelting1@buddy ~]$ ls
  batchjob.sh  Data_Folder_01  Data Folder 02  script.sh  slurm_output.txt

Copy, Move, and Rename
~~~~~~~~~~~~~~~~~~~~~~

Often times, we want to replicate files and folders on our system. To do this, we use the "CoPy" command. For copying directories that contain files, we also want to include a "Rescursive" option. When using copy, we will first specify the source followed by the destination

.. code-block:: console

   [skelting1@buddy ~]$ cp script.sh copy-of-script.sh
   [skelting1@buddy ~]$ ls
   batchjob.sh  copy-of-script.sh  Data_Folder_01  Data Folder 02  script.sh  slurm_output.txt
   [skelting1@buddy ~]$ cp -r Data_Folder_01 Data_Folder_04
   [skelting1@buddy ~]$ ls
   batchjob.sh  copy-of-script.sh  Data_Folder_01  Data Folder 02  Data_Folder_04  script.sh  slurm_output.txt

We can also copy files or directories into other directories

.. code-block:: console

  [skelting1@buddy ~]$ cp script.sh Data_Folder_01/script.sh
  [skelting1@buddy ~]$ ls Data_Folder_01
  data-set-01.dat  data-set-02.dat  meta  script.sh



Common Commands and Features
----------------------------

File Viewing/Editing and Pipes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Shortcuts
~~~~~~~~~

Searching
~~~~~~~~~

Compressing and Uncompressing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

File Permissions and Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Downloading Files
~~~~~~~~~~~~~~~~~

Tips and Tricks
---------------

Basic Scripting
---------------

Hello World
~~~~~~~~~~~

Basic Logic
~~~~~~~~~~~

Providing Input
~~~~~~~~~~~~~~~

Troubleshooting
~~~~~~~~~~~~~~~

Additional Resources
--------------------


