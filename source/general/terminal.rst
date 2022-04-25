Using the Terminal
==================

The Linux command line is one of two methods for accessing Buddy resources. It's features, power, and flexibility are essential for those wishing to properly utilize the cluster. While the terminal may seem confusing, many of it's aspects are straightfoward.

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

  * **Powershell**: Powershell is a built in Windows terminal emulator that uses the Powershell language. You can access it via your start menu and connect Buddy by using the command ``ssh username@buddy.uco.edu``
  * **Putty**: Putty is a popular option for Windows and can be downloaded from the Putty website. 
  * **MobaXTerm**: MobaXTerm is another common software and can be downloaded form the Moba website.
  * **WinSCP**: WinSCP is a software that is not for SSH, but rather file transfer over SCP.

* **OSX**

  * **Terminal**: OSX has it's own built in terminal emulator. It can be accessed from your utility folder and you can connect to Buddy with the command ``ssh username@buddy.uco.edu``.

.. warning::
  **Filezilla is no longer recommended** as it's installer comes bundled with other software! While the bundled offer is not malicious, this can be considered undesireable as the bundled application is installed in a deceptive manner and can interfere with your anti-virus.

Terminal Basics
---------------

Navigation
~~~~~~~~~~

Creating Files and Directories
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Copy, Move, Rename, and Delete
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Editing Files
-------------

Nano
~~~~

VIM
~~~

Common Commands and Features
----------------------------

File Viewing and Pipes
~~~~~~~~~~~~~~~~~~~~~~

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


