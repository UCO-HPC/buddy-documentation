Using the Terminal
==================

The Linux command line is one of two methods available for accessing Buddy resources. Accessing the cluster this way is recommended for users who are already familiar with navigating Linux using a terminal.

Background
----------

Buddy's servers and compute nodes run on an operating system called Linux. Unlike Windows or MacOS, interfacing with a Linuxmachine mainly relies on using a terminal, where users can input commands to interact with the system. You can create, view, and edit files and scripts as well as schedule jobs with Slurm.

Accessing the Terminal
----------------------

The terminal can be accessed in one of two ways. One is via the web browser, and the other is via SSH. Upon access, you will be greeted with a black screen and blinking cursor. 

Web browser Access
~~~~~~~~~~~~~~~~~~

The easiest way to access the terminal is via OnDemand. Once you're logged in, you can access the terminal by going to Clusters > Buddy 2.5 Shell Access. This will open up a terminal for you in a new window.

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

SSH access is also available for those who prefer using a terminal emulator of their choice. You can ssh into Buddy by connecting to ``username@hpc.uco.edu``. There are few applications available on Windows and MacOS to utilize SSH:

.. note::
  Please read the associated documentation for each of these softwares if you desire to use them. Users uncomfortable with this method of access are recommended to use the built in OnDemand terminal mentioned above for SSH and the OnDemand file browser for uploading and downloading files to Buddy.

* **Windows**

  * `Powershell`_: Powershell is a built-in Windows terminal emulator that uses the Powershell language. You can access it via your start menu and connect Buddy by using the command ``ssh username@buddy.uco.edu``. You can exit the ssh prompt by typing ``exit``.
  * `WSL`_: Windows Subsystem for Linux is a popular option for running a local Linux virtual machine on your own computer. WSL utilizes the built-in Windows terminal. You can use this terminal to SSH into Buddy.
  * `Putty`_: Putty is a popular option for Windows and can be downloaded from the Putty website.
  * `MobaXTerm`_: MobaXTerm is another common software and can be downloaded form the Moba website.
  * `WinSCP`_: WinSCP is a software that is not for SSH, but rather file transfer over SCP.

* **OSX**

  * `Terminal`_: OSX has it's own built in terminal emulator. It can be accessed from your utility folder and you can connect to Buddy with the command ``ssh username@buddy.uco.edu``. You can exit the ssh prompt by typing ``exit``.
  * `Finder`_: Your file browser in Mac OS can be used to directly connect Buddy for file transfer. You will want to connect to ``sftp://username@buddy.uco.edu``.

.. warning::
  **Filezilla is no longer recommended** as it's installer comes bundled with other software! While the bundled offer is not malicious, this can be considered undesireable as the bundled application is installed in a deceptive manner and can interfere with your anti-virus.

.. _Powershell: https://docs.microsoft.com/en-us/powershell/scripting/learn/remoting/ssh-remoting-in-powershell-core?view=powershell-7.2
.. _WSL: https://learn.microsoft.com/en-us/windows/wsl/about
.. _Putty: https://www.putty.org/
.. _MobaXTerm: https://mobaxterm.mobatek.net/
.. _WinSCP: https://winscp.net/eng/index.php
.. _Terminal: https://www.servermania.com/kb/articles/ssh-mac/
.. _Finder: https://support.apple.com/guide/mac-help/connect-mac-shared-computers-servers-mchlp1140/mac

Terminal Basics
---------------

This section covers everyday commands used regularly in the terminal. On a terminal, you don't have a file browser, word, or any other "GUI" application. But that doesn't mean it is difficult to use. While there is a learning curve, once common commands are memorized, it's as easy as riding a bike.

Navigation
~~~~~~~~~~

Navigating files and folders is a fundamental aspect of using any computer. But within the terminal, we are not automatically shown what we want to see. We have to be more explicit. 

Let's start by viewing the contents of our current folder using the "List" command. 

.. code-block:: console

  [skelting1@buddy ~]$ ls
  batchjob.sh  Data_Folder_01  Data Folder 02  slurm_output.txt

You can view the contents of a directory by passing a file path to the "LiSt"

.. code-block:: console

  [skelting1@buddy ~]$ ls Data_Folder_01
  data-set-01.dat  data-set-02.dat  meta

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

One option for going up a folder is to give our ``cd`` command the absolute path of the parent directory: ``/home/skelting1/Data_Folder_01/`` but, this is highly inefficient. Let's examine another special folder. We will need to add another option to our "LiSt" command to see what they are.

.. code-block:: console

  [skelting1@buddy meta]$ ls -a
  .  ..  info.json

The "All" option for ``ls`` shows us some directories we couldn't see before. One is a directory named ``.`` and the other is a directory named ``..``. ``.`` represents the current directory, and ``..`` represents the directory above it. Going up a directory is as easy as

.. code-block:: console

  [skelting1@buddy meta]$ cd ..
  [skelting1@buddy Data_Folder_01]$  

With the ``..`` relative path in your tool-belt you can go anywhere by building up a longer path. For example, to jump from a directory to a sibling directory, you could go up a directory and then down with two two separate commands or you can jump directly using one command

.. code-block:: console

  [skelting1@buddy meta]$ pwd
  /home/skelting1/Data_Folder_01/meta
  [skelting1@buddy meta]$ cd ../../Data_Folder_02
  [skelting1@buddy Data_Folder_02]$ pwd
  /home/skelting1/Data_Folder_02

You'll notice if you try to change directory to ``.`` that nothing really happens. This is the intended behavior as we are changing directory to our current directory. Which of course leaves us in the same place! Let's go back to our home folder and review a special case you will most likely encounter.

.. code-block:: console

  [skelting1@buddy ~]$ ls
  batchjob.sh  Data_Folder_01  Data Folder 02  slurm_output.txt

You'll notice that one of our folder names has spaces in it. This is generally not recommended from a convenience standpoint, but it happens often for one reason or another. If we try to ``cd`` into this folder, odd things happen.

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

If you want to delete several similarly named files, like output files, you can replace the part that differs between the paths by a star which is called a wildcard.

.. code-block:: console

  [skelting1@buddy ~]$ ls
  data-001.out data-002.out data-003.out data-004.out foobar.out example.txt
  [skelting1@buddy ~]$ rm data-*.out
  [skelting1@buddy ~]$ ls
  foobar.out example.out

.. warning::

  The ``rm`` command is permanent!! There is no trashcan to restore files from, and data recovery is not possible. Please be careful when using this command. Remember, think twice, hit enter once.

You may notice that if the directory is filled with files, it may prompt you about deleting each and every file. If this is the case, we can use the "Force" option. 

.. code-block:: console
  
  [skelting1@buddy ~]$ rm -r -f Data_Folder_03

or

.. code-block:: console
  
  [skelting1@buddy ~]$ rm -rf Data_Folder_03

There may be instances when you want to create a blank file. Do do this, we use the touch command

.. code-block:: console
  
  [skelting1@buddy ~]$ touch script.sh
  [skelting1@buddy ~]$ ls
  batchjob.sh  Data_Folder_01  Data Folder 02  script.sh  slurm_output.txt

Copy, Move, and Rename
~~~~~~~~~~~~~~~~~~~~~~

Often times, we want to replicate files and folders on our system. To do this, we use the "CoPy" command. For copying directories that contain files, we also want to include a "Recursive" option. When using copy, we will first specify the source followed by the destination

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

The "MoVe" command is used to move files from one place to another. Its behavior can change depending on what paths you provide and what those paths go to.

If you provide two paths and the first one exist while the second one does not, the first file will be renamed to the second.

.. code-block:: console

  [skelting1@buddy ~]$  ls
  batchjob.sh copy-of-script.sh Data_Folder_01 Data Folder 02 script.sh slurm_output.txt
  [skelting1@buddy ~]$ mv script.sh foobar.sh
  [skelting1@buddy ~]$  ls
  batchjob.sh copy-of-script.sh Data_Folder_01 Data Folder 02 foobar.sh slurm_output.txt

.. note::

   If foobar.sh already exists, the command will throw an error. Using the -f flag will allow you to overwrite foobar.sh

This works for directories as well with one exception. If the last path provided is an existing directory, whatever is at all of the other paths will be moved into the directory


.. code-block:: console

  [skelting1@buddy ~]$  ls
  batchjob.sh copy-of-script.sh Data_Folder_01 Data Folder 02 foobar.sh slurm_output.txt
  [skelting1@buddy ~]$ mv batchjob.sh copy-of-script.sh foobar.sh slurm_output.txt Data_Folder_01
  [skelting1@buddy ~]$  ls
  Data_Folder_01 Data Folder 02
  [skelting1@buddy ~]$  ls Data_Folder_01
  data-set-01.dat  data-set-02.dat  meta  script.sh batchjob.sh copy-of-script.sh foobar.sh slurm_output.txt

You can also use wildcards to move similarly named paths as well. If you wanted to move your ``.dat`` files back out of Data_Folder_1 and into the current working directory you could do the following

.. code-block:: console

  [skelting1@buddy ~]$  ls Data_Folder_01
  data-set-01.dat  data-set-02.dat  meta  script.sh batchjob.sh copy-of-script.sh foobar.sh slurm_output.txt
  [skelting1@buddy ~]$  mv Data_Folder_01/*.dat .
  [skelting1@buddy ~]$  ls
  data-set-01.dat data-set-01.dat Data_Folder_01 Data Folder 02

.. note::

  Notice the use of the special ``.`` path to reference the current working directory

Common Commands and Features
----------------------------

File Viewing/Editing and Pipes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Viewing
_______
Viewing the contents of a file is a common task so there are a couple of commands to do so. The "conCATenate" command is used to display the entire contents of a file

.. code-block:: console

  [skelting1@buddy ~]$  cat data-set-01.dat
  key1 value1
  key2 value2
  key3 value3

The name "conCATenate" comes from its ability to join the output of files together. This is evident when viewing the contents of several files at once

.. code-block:: console

  [skelting1@buddy ~]$  cat data-set-01.dat data-set-02.dat
  key1 value1
  key2 value2
  key3 value3
  other data1
  other data2
  other data3

You could have also used the wildcard character here: ``cat *.dat``

If you just want to view the beginning or end of a file you can use the head and tail commands respectively. The ``-n`` flag specify how many lines you would like to see; defaulting to 10 if the -n flag is omitted

.. code-block:: console

  [skelting1@buddy ~]$  tail -n 2 data-set-01.dat
  key2 value2
  key3 value3
  [skelting1@buddy ~]$  head -n 2 data-set-01.dat
  key1 value1
  key2 value2

Tail has a useful feature in the ``-f`` flag which causes tail to watch for changes in the given files and updates the screen as they occur. This is particularly useful for output files such as those generated by slurm scripts

.. code-block:: console

  [skelting1@buddy ~]$  tail -n 2 -f slurm.out
  output line 2
  output line 3

later...

.. code-block:: console

  [skelting1@buddy ~]$  tail -n 2 -f slurm.out
  output line2
  output line3
  output line4


.. note::

  Displaying the contents of a file usually only makes since is that file is plain text; i.e. not a binary file. Catting out a .bin file will just result in your screen being filled with random nonsense characters

Editing with nano
_________________

To begin editing a file with nano pass its file path to the ``nano`` command

.. code-block:: console

   [skelting1@buddy ~]$ nano data-set-02.dat

.. code-block::
   :linenos:
   :caption: data-set-02.dat

   April 1st subject baseline
   May 5th subject reports weight loss
   June 3rd subject reports light-headedness may be due to trial drug
   June 10th trial discontinued

Navigate using arrow keys and edit the file by typing characters and using backspace like you'd expect. The characters you type will appear before the currently selected character. 

.. note::
   When using the nano editor, command shortcuts appear at the bottom of the screen. These shortcuts can be confusing if you aren't familiar with the notation so just remember that ``^`` refers the ``Ctrl`` key and ``M`` represents the meta key also known as the ``Alt`` key on windows or the ``Option`` on Mac.

Copy, cut, and paste can be achieved by first selecting the desired text. Move the cursor to the first character of the selection, hold ``Shift`` and use the arrow keys to select all desired characters. Then press ``Alt+6`` or ``Option+6`` to copy or ``Ctrl+k`` to cut, move to the desired paste location and press ``Ctrl+u`` to paste.

Save using ``Ctrl+o`` and exit using ``Ctrl+x``.

Editing with vim
________________

To begin editing a file with nano pass its file path to the ``vim`` command

.. code-block:: console

   [skelting1@buddy ~]$ vim data-set-02.dat

.. code-block::
   :linenos:
   :caption: data-set-02.dat

   April 1st subject baseline
   May 5th subject reports weight loss
   June 3rd subject reports light-headedness may be due to trial drug
   June 10th trial discontinued

Vim uses the concept of "modes" to categorize different kinds of behavior. For instance, typing new portions of a file must happen within "insert mode". Understanding how to use and swtich between modes is one of the most important parts of using vim.

To enter a mode first enter "normal" mode by pressing the ``ESC`` key. You can think of this as backing out of whatever other mode you might already be in. Then press the appropriate key to enter your desired mode.

.. tip::
   If you hit something by mistake and can't figure out how to get out of it, just spam the ``ESC`` key. This will always get you back to vim's normal mode and you can get where you want from there. When in doubt, get to normal mode. 

+----------+----------------------+---------------------------------------------------------+
| Shortcut | Mode                 | Description                                             |
+==========+======================+=========================================================+
| ESC      | Normal mode          | manipulate whole lines and jump into other modes        |
+----------+----------------------+---------------------------------------------------------+
| i        | Insert mode          | insert and delete characters like a normal editor       |
+----------+----------------------+---------------------------------------------------------+
| Ctrl+v   | Block visual mode    | select character by character and across multiple lines |
+----------+----------------------+---------------------------------------------------------+
| Shift+v  | Linewise visual mode | select multiple lines                                   |
+----------+----------------------+---------------------------------------------------------+
| :        | Command mode         | type commands to perform various vim functions          |
+----------+----------------------+---------------------------------------------------------+

To begin editing a file, make sure you're in normal mode by pressing ``ESC``, enter insert mode by pressing ``i``, and begin editing. 

Cut, copy, and paste can be caried out on entire lines or on selected portions of text. 

To copy an entire line, enter normal mode by pressing ``ESC``, navigate the cursor to the desired line, and "yank" the line with ``yy``. Cut is similar to copy but you "delete" the line with ``dd`` instead of "yanking" it. To paste the stored line, navigate the cursor to a line near where you would like to "put" it and press ``p`` to paste the below the current line or ``Shift+p`` to paste above it. 

To copy or cut a selection you first need to select some text. To select multiple lines, first be sure you're in normal mode by typing ``ESC``, then navigate to the first line you would like to select and enter "linewise visual mode" by pressing ``Shift+v``. Finally use the up and down arrow keys to select more lines. To select a block of text, first be sure you're in normal mode by pressing ``ESC``, then navigate the first character you would like to select and enter "block visual mode" by pressing ``Ctrl+v``. Finally use the arrow keys to complete your selection.

With some of the text selected you can "yank" (copy) the selection with ``y`` or "delete"(cut) it with ``d``. You can "put"(paste) the selected text using ``p`` or ``Shift+p``. If you made the selection using "linewise visual mode" the selection will be pasted above or below the current line. If you made the selection using "block visual mode" the selection will be pasted before or after the currently selected character.

To save the current file or exit vim you need to use the appropriate vim commands. Firstly, you need to be sure you are in normal mode by typing ``ESC`` then jump into command mode by typing ``:``. In command mode you can save the current file by typing the ``w`` command and hitting enter. To save and quit type ``wq`` and hit enter. You can quit without saving by just using the ``q`` command if you haven't edited the file otherwise you will have to force vim to exit without saving by using the ``q!`` command.

Pipes
_____
Sometimes you may want to take the output of a command and so something with it like storing it in a file or passing it to another command; this is where pipes become useful

For example: if you wanted to store the result of the ``ls`` command as a file, you could do the following

.. code-block:: console

  [skelting1@buddy ~]$ ls > output.txt
  [skelting1@buddy ~]$ cat output.txt
  data-set-01.dat  data-set-02.dat  meta

The ``>`` pipe places the output of the previous command into the given file; creating it if it doesn't already exist and overwriting it if it does. If you wish to append the command output to the end of the given file instead of overwriting it use the ``>>`` pipe.

.. code-block:: console

  [skelting1@buddy ~]$ ls >> output.txt
  [skelting1@buddy ~]$ cat output.txt
  data-set-01.dat  data-set-02.dat  meta
  [skelting1@buddy ~]$ ls >> output.txt
  [skelting1@buddy ~]$ cat output.txt
  data-set-01.dat  data-set-02.dat  meta
  data-set-01.dat  data-set-02.dat  meta

To pass the output of one command as input to another use the ``|`` pipe. For example if you only wanted the last two lines of the ``ls -a`` command you could do the following.

.. code-block:: console

  [skelting1@buddy ~]$ ls -l
  total 16
  drwxr-xr-x 2 tdunn3 tdunn3 4096 May  4 11:35  Data_Folder_01
  drwxr-xr-x 2 tdunn3 tdunn3 4096 May  4 11:35 'Data Folder 02'
  -rw-r--r-- 1 tdunn3 tdunn3   36 May  4 11:34  data-set-01.dat
  -rw-r--r-- 1 tdunn3 tdunn3   39 May  4 11:34  data-set-02.dat
  [skelting1@buddy ~]$ ls -l | tail -n 2
  -rw-r--r-- 1 tdunn3 tdunn3   36 May  4 11:34  data-set-01.dat
  -rw-r--r-- 1 tdunn3 tdunn3   39 May  4 11:34  data-set-02.dat

It is common practice to chain multiple commands one after the other using ``|`` in order to refine data with successive commands.

Shortcuts
~~~~~~~~~

+---------------+-------------------------------------------------------------------+
| Command       | description                                                       |
+===============+===================================================================+
| !!            | used within a command will be replaced with your last run command |
+---------------+-------------------------------------------------------------------+
| Ctl+Shift+c   | copies the selected text in the terminal                          |
+---------------+-------------------------------------------------------------------+
| Ctl+Shift+v   | pastes in terminal                                                |
+---------------+-------------------------------------------------------------------+
| Tab           | completes the portion of text that has already been typed         |
+---------------+-------------------------------------------------------------------+
| Up            | autofills the last command                                        |
+---------------+-------------------------------------------------------------------+
| Home          | jumps to beginning of line                                        |
+---------------+-------------------------------------------------------------------+
| End           | jumps to end of line                                              |
+---------------+-------------------------------------------------------------------+

Searching
~~~~~~~~~

grep
____
The ``grep`` command is one of the most useful commands you could have in your arsenal. It's used to search for words or patterns within one or multiple files or strings.

To search for lines containing a word or phrase within a file:

.. code-block:: console

   [skelting1@buddy ~]$ cat data-set-02.dat
   April 1st subject baseline
   May 5th subject reports weight loss
   June 3rd subject reports light-headedness may be due to trial drug
   June 10th trial discontinued
   [skelting1@buddy ~]$ grep data-set-02.dat May
   May 5th subject reports weight loss

Grep also works with data piped in from other commands. This is actually a common use case for grep

.. code-block:: console

   [skelting1@buddy ~]$ ls -l
   total 16
   drwxr-xr-x 2 tdunn3 tdunn3 4096 May  4 11:35  Data_Folder_01
   drwxr-xr-x 2 tdunn3 tdunn3 4096 May  4 11:35 'Data Folder 02'
   -rw-r--r-- 1 tdunn3 tdunn3   36 May  4 11:34  data-set-01.dat
   -rw-r--r-- 1 tdunn3 tdunn3   39 May  4 11:34  data-set-02.dat
   [skelting1@buddy ~]$ ls -l | grep 02
   drwxr-xr-x 2 tdunn3 tdunn3 4096 May  4 11:35 'Data Folder 02'
   -rw-r--r-- 1 tdunn3 tdunn3   39 May  4 11:34  data-set-02.dat

Another important use case for grep is listing files that contain a pattern with the ``-l`` flag. It is often used with the ``-i`` flag which makes the search case insensative (May is the same as may) and ``-R`` which recursivly searches directories.

.. code-block:: console

   [skelting1@buddy ~]$ grep -Ril may
   data-set-02.dat

.. note::
   To search for patterns that contain spaces you can either "escape" the spaces using back slashes, i.e. `my string` becomes `my\\ string`, or you can quote them, `my string` becomes `"my string"`. However, quotes can be tricky because they are designed to search for regular expressions so special characters like ``.``'s and ``-``'s are treated as instructions. To search for quoted patterns containing special characters you must "escape" them with back slashes like "my hyper\\-strange expression goes \\[HERE\\] \\." This forces those characters to be read as "literals" meaning they are treated as the literal character you typed and not a regular expressrion instruction.

find
____
The find command is used to find files matching the given pattern

To find files within the current directory and its subdirectories with "02" in the name

.. code-block:: console

   [skelting1@buddy ~]$ ls
   Data_Folder_01 'Data Folder 02' data-set-01.dat data-set-02.dat
   [skelting1@buddy ~]$ find . -name 02
   'Data Folder 02' data-set-02.dat

Find is often used with other commands. For example you can find with the type f (regular file) using find's ``-type`` and then of pass those to grep using the ``-exec`` flag to select only those files that contain a certain phrase

.. code-block:: console

   [skelting1@buddy ~]$ find . -type f -exec grep -l May {} \;
   data-set-02.dat

The ``{}`` in the above command will be filled by the output of the rest of the find command. So actual command that returns the above output is ``grep -l May data-set-01.dat data-set-02.dat``

File Permissions and Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Listing file info
_________________
The ``ls -l`` command provides a lot of useful information.

.. code-block:: console

  [skelting1@buddy ~]$ ls -l
  total 16
  drwxr-xr-x 2 tdunn3 tdunn3 4096 May  4 11:35  Data_Folder_01
  drwxr-xr-x 2 tdunn3 tdunn3 4096 May  4 11:35 'Data Folder 02'
  -rw-r--r-- 1 tdunn3 tdunn3   36 May  4 11:34  data-set-01.dat
  -rw-r--r-- 1 tdunn3 tdunn3   39 May  4 11:34  data-set-02.dat

The first part of each line, ``drwxr-xr-x``, describe the file permissions i.e. who is allowed to do what with this file. The ``d`` means we are looking at a directory and the next nine character correspond to the read(r), write(w), and execute(x) permissions for the owner the file, the access group, and everyone else respectively. For example, the first file has permissions of ``rwxr-xr-x`` which means the owner can read, write and execute(``rwx``) and the group along with everyone else can only read and execute(``r-x``).

The second part counts the number of hard links to the file. If you're curious you can find more information `here <https://medium.com/@krisbredemeier/the-difference-between-hard-links-and-soft-or-symbolic-links-780149244f7d>`_

The third and fourth parts correspond to the owner and the group respectively. These are the same owner and group that are referenced in the first part.

The fourth, fifth, and sixth parts describe the file size, the date the file was created, and its name respectively.

Changing file permissions
_________________________
The file permissions described in the previous section can be altered with the ``chmod`` command. There are two ways to use this command: the first is easier to understand but bulky while the second is more obscure but also more concise.

The bulky version:

.. code-block:: console

  [skelting1@buddy ~]$ chmod u=rwx,g=rx,o=r data-set-02.dat

In the above example ``u=rwx`` gives read, write, and execute permissions to the owner of the file, ``g=rx`` gives read and execute permissions to the file's group and ``o=r`` gives read permissions to everyone else.

For the concise version each of the permissions are encoded as powers of two. Read (r) is encoded as 4, write(w) is 2, execute(x) is 1, and 0 is reserved for no permissions. In the above example, the owner of the file has permissions of ``rwx``. To express that using the encoded numbers, simply add them together. 4+2+1=7 so ``rwx`` is equivalent to 7. Next, the group has ``rx`` permissions so, 4+2=6, ``rx`` is equivalent to 6. Finally everyone else only has read permissions so that is simply 2. The final permissions are written in owner-group-other order so the permissions for this file are written as 762,
 
.. code-block:: console

  [skelting1@buddy ~]$ chmod 762 data-set-02.dat
 
This method may seem complicated but it is a more direct way of representing permissions and it is much more common than the first method so you are more likely to see it when searching for command help than the first example. As with any command, if you use it often enough you will learn it, otherwise don't be ashamed to look it up.

Compressing and Uncompressing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Compressing a file makes it more portable; both because it can reduce the file size but also because it bundles a directory of files into a single file.

Probably the easiest way to compress a file is to use the ``zip`` command.

.. code-block:: console

  [skelting1@buddy ~]$ zip zipped_file.zip my_directory/

To uncompress a ``zip`` file use the ``unzip`` command.

.. code-block:: console

  [skelting1@buddy ~]$ unzip zipped_file.zip

Another popular method for compressing files is the ``tar`` command. The ``tar`` command has notoriously difficult to remember flags which has lead to an inside joke among linux users: "Oh so you say you're a linux expert, but can you tar a file without looking it up?". This is mainly because no one uses the command frequently enough to remember how it works. That being said, it isn't difficult; just hard to remember so don't be afraid to refer back to this guide if you forget because even the experts have to look it up.

.. code-block:: console

  [skelting1@buddy ~]$ tar -czvf compressed.tar.gz my_directory/

Technically, ``tar`` isn't a compression tool. It creates archives, called tarballs, which could be compressed but don't have to be. These archives essentially bundle different files together into a single file. In the above command the ``-c`` flag creates an archive, ``-z`` compresses it using the ``gzip`` format, ``-v`` displays the progress in the terminal, and ``-f`` allows you to specify the file name of the final tarbal.

Untarring a file can be accomplished as follows:

.. code-block:: console

  [skelting1@buddy ~]$ tar -xvf compressed.tar.gz

In the above example: ``-x`` extracts the files from the tarbal, ``-v`` displays progress in the terminal, and ``-f`` allows you to specify the input file name.

Downloading Files
~~~~~~~~~~~~~~~~~
Downloading files from sources on the internet is a crucial part of modern terminal usage and there are several ways to accomplish it for different use cases.

.. note::
   Please review the :doc:`Cluster Usage: Rules and Guidelines </quickstart/etiquette>` section and the :doc:`Data Transfer </general/data_transfer>` section before moving data onto buddy

wget
____
Wget is a command line tool for pulling files from a download link. To use it, just navigate to the directory that you wish the file to be downloaded to, copy the link to your file, and use the following command.

.. code-block:: console

  [skelting1@buddy ~]$ cd my_directory
  [skelting1@buddy my_directory]$ wget https://www.google.com/images/branding/googlelogo/2x/googlelogo_light_color_272x92dp.png

This example downloads the google banner image.

.. warning::
   Since wget allows you to pull data from another source, it can be dangerous. It is important to be sure your download link is correct, you know what you are downloading and you verify the correct file has been downloaded

sftp
____
Sftp is a file transfer protocol with a utility similar to ssh which we discussed in a previous section.

.. code-block:: console

  [myuser@mycomputer ~]$ sftp buddyUsername@buddy.uco.edu
  sftp>

.. note::
   You are able to use the ``ls`` and the ``cd`` commands within the sftp prompt so basic navigation is possible.

To move files from your end to buddy first navigate to the directory where your file is and then move the file to buddy using sftp and the ``put`` command.

.. code-block:: console

  [myuser@mycomputer ~]$ ls
  myfile1.txt myfile2.dat foobar/
  [myuser@mycomputer ~]$ sftp buddyUsername@buddy.uco.edu
  sftp> put myfile1.txt
  Uploading myfile1.txt  to /home/buddyUsername/myfile.txt
  myfile.txt                 100%  236KB   4.5MB/s   00:00

Files can be retrieved from a remote server by connecting to it via sftp and using the ``get`` command. The file will be downloaded to whichever directory you were in when you connected via sftp.

.. code-block:: console

  sftp> get myfile1.txt
  Fetching /home/buddyUsername/myfile1.txt to myfile1.txt
  myfile1.txt                100%  236KB  34.4KB/s   00:06

To leave an sftp session use the ``exit`` command.

.. code-block:: console

  sftp> exit
  [myuser@mycomputer ~]$ 

git
___
See :doc:`github </general/git>` section

Tips and Tricks
---------------
Some rapid fire tips and tricks

#. If you use a command often enough, you will learn it. Otherwise don't be ashamed to look it up. There is no point in memorizing something you'll never use and even experienced linux users look things up regularly so you're in good company
#. Tab complete is your friend. Just type enough of something to uniquely identify it and then press tab to fill in the rest. It saves so much time
#. The ``Home`` key allows you to jump to the beginning of a line while the ``End`` key jumps to the end.
#. If you want to stop a command from running before it finishes or you want to get out of something try pressing ``Ctrl+c``. This sends a keyborard interrupt which should tell the command to halt
#. When you are first learning the terminal and using different commands it is common to get stuck inside of something and not know how to get out of it. When this happens it is common practice to spam the keys that are most commonly used to escape various programs. Try ``q`` for quit, ``ESC`` for escape, ``Ctrl+c`` sends a keyboard interrupt and should kill the command you are inside of, ``Ctrl+d`` sometimes works if ``Ctrl+c`` fails, if you are able to type try typing "exit" or "quit", and if all else fails just close the terminal window and open a new one; we've all had to do that once or twice

Basic Bash Scripting
--------------------
Sometimes you may find that you need to run several commands one after another or even with some additional logic like branching or loops; this is where scripting becomes useful. The idea is to write down a series of commands within a logical structure in a file and then execute the file just like a normal program. Scripting makes it possible to handle complex scenarios in a repeatable way which is why we use them to submit jobs to the cluster using slurm. Though bash scripts can be executed directly, scripts on Buddy must be run using slurm. See :doc:`the slurm section </general/slurm>` for more information.

Hello World
~~~~~~~~~~~
Every script begins with a shebang, ``#!``, followed by the path to the appropriate interpreter which is ``/bin/bash`` in this case so our hello world script will begin like so:

.. code-block:: bash
   :linenos:
   :caption: hello_world.sh

   #!/bin/bash

To print "hello world" to the terminal we can use the ``echo`` command. Lines beginning with a hash, ``#``, are comments. They are not executed by the interpreter and are just for the benefit of anyone reading the code. We will add a comment to label our simple script.

.. code-block:: bash
   :linenos:
   :caption: hello_world.sh

   #!/bin/bash

   # This statement prints hello world to the terminal
   echo "hello world"

Basic Logic
~~~~~~~~~~~
.. warning::
    Spaces and newlines are very important parts of the bash syntax. Something as simple as adding a space or forgetting to add one can cause a difficult to find error so pay attention to leading and trailing spaces in the following examples

Variables
_________
An essential part of any programming language is how variables are handled.

.. code-block:: bash
   :linenos:
   :caption: variables.sh

   #!/bin/bash

   # Declare variable in bash. Notice: No space before or after the =
   my_variable=8

   #reference variable in bash
   echo $my_variable

It is important to note that variables in bash are untyped. You can treat them as strings that are interpreted depending on the situation

Branching and Conditions
________________________
One of the most ubiquitous and most useful programming structures are branching statements which decide which code block to run based on the provided condition.

Here are some of the conditions available in bash

+-------------------+-----------------------------------------------------------------------+
| condition         | description                                                           |
+===================+=======================================================================+
| $a -eq $b         | returns true if a and b are equal (both are numbers)                  |
+-------------------+-----------------------------------------------------------------------+
| $a -lt $b         | returns true if a is less than b (both are numbers)                   |
+-------------------+-----------------------------------------------------------------------+
| $a -gt $b         | returns true if a is greater than b (both are numbers)                |
+-------------------+-----------------------------------------------------------------------+
| $a == $b          | returns true if a and b are equivalent (both are strings)             |
+-------------------+-----------------------------------------------------------------------+
| $a != $b          | returns true if a and b are not equivalent (both are strings)         |
+-------------------+-----------------------------------------------------------------------+
| ! [ `condition` ] | returns true if condition is false                                    |
+-------------------+-----------------------------------------------------------------------+
| -d $a             | return true if directory at path a exists                             |
+-------------------+-----------------------------------------------------------------------+
| -e $a             | return true if file at path a exists                                  |
+-------------------+-----------------------------------------------------------------------+
| -r $a             | return true if file at path a exists and can be read                  |
+-------------------+-----------------------------------------------------------------------+
| -w $a             | return true if file at path a exists and can be written to            |
+-------------------+-----------------------------------------------------------------------+
| -x $a             | return true if file at path a exists and can be executed              |
+-------------------+-----------------------------------------------------------------------+
| -z "$a"           | return true if variable a is defined                                  |
+-------------------+-----------------------------------------------------------------------+

Bash branches might look a little strange if you have used another programming language like python or java.

.. code-block:: bash
   :linenos:
   :caption: branching.sh

   #!/bin/bash

   # branching. Note the spaces before and after the condition
   if [ condition ]
   then
       echo condition is true
   elif [ condition2 ]
   then
       echo condition is false and condition2 is true
   else
       echo condition and condition2 are false
   fi

There are a few things to unpack here. Firstly the if block ends with ``fi``. Statement blocks in bash end with the block name spelled backwards. Secondly after a conditional statement like ``if`` and ``elif`` the body is declared with a ``then`` statement. Finally, statements are separated by new lines. However, multiple statements can be declared on the same line by separating them with a ``;``. This feature allow us to rewrite the above example in a different way which you do tend to see if you search for examples online. The style you choose is up to you but here is how the above example looks making use of ``;``.

.. code-block:: bash
   :linenos:
   :caption: branching.sh

   #!/bin/bash
   
   # branching
   if [ condition ]; then
       echo condition is true
   elif [ condition2 ]; then
       echo condition is false and condition2 is true
   else
       echo condition and condition2 are false
   fi
   
.. note:: 
    conditions in bash can get complicated when you start to branch out to using different "test constructs" like ``(())`` and ``[]`` and unusual operators like ``-z`` which checks if a variable is defined. Don't worry about learning these until you run into a situation that requires them

Loops
_____
Loops are essential for any programming language and bash has three varieties: while loops, until loops, and for loops. All loop blocks begin with do and end with done.

.. code-block:: bash
   :linenos:
   :caption: loops.sh

   #!/bin/bash

   ### The following loops are equivalent

   # While loop
   a=0
   while [ $a -le 5 ]; do
       echo a equals: $a
       ((a=a+1))
   done
   
   # until loop
   a=0
   until [ $a -ge 5 ]; do
       echo a equals: $a
       ((a=a+1))
   done
   
   # For loop
   # Note that the variable "a" after the "for" does not come after a "$". 
   #    This is because a is being declared here and is set equal to each 
   #    value in the sequence "0 .. 4" one after the other.
   for a in {0 .. 4} ; do
       echo a equals: $a
   done
   
.. note::
    in the for loop example, ``..`` declare a range from 0 up to and including 4 . If it is equivalent to just typing 0 1 2 3 4 .


Providing Input
~~~~~~~~~~~~~~~
Passing input to a script from the command line is as simple as including your input, separated by spaces, after you invoke the script.

.. code-block:: console

  [skelting1@buddy ~]$ sbatch input_example.sh input1 input2 input3 input4

Then each input will be available within your script through number variables along with the name of the script in the 0 number variable.

.. code-block:: bash
   :linenos:
   :caption: input_example.sh

   #!/bin/bash

   echo this script is called: $0
   echo input one is: $1
   echo input two is: $2
   echo input three is: $3
   echo input four is: $4

All inputs and the name of the script can also be accessed in an array ``$@``.

.. code-block:: bash
   :linenos:
   :caption: input_example.sh

   #!/bin/bash

   echo input command: $@

Troubleshooting
~~~~~~~~~~~~~~~

Basic debugging involves:
  #. Identifying the error message
  #. Determining the source of the bug
  #. Fixing the bug

Identifying the error message may or may not be easy depending on how clear the ouptut of your command is and how much output there is. There is a tendency for error messages to get burried in the output of software if it is poorly written or simply complex. Take time and read carefully to figure out what the computer is trying to tell you about what has gone wrong.

.. note::
   Warnings are different from errors in that they indicate bad practice, outdated commands, or other minor issues while errors indicate serious issues. They can sometimes hint at the source of an error but that is after you have looked into any error messages that you find.

Determining the source of the bug usually involves some knowledge of how your program is constructed though some error messages will tell you the line number that the error occured on (and we are incredibly grateful for that). A powerful technique is to simply copy the error message (or part of the message) into a web browser and search for other people who have had the same problem. This is usually the first step if your someone else's software and is very common even and especially with professional programmers. Internet searching is a skill in and of itself so we won't go into detail except to say that there is plenty of helpful information out there as well plenty of misleading information. Be careful when following someone's advice and even then, take precautions, make backups and contact administration if you are unsure or have any questions.

Fixing the bug is the hard part. If you misidentified the actual error message or the real cause of the error then you will make a fix and it won't work or might even break something else. Part of working through this last step is going back to the previous two and trying something else. Reread the error message, try changing the way you phrase your search, gather more information, and try again. Debugging can often feel like you're battling with the computer and it is refusing to yeild. If you get stuck or have any questions contact administration with your bug and some of the information you collected and we will try to help you narrow down your issue. 

